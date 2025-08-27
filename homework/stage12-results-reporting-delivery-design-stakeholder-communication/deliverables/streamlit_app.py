# In terminal run:
# streamlit run /Users/aditya/Documents/bootcamp_aditya_shah/homework/stage12-results-reporting-delivery-design-stakeholder-communication/deliverables/streamlit_app.py

import streamlit as st
from pathlib import Path

# === Setup ===
st.set_page_config(layout="wide")

# Point to correct folder where your images actually are
img_dir = Path("/Users/aditya/Documents/bootcamp_aditya_shah/homework/stage12-results-reporting-delivery-design-stakeholder-communication/deliverables/images")  

slides = [
    "Title + Executive Summary",
    "Key Chart 1 (Risk–Return)",
    "Key Chart 2 (Scenario Impact)",
    "Assumptions & Risks",
    "Sensitivity Summary"
]

# === Helper function (safe image loading) ===
def safe_image(path, caption):
    try:
        st.image(str(path), caption=caption, use_container_width=True)
    except Exception:
        st.warning(f"⚠️ Could not load image: {path}")

# === Navigation ===
st.sidebar.title("📊 Scenario PPT Navigator")
current_slide = st.sidebar.radio("Go to Slide:", slides)

# === SLIDE 1: Title + Executive Summary ===
if current_slide == "Title + Executive Summary":
    st.title("Scenario Analysis Report")
    st.subheader("Executive Summary")
    st.write("""
    - Baseline delivers a balanced profile (Sharpe ~0.56).  
    - Alt-impute lowers risk-adjusted return (Sharpe ~0.49).  
    - Alt-outlier shows strongest Sharpe (0.61) but with higher volatility.  
    """)

# === SLIDE 2: Risk–Return ===
elif current_slide == "Key Chart 1 (Risk–Return)":
    st.header("Risk–Return Tradeoff")
    safe_image(img_dir / "risk_return.png", "Risk–Return by Scenario")
    st.write("""
    **Takeaway**: The outlier-adjusted scenario has the best Sharpe ratio 
    but comes with slightly higher volatility.  
    """)

# === SLIDE 3: Scenario Impact ===
elif current_slide == "Key Chart 2 (Scenario Impact)":
    st.header("Scenario Impact on Returns")
    safe_image(img_dir / "return_by_scenario.png", "Return by Scenario")
    st.write("""
    **Takeaway**: Alt-impute underperforms, while outlier-adjusted delivers the highest return.  
    """)

# === SLIDE 4: Assumptions & Risks ===
elif current_slide == "Assumptions & Risks":
    st.header("Assumptions & Risks")
    st.write("""
    **Assumptions**  
    - Baseline uses median imputation for missing values.  
    - Alt-impute uses mean imputation, which may be skewed by outliers.  
    - Alt-outlier removes >3σ outliers, which can reduce noise but risks losing valuable data.  

    **Risks**  
    - Overfitting decisions to past noise.  
    - Limited sample size may distort inference.  
    - Assumption-driven bias could affect generalization.  
    """)

# === SLIDE 5: Sensitivity Summary ===
elif current_slide == "Sensitivity Summary":
    st.header("Sensitivity Summary & Implications")
    safe_image(img_dir / "metricA_over_time.png", "MetricA Over Time")
    st.write("""
    **Summary**  
    - Baseline is the most stable.  
    - Alt-outlier provides stronger Sharpe and return but assumes data filtering.  
    - Alt-impute looks weaker overall.  

    **What this means for you**  
    - If you value **stability**, baseline is the safer choice.  
    - If you seek **higher returns with acceptable volatility**, outlier-adjusted is better.  
    - Mean imputation is less reliable and not recommended.  
    """)
