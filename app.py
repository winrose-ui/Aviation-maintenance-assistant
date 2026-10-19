import streamlit as st
import pandas as pd
import json
from pathlib import Path

st.set_page_config(
    page_title="Aviation Log Validator",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ Aviation Maintenance Log Validator")
st.write(
    "An educational tool for checking fictional maintenance "
    "records for missing information and data inconsistencies."
)

st.warning(
    "Educational prototype only. This tool does not determine "
    "aircraft airworthiness or certify regulatory compliance."
)

st.subheader("Generate and review test records")

if st.button("Load sample records"):
    file_path = Path("sample_logs.json")

    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as file:
            records = json.load(file)

        st.session_state["records"] = records
    else:
        st.info(
            "No sample file exists yet. Generate the records "
            "using log_generator.py first."
        )

if "records" in st.session_state:
    records = st.session_state["records"]

    st.metric("Test records loaded", len(records))
    st.dataframe(pd.DataFrame(records), use_container_width=True)

    st.caption(
        "All displayed records should be fictional test data."
    )
else:
    st.info("Click 'Load sample records' after generating the test data.")
