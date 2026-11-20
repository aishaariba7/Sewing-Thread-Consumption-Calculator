# Sewing Thread Consumption Calculator

**Course:** AI234 – Artificial Intelligence  
**Department:** Textile Engineering, MUET Jamshoro  
**Assigned topic:** Sewing Thread Consumption Calculator  
**Roll number:** 25TE062

## Purpose

This Streamlit application estimates sewing thread consumption for a seam or garment order and estimates the number of cones required.

## Features

- Select stitch type.
- Enter seam length and number of identical seams/garments.
- Adjust the thread consumption factor.
- Add a wastage allowance.
- Enter usable thread length per cone.
- Calculate total thread consumption in meters.
- Estimate the number of cones.
- View a calculation breakdown and a horizontal bar chart.
- Read a limitations and responsible-use note.

## Formula

1. Total seam length = seam length × number of identical seams/garments
2. Thread before wastage = total seam length × thread consumption factor
3. Total thread = thread before wastage × (1 + wastage percentage / 100)
4. Cones required = round up(total thread / usable thread length per cone)

## Important assumptions

Preset stitch factors are illustrative educational starting values, not official industry standards. Actual thread consumption depends on stitch density, stitch class, seam construction, fabric thickness, thread size, machine settings, and production practice. Use a measured or instructor-provided factor for more reliable results.

## Project files

- `app.py` – Streamlit application.
- `requirements.txt` – Required Python packages.
- `README.md` – Project information and instructions.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

Upload all three files to a public GitHub repository. In Streamlit Community Cloud, connect the repository and select `app.py` as the main file.

## Responsible AI and limitations

This version is a transparent, rule-based calculator, not a trained machine-learning model. Its results are estimates based on user inputs and assumptions. Verify the consumption factor and usable cone length before using results for production decisions.
