import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="NGO Proposal Builder Demo",
    page_icon="📘",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
/* Main app background */
.stApp {
    background-color: #f8fafc;
}

/* Main title */
.main-title {
    color: #0b3d91;
    font-size: 2.2rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
}

.sub-text {
    color: #1f2937;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}

/* Section card */
.form-card {
    background: rgba(255,255,255,0.88);
    padding: 1.2rem;
    border-radius: 14px;
    border: 1px solid #dbe4f0;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}

/* Labels and text */
label, .stMarkdown, .stText, .stTextInput, .stTextArea, .stSelectbox {
    color: #111827 !important;
}

/* Inputs */
input, textarea {
    color: #111827 !important;
    background-color: #ffffff !important;
}

/* Buttons */
.stButton > button {
    background-color: #0b3d91;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.55rem 1rem;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #082c6c;
    color: white;
}

/* Download button */
.stDownloadButton > button {
    background-color: #14532d;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.55rem 1rem;
    font-weight: 600;
}

.stDownloadButton > button:hover {
    background-color: #0f3d21;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b3d91 0%, #14532d 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Text areas in output */
textarea {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session State Initialization
# -----------------------------
default_values = {
    "step": 1,
    "ngo_name": "",
    "project_title": "",
    "project_type": "Education",
    "location": "",
    "duration": "",
    "beneficiaries": "",
    "problem_statement": "",
    "goals": "",
    "expected_outcomes": "",
    "activities": "",
    "budget": "",
    "resources_needed": "",
    "budget_notes": "",
    "challenges": "",
    "risks": "",
    "mitigation": "",
    "additional_notes": "",
    "submitted": False
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------------
# Helper Functions
# -----------------------------
def next_step():
    if st.session_state.step < 5:
        st.session_state.step += 1
    st.rerun()

def prev_step():
    if st.session_state.step > 1:
        st.session_state.step -= 1
    st.rerun()

def reset_form():
    for key, value in default_values.items():
        st.session_state[key] = value
    st.rerun()

def collect_form_data():
    return {
        "NGO Name": st.session_state.ngo_name,
        "Project Title": st.session_state.project_title,
        "Project Type": st.session_state.project_type,
        "Location": st.session_state.location,
        "Duration": st.session_state.duration,
        "Target Beneficiaries": st.session_state.beneficiaries,
        "Problem Statement": st.session_state.problem_statement,
        "Goals/Objectives": st.session_state.goals,
        "Expected Outcomes": st.session_state.expected_outcomes,
        "Key Activities": st.session_state.activities,
        "Estimated Budget": st.session_state.budget,
        "Resources Needed": st.session_state.resources_needed,
        "Budget Notes": st.session_state.budget_notes,
        "Potential Challenges": st.session_state.challenges,
        "Risks": st.session_state.risks,
        "Mitigation Strategies": st.session_state.mitigation,
        "Additional Notes": st.session_state.additional_notes
    }

def generate_report_text(data):
    lines = []
    lines.append("NGO PROPOSAL BUILDER DEMO")
    lines.append("=" * 40)
    lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    for key, value in data.items():
        lines.append(f"{key}:")
        lines.append(f"{value if value else 'N/A'}")
        lines.append("")

    return "\n".join(lines)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📘 NGO Proposal Builder Demo")
st.sidebar.write("Use the steps below to complete the proposal form.")

steps = {
    1: "Basic Information",
    2: "Needs & Goals",
    3: "Activities & Budget",
    4: "Risks & Notes",
    5: "Review & Download"
}

for num, label in steps.items():
    if st.session_state.step == num:
        st.sidebar.markdown(f"**➜ Step {num}: {label}**")
    else:
        st.sidebar.write(f"Step {num}: {label}")

st.sidebar.divider()

if st.sidebar.button("Reset Form"):
    reset_form()

# -----------------------------
# Main Title
# -----------------------------
st.markdown('<div class="main-title">NGO Proposal Builder Demo</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">Create a simple NGO project proposal using this guided multi-step form.</div>',
    unsafe_allow_html=True
)

st.progress(st.session_state.step / 5)

# -----------------------------
# Step 1
# -----------------------------
if st.session_state.step == 1:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("Step 1: Basic Information")

    col1, col2 = st.columns(2)

    with col1:
        st.session_state.ngo_name = st.text_input("NGO Name", value=st.session_state.ngo_name)
        st.session_state.project_title = st.text_input("Project Title", value=st.session_state.project_title)
        project_types = ["Education", "Health", "Agriculture", "Youth Empowerment", "Women Empowerment", "Environment", "Other"]
        current_index = project_types.index(st.session_state.project_type) if st.session_state.project_type in project_types else 0
        st.session_state.project_type = st.selectbox("Project Type", project_types, index=current_index)

    with col2:
        st.session_state.location = st.text_input("Project Location", value=st.session_state.location)
        st.session_state.duration = st.text_input("Project Duration", value=st.session_state.duration, placeholder="e.g. 6 months")

    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 4])
    with c2:
        if st.button("Next"):
            next_step()

# -----------------------------
# Step 2
# -----------------------------
elif st.session_state.step == 2:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("Step 2: Needs Assessment & Goals")

    st.session_state.beneficiaries = st.text_area(
        "Target Beneficiaries",
        value=st.session_state.beneficiaries,
        placeholder="Who will benefit from this project?"
    )

    st.session_state.problem_statement = st.text_area(
        "Problem Statement",
        value=st.session_state.problem_statement,
        placeholder="What problem is the project trying to solve?"
    )

    st.session_state.goals = st.text_area(
        "Project Goals/Objectives",
        value=st.session_state.goals,
        placeholder="What are the main goals of the project?"
    )

    st.session_state.expected_outcomes = st.text_area(
        "Expected Outcomes",
        value=st.session_state.expected_outcomes,
        placeholder="What results do you expect from the project?"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 3])
    with c1:
        if st.button("Back"):
            prev_step()
    with c2:
        if st.button("Next"):
            next_step()

# -----------------------------
# Step 3
# -----------------------------
elif st.session_state.step == 3:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("Step 3: Activities & Budget")

    st.session_state.activities = st.text_area(
        "Key Activities",
        value=st.session_state.activities,
        placeholder="List the major project activities"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.session_state.budget = st.text_area(
            "Estimated Budget",
            value=st.session_state.budget,
            placeholder="Enter estimated costs"
        )

    with col2:
        st.session_state.resources_needed = st.text_area(
            "Resources Needed",
            value=st.session_state.resources_needed,
            placeholder="Staff, equipment, materials, etc."
        )

    st.session_state.budget_notes = st.text_area(
        "Budget Notes",
        value=st.session_state.budget_notes,
        placeholder="Any extra explanation about the budget"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 3])
    with c1:
        if st.button("Back"):
            prev_step()
    with c2:
        if st.button("Next"):
            next_step()

# -----------------------------
# Step 4
# -----------------------------
elif st.session_state.step == 4:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("Step 4: Risks & Additional Notes")

    st.session_state.challenges = st.text_area(
        "Potential Challenges",
        value=st.session_state.challenges,
        placeholder="What challenges might affect implementation?"
    )

    st.session_state.risks = st.text_area(
        "Risks",
        value=st.session_state.risks,
        placeholder="What risks should be considered?"
    )

    st.session_state.mitigation = st.text_area(
        "Mitigation Strategies",
        value=st.session_state.mitigation,
        placeholder="How will the risks be managed?"
    )

    st.session_state.additional_notes = st.text_area(
        "Additional Notes",
        value=st.session_state.additional_notes,
        placeholder="Any other useful information"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 3])
    with c1:
        if st.button("Back"):
            prev_step()
    with c2:
        if st.button("Next"):
            next_step()

# -----------------------------
# Step 5
# -----------------------------
elif st.session_state.step == 5:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("Step 5: Review & Download")

    data = collect_form_data()

    with st.expander("View Proposal Details", expanded=True):
        for key, value in data.items():
            st.markdown(f"**{key}:** {value if value else 'N/A'}")

    report_text = generate_report_text(data)

    st.text_area("Generated Proposal Preview", report_text, height=350)

    safe_title = st.session_state.project_title.strip().replace(" ", "_") if st.session_state.project_title.strip() else "proposal"
    filename = f"{safe_title}.txt"

    st.download_button(
        label="Download Proposal",
        data=report_text,
        file_name=filename,
        mime="text/plain"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 3])
    with c1:
        if st.button("Back"):
            prev_step()
    with c2:
        if st.button("Start Over"):
            reset_form()
