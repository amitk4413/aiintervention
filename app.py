import streamlit as st
import tempfile
import os
import json

from dotenv import load_dotenv
load_dotenv()

from tools.file_reader import read_file
from llm_structured import generate_jira_structure
from utils.json_cleaner import extract_json
from utils.jira_uploader import push_to_jira


st.set_page_config(page_title="AI SDLC → Jira Generator", layout="wide")

st.markdown(
    "<h2 style='text-align:center;'>📄 AI SDLC → Jira Ticket Generator</h2>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload requirement document (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

parsed = None

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    text = read_file(file_path)

    st.subheader("📄 Extracted Text Preview")
    st.write(text[:2000])

    if st.button("🚀 Generate Jira Stories"):

        try:
            st.info("Generating Jira structure...")

            raw_output = generate_jira_structure(text)

            st.subheader("🧠 Raw Output")
            st.code(raw_output)

            parsed = extract_json(raw_output)

            st.subheader("✅ Parsed Jira JSON")
            st.json(parsed)

            st.session_state["jira_data"] = parsed

        except Exception as e:
            st.error("Failed to generate Jira structure")
            st.exception(e)


# =========================
# PUSH TO JIRA
# =========================
if "jira_data" in st.session_state:

    st.divider()
    st.subheader("🚀 Push to Jira")

    if st.button("Create Jira Tickets"):

        try:
            with st.spinner("Creating Jira issues..."):
                result = push_to_jira(st.session_state["jira_data"])

            st.success("Jira tickets created successfully!")
            st.json(result)

        except Exception as e:
            st.error("Jira creation failed")
            st.exception(e)