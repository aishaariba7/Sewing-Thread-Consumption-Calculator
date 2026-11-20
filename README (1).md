# Sewing Thread Consumption Calculator

**Course:** AI234 – Artificial Intelligence  
**Department:** Textile Engineering, MUET Jamshoro  
**Assigned topic:** Sewing Thread Consumption Calculator  
**Roll number:** 25TE062

## Project purpose

This Streamlit web application estimates the amount of sewing thread needed for a seam or garment order. The user selects a stitch type and enters seam length, number of identical seams/garments, a thread-consumption factor, wastage allowance, and usable thread length per cone.

## Main features

- Stitch-type selection: Lockstitch, Chain stitch, Overlock, Coverstitch, or custom.
- Inputs for seam length and number of seams/garments.
- Editable thread-consumption factor.
- Wastage allowance.
- Estimated total thread in meters.
- Estimated number of cones.
- Calculation breakdown and a simple bar chart.
- Limitations and responsible-use note.

## Formula

1. Total seam length = seam length × number of identical seams/garments
2. Thread before wastage = total seam length × thread-consumption factor
3. Total thread = thread before wastage × (1 + wastage % / 100)
4. Cones required = round up(total thread / usable thread length per cone)

## Important note about assumptions

The preset stitch factors in `app.py` are illustrative starting values for an educational demonstration. They are not claimed to be official textile-industry standards. Actual consumption depends on stitch density, stitch class, seam construction, fabric thickness, thread size, machine settings, and production practice. For accurate production planning, use a factor measured from a sample seam or provided by a reliable production source.

## Files

- `app.py` – Streamlit application.
- `requirements.txt` – Python package requirements.
- `README.md` – Project description and instructions.

## Run locally

1. Install Python.
2. Open a terminal in this project folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Deploy using GitHub and Streamlit Community Cloud

1. Create a **public** GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. Sign in to Streamlit Community Cloud using GitHub.
4. Create a new app, select this repository, and set the main file path to `app.py`.
5. Deploy and test the public app URL.

## Responsible AI and limitations

This version is a transparent, rule-based calculator rather than a trained machine-learning model. It does not independently learn from factory production data. Its outputs are estimates based on user-entered assumptions. Users should verify the thread factor and cone length before relying on the results.
