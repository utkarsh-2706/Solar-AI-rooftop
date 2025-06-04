# ☀️ Solar Rooftop Analysis AI Tool

An AI-powered rooftop analysis system that leverages satellite imagery to assess solar installation potential, provide tailored recommendations, and estimate return on investment (ROI). Designed to assist homeowners and solar professionals in making data-driven solar decisions.

---

## 🚀 Project Overview

This intelligent system enables users to upload satellite images of rooftops and receive:

* ✅ Rooftop suitability assessment
* ⚙️ Solar installation recommendations
* 📊 ROI and cost-benefit insights
* 🤖 AI-powered suggestions via LLM (Groq/LLama3)

The assistant is designed to align with the evolving solar industry by integrating vision analysis, prompt-engineering-based summarization, and accurate estimations.

---

## 🛠️ Tech Stack

| Domain                | Tools & Tech                             |
| --------------------- | ---------------------------------------- |
| Frontend              | [Streamlit](https://streamlit.io/)       |
| Backend / API         | Python                                   |
| Vision AI             | `transformers`, `PIL`                    |
| LLM                   | Groq (LLama3-70B via API)                |
| Deployment (optional) | Streamlit Cloud / Hugging Face Spaces    |
| Others                | `dotenv`, `requests`, `os`, `json`, etc. |

---

## 📁 Project Structure

```
Solar-AI-rooftop/
├── app.py                             # Main Streamlit web app
├── analyzer/
│   ├── __init__.py
│   ├── rooftop_segmenter.py          # Image segmentation module
│   ├── solar_calculator.py           # Panel layout & ROI logic
│   └── llm_assistant.py              # OpenRouter / LLM API integration
├── utils/
│   ├── __init__.py
│   ├── image_utils.py                # Resizing, preprocessing helpers
│   └── geo_utils.py                  # Sun angle, irradiance, etc.
├── assets/
│   └── sample_images/                # Test satellite images
├── outputs/
│   └── reports/                      # JSON or PDF reports
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml                   # Streamlit configuration (optional)

```

---

## 🥪 How to Run Locally

### 1. Clone the repo or unzip the folder

```bash
git clone https://github.com/utkarsh-2706/Solar-AI-rooftop.git
cd Solar-AI-rooftop
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv myenv
source myenv/bin/activate  # or `myenv\Scripts\activate` on Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Add API Key (Groq via .env)

Create a `.env` file in the root folder and paste your API key:

```
GROQ_API_KEY=gsk_your_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🖼️ Example Usage

1. Launch the app in your browser.
2. Upload a rooftop satellite image from `assets/sample_images/`.
3. View:

   * Rooftop suitability info
   * ROI summary
   * Installation recommendation
4. Click **"Ask AI for Recommendations"** to get advice from LLama3-based assistant (via Groq).

---


## 🛌 Acknowledgements

* [Groq API](https://console.groq.com/)
* [Hugging Face Transformers](https://huggingface.co/)
* [Streamlit](https://streamlit.io/)
* [OpenRouter](https://openrouter.ai/) *(if used as fallback)*

---

## 📬 Contact

**Utkarsh Sharma**
Email: `sharmautkarsh2706@gamil.com`

---
