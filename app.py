import streamlit as st
from resume_analyzer import extract_text_from_pdf, analyze_resume


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)


# Main heading
st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with the skills "
    "required for a job."
)


# Upload resume
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)


# Job keywords
keywords_input = st.text_input(
    "Enter required skills/keywords (comma-separated):",
    "Python, SQL, Machine Learning, Data Analysis"
)


# Analyze when a file is uploaded
if uploaded_file is not None:

    st.success("Resume uploaded successfully! ✅")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(uploaded_file)

    # Convert keywords into a list
    keywords = [
        keyword.strip()
        for keyword in keywords_input.split(",")
        if keyword.strip()
    ]

    # Analyze resume
    result = analyze_resume(
        resume_text,
        keywords
    )

    # Results
    st.subheader("📊 Resume Analysis")

    # Word count
    st.write(
        f"**Word Count:** {result['word_count']}"
    )

    # Skills/entities found
    st.subheader("✅ Skills / Entities Found")

    if result["skills_found"]:
        st.write(
            ", ".join(result["skills_found"])
        )
    else:
        st.write("No entities detected.")

    # Missing keywords
    st.subheader("❌ Missing Job Keywords")

    if result["missing_keywords"]:
        st.warning(
            ", ".join(result["missing_keywords"])
        )
    else:
        st.success(
            "Your resume contains all the required keywords! 🎉"
        )

    # Show extracted text
    with st.expander("📜 View Extracted Resume Text"):
        st.text(resume_text)
        