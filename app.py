import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# -------------------------------
# Load API Key Securely
# -------------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠ GROQ_API_KEY not found. Please set it in your .env file.")
    st.stop()

client = Groq(api_key=api_key)

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Sales & Marketing System",
    page_icon="🚀",
    layout="centered"
)

# -------------------------------
# Custom Styling (Modern UI)
# -------------------------------
st.markdown("""
<style>

    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #1f4e79, #2e86c1);
    }

    /* Main Content Card */
    .block-container {
        padding: 2rem 3rem;
        background: rgba(255, 255, 255, 0.96);
        border-radius: 18px;
        box-shadow: 0px 12px 35px rgba(0, 0, 0, 0.2);
        margin-top: 2rem;
    }

    /* Title */
    .main-title {
        font-size: 36px;
        font-weight: 800;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 16px;
        color: #555;
        margin-bottom: 30px;
    }

    /* Labels */
    .stSelectbox label,
    .stTextArea label {
        font-weight: 600 !important;
        color: #1f4e79 !important;
    }

    /* Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #1f4e79, #2e86c1);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 16px;
        border: none;
        transition: 0.3s ease-in-out;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #154360, #1f618d);
        transform: scale(1.03);
        box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
    }

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header Section
# -------------------------------
st.markdown('<div class="main-title">🚀 AI Sales & Marketing Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Campaigns • AI Lead Scoring • Business Strategy Insights</div>', unsafe_allow_html=True)

# -------------------------------
# Feature Selection
# -------------------------------
feature = st.selectbox(
    "Select Feature",
    [
        "Campaign Generation",
        "Sales Pitch Creation",
        "Lead Scoring",
        "Market Analysis",
        "Business Insights"
    ]
)

user_input = st.text_area("Enter Product / Business Details")

# -------------------------------
# AI Function
# -------------------------------
def generate_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


# -------------------------------
# Generate Button Logic
# -------------------------------
if st.button("Generate 🚀"):

    if user_input.strip() == "":
        st.warning("Please enter details.")
    else:

        if feature == "Campaign Generation":
            prompt = f"""
            Create a marketing campaign for:
            {user_input}

            Include:
            - Target audience
            - Channels
            - Budget strategy
            - Timeline
            """

        elif feature == "Sales Pitch Creation":
            prompt = f"""
            Create a persuasive sales pitch for:
            {user_input}
            """

        elif feature == "Lead Scoring":
            prompt = f"""
            Analyze this lead information:
            {user_input}

            Provide:
            - Score out of 100
            - Reason
            - Recommended action
            """

        elif feature == "Market Analysis":
            prompt = f"""
            Provide market analysis for:
            {user_input}

            Include trends, competitors and growth opportunities.
            """

        elif feature == "Business Insights":
            prompt = f"""
            Provide strategic business insights and recommendations for:
            {user_input}
            """

        with st.spinner("Generating AI insights... 🔍"):
            result = generate_ai(prompt)

        # Styled Output Box
        st.markdown("### 📊 AI Generated Strategy")

        st.markdown(
            f"""
            <div style="
                background-color:#f4f6f7;
                padding:20px;
                border-radius:12px;
                border-left:6px solid #1f4e79;
                box-shadow:0px 5px 15px rgba(0,0,0,0.1);
            ">
                {result}
            </div>
            """,
            unsafe_allow_html=True
        )
