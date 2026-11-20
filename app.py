import math
import streamlit as st

st.set_page_config(
    page_title="Sewing Thread Consumption Calculator",
    page_icon="🧵",
    layout="centered"
)

# Illustrative starting factors only. Actual values depend on stitch class,
# stitch density, fabric thickness, seam construction, and machine settings.
STITCH_FACTORS = {
    "Lockstitch": 2.5,
    "Chain stitch": 3.0,
    "Overlock": 4.0,
    "Coverstitch": 4.5,
    "Other / custom": 2.5,
}

st.title("🧵 Sewing Thread Consumption Calculator")
st.write(
    "Estimate the total sewing thread required for a garment order. "
    "Choose a stitch type, enter the seam length, and adjust the assumptions "
    "to match your production information."
)

st.info(
    "This is an educational estimation tool. The stitch factors shown are "
    "illustrative starting values, not fixed industry standards. Use a factor "
    "measured from your own sewing sample or supplied by your instructor/mill "
    "for a more reliable estimate."
)

st.header("1. Enter production details")

stitch_type = st.selectbox(
    "Select stitch type",
    list(STITCH_FACTORS.keys())
)

col1, col2 = st.columns(2)
with col1:
    seam_length = st.number_input(
        "Seam length (meters)",
        min_value=0.0,
        value=100.0,
        step=1.0,
        help="Length of one seam or the combined seam length for one garment."
    )
with col2:
    number_of_seams = st.number_input(
        "Number of identical seams / garments",
        min_value=1,
        value=1,
        step=1,
        help="Use 1 if the seam length entered is already the total order length."
    )

st.header("2. Set estimation assumptions")

default_factor = STITCH_FACTORS[stitch_type]
thread_factor = st.number_input(
    "Thread consumption factor (meters of thread per meter of seam)",
    min_value=0.1,
    value=float(default_factor),
    step=0.1,
    help="The total factor should account for all threads used by the selected stitch."
)

wastage_percent = st.number_input(
    "Extra thread / wastage allowance (%)",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=1.0
)

cone_length = st.number_input(
    "Usable thread length per cone (meters)",
    min_value=1.0,
    value=5000.0,
    step=500.0,
    help="Change this to the usable length printed on the cone or provided by the supplier."
)

st.caption(
    f"Suggested starting factor for {stitch_type}: {default_factor:.1f}. "
    "You can edit it if you have a measured value."
)

st.header("3. Estimated result")

if st.button("Calculate thread requirement", type="primary", use_container_width=True):
    total_seam_length = seam_length * number_of_seams
    basic_thread = total_seam_length * thread_factor
    wastage_thread = basic_thread * (wastage_percent / 100)
    total_thread = basic_thread + wastage_thread
    cones_required = math.ceil(total_thread / cone_length) if total_thread > 0 else 0

    c1, c2 = st.columns(2)
    c1.metric("Total seam length", f"{total_seam_length:,.2f} m")
    c2.metric("Estimated thread", f"{total_thread:,.2f} m")

    c3, c4 = st.columns(2)
    c3.metric("Thread before wastage", f"{basic_thread:,.2f} m")
    c4.metric("Cones required", f"{cones_required:,}")

    st.subheader("Calculation breakdown")
    st.dataframe(
        {
            "Item": [
                "Total seam length",
                "Thread before wastage",
                "Wastage allowance",
                "Total estimated thread",
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
        },
        hide_index=True,
        use_container_width=True,
    )

    st.bar_chart(
        {
            "Thread length (meters)": {
                "Before wastage": basic_thread,
                "Wastage": wastage_thread,
                "Total": total_thread,
            }
        }
    )

    st.success(
        f"Estimated requirement: {total_thread:,.2f} meters of thread "
        f"({cones_required} cone(s))."
    )

st.divider()
st.subheader("Formula used")
st.latex(r" L_s = \text{seam length} \times \text{number of seams}")
st.latex(r" T_b = L_s \times F")
st.latex(r" T = T_b \times \left(1 + \frac{W}{100}\right)")
st.latex(r" \text{Cones} = \left\lceil \frac{T}{C} \right\rceil")

st.write("Where:")
st.markdown(
    """
    - **Lₛ** = total seam length (m)
    - **Tᵦ** = thread required before wastage (m)
    - **F** = thread consumption factor
    - **W** = wastage allowance (%)
    - **T** = total estimated thread (m)
    - **C** = usable thread length per cone (m)
    """
)

st.divider()
st.subheader("Limitations & Responsible Use")
st.write(
    "This calculator uses simplified assumptions. Actual thread consumption "
    "changes with stitch density, stitch type/class, seam construction, fabric "
    "thickness, machine tension, thread size, and operator practices. The preset "
    "factors are examples for learning and must not be treated as verified "
    "production standards. Confirm the factor by measuring thread use on a "
    "sample seam before placing a production order. Do not enter confidential "
    "factory or customer information."
)

st.caption("AI234 Capstone Project | Textile Engineering | MUET Jamshoro")
