def calculate_panel_output(area_m2, efficiency=0.20, irradiance=1000):
    kw_output = (area_m2 * efficiency * irradiance) / 1000  # kW
    return round(kw_output, 2)

def estimate_roi(area_m2, location='India'):
    panel_area = 1.6  # m² per panel
    cost_per_panel = 300  # USD
    savings_per_year = 120  # USD average
    num_panels = int(area_m2 / panel_area)
    total_cost = num_panels * cost_per_panel
    yearly_savings = num_panels * savings_per_year
    payback_years = total_cost / yearly_savings if yearly_savings > 0 else None

    return {
        'panel_count': num_panels,
        'estimated_cost': total_cost,
        'annual_savings': yearly_savings,
        'payback_years': round(payback_years, 2)
    }
