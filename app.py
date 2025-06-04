import streamlit as st
from PIL import Image
from analyzer.rooftop_segmenter import segment_rooftop
from analyzer.solar_calculator import calculate_panel_output, estimate_roi
from analyzer.llm_assistant import query_groq
from dotenv import load_dotenv
load_dotenv()

import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.title("☀️ Rooftop Solar Potential Analyzer")

uploaded = st.file_uploader("Upload a Satellite Image of Rooftop", type=["jpg", "png", "jpeg"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Uploaded Rooftop", use_column_width=True)

    mask, usable_percent = segment_rooftop(image)
    st.image(mask, caption=f"Segmented Rooftop Area ({usable_percent:.2f}%)", use_column_width=True)

    rooftop_area = st.number_input("Estimated Rooftop Area (in m²)", min_value=10, max_value=500, value=50)
    usable_area = rooftop_area * (usable_percent / 100)

    output_kw = calculate_panel_output(usable_area)
    roi = estimate_roi(usable_area)

    st.write("### 📊 Output Summary")
    st.write(f"🔋 Estimated Power Output: {output_kw} kW")
    st.write(f"📦 Number of Panels: {roi['panel_count']}")
    st.write(f"💰 Installation Cost: ${roi['estimated_cost']}")
    st.write(f"💸 Annual Savings: ${roi['annual_savings']}")
    st.write(f"⏳ Payback Period: {roi['payback_years']} years")

    if st.button("Ask AI for Recommendations"):
        prompt = f"""A rooftop has {usable_area:.2f} m² usable space. Suggest optimal panel setup, power output, 
        and ROI. Assume India location, monocrystalline panels (21% efficiency)."""
        ai_response = query_groq(prompt)
        st.markdown("### 🤖 AI Recommendation")
        st.write(ai_response)
