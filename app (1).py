import math
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Sewing Thread Consumption Calculator",
    page_icon="🧵",
    layout="centered"
)

# Educational starting factors only; verify with measured production data.
STITCH_FACTORS = {
    "Lockstitch": 2.5,
    "Chain stitch": 3.0,
    "Overlock": 4.0,
    "Coverstitch": 4.5,
    "Other / custom": 2.5,
}

st.title("🧵 Sewing Thread Consumption Calculator")
st.write(
    "Estimate the sewing thread required for a seam or garment order. "
    "Enter your production details and review the estimated thread length "
    "and number of cones."
)

st.info(
    "Educational estimate: preset stitch factors are illustrative starting "
    "values, not official industry standards. For reliable production planning, "
    "use a factor measured from a sample seam or supplied by your instructor "
    "or production unit."
)

st.header("1. Production details")
stitch_type = st.selectbox("Select stitch type", list(STITCH_FACTORS.keys()))

col1, col2 = st.columns(2)
with col1:
    seam_length = st.number_input(
        "Seam length (meters)", min_value=0.0, value=100.0, step=1.0
    )
with col2:
    number_of_seams = st.number_input(
        "Number of identical seams / garments",
        min_value=1, value=1, step=1
    )

st.header("2. Estimation assumptions")
thread_factor = st.number_input(
    "Thread consumption factor (m thread / m seam)",
    min_value=0.1,
    value=float(STITCH_FACTORS[stitch_type]),
    step=0.1,
    help="Edit this factor if you have a measured or instructor-provided value."
)
wastage_percent = st.number_input(
    "Wastage allowance (%)",
    min_value=0.0, max_value=100.0, value=10.0, step=1.0
)
cone_length = st.number_input(
    "Usable thread per cone (meters)",
    min_value=1.0, value=5000.0, step=500.0
)

st.caption(
    f"Illustrative starting factor for {stitch_type}: "
    f"{STITCH_FACTORS[stitch_type]:.1f}. Adjust it when better data is available."
)

st.header("3. Calculate requirement")
if st.button("Calculate thread requirement", type="primary", use_container_width=True):
    total_seam_length = seam_length * number_of_seams
    basic_thread = total_seam_length * thread_factor
    wastage_thread = basic_thread * (wastage_percent / 100.0)
    total_thread = basic_thread + wastage_thread
    cones_required = math.ceil(total_thread / cone_length) if total_thread > 0 else 0

    st.subheader("Estimated results")
    metric1, metric2 = st.columns(2)
    metric1.metric("Total thread required", f"{total_thread:,.2f} m")
    metric2.metric("Cones required", f"{cones_required:,}")

    breakdown = pd.DataFrame({
        "Item": [
            "Total seam length",
            "Thread before wastage",
            "Wastage allowance",
            "Total thread required",
            "Usable thread per cone",
            "Cones required",
        ],
        "Value": [
            f"{total_seam_length:,.2f} m",
            f"{basic_thread:,.2f} m",
            f"{wastage_thread:,.2f} m",
            f"{total_thread:,.2f} m",
            f"{cone_length:,.2f} m",
            f"{cones_required:,}",
        ],
    })
    st.dataframe(breakdown, hide_index=True, use_container_width=True)

    st.subheader("Thread Consumption Analysis")
    chart_data = pd.DataFrame({
        "Component": ["Before wastage", "Wastage", "Total thread"],
        "Thread length (meters)": [basic_thread, wastage_thread, total_thread],
    }).set_index("Component")

    st.bar_chart(
        chart_data,
        horizontal=True,
        height=260,
        use_container_width=True,
    )
    st.caption(
        "The chart compares thread before wastage, the extra wastage allowance, "
        "and the final estimated thread requirement."
    )

    st.success(
        f"Estimated requirement: {total_thread:,.2f} meters of thread "
        f"({cones_required} cone(s))."
    )

st.divider()
st.subheader("Formula used")
st.latex(r"L_s = \text{seam length} \times \text{number of seams}")
st.latex(r"T_b = L_s \times F")
st.latex(r"T = T_b \times \left(1 + \frac{W}{100}\right)")
st.latex(r"\text{Cones} = \left\lceil \frac{T}{C} \right\rceil")

st.markdown(
    """
    **Where:**
    - \(L_s\) = total seam length (m)
    - \(T_b\) = thread required before wastage (m)
    - \(F\) = thread consumption factor
    - \(W\) = wastage allowance (%)
    - \(T\) = total estimated thread (m)
    - \(C\) = usable thread length per cone (m)
    """
)

st.divider()
st.subheader("Limitations & Responsible Use")
st.write(
    "This is a simplified, rule-based estimation tool, not a trained machine-learning "
    "model. Actual thread consumption depends on stitch density, stitch class, seam "
    "construction, fabric thickness, thread size, machine settings, and production "
    "practice. Preset factors are examples only and must not be treated as verified "
    "industry standards. Confirm the factor using a sample seam before production. "
    "Avoid entering confidential factory or customer information."
)

st.caption("AI234 Capstone Project | Textile Engineering | MUET Jamshoro")
