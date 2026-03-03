import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Nova Resource Labs", page_icon="🛰️", layout="wide")

# --- HIGH-TECH CSS INJECTION ---
st.markdown("""
    <style>
    /* Deep Space Background */
    .stApp {
        background: radial-gradient(circle at top right, #1a1a2e, #0f0f1a, #000000);
        color: #e0e0e0;
    }
    
    /* Glassmorphism Containers */
    div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }

    /* Professional Headers */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        letter-spacing: -1px;
        text-transform: uppercase;
        color: #00d4ff !important;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #ffffff;
        font-weight: 800;
    }
    
    /* Custom Button */
    .stButton>button {
        width: 100%;
        background-color: transparent;
        color: #00d4ff;
        border: 2px solid #00d4ff;
        transition: 0.3s;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00d4ff;
        color: black;
        box-shadow: 0 0 20px #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: MISSION LOG ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/00d4ff/satellite.png")
    st.title("NOVA OPS")
    st.status("Orion Sync: ACTIVE", state="complete")
    st.write("---")
    st.caption("Current Window: April 2026")
    st.caption("Asset: 2013 GM3")

# --- MAIN PAGE ---
st.title("Nova Resource Labs")
st.write("### Architecting the Next Frontier of Mineral Intelligence.")

# --- MISSION DATA TILES ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Valuation", "$1.2 Billion", "+12% Market")
with col2:
    st.metric("Purity", "18% Iridium", "Grade: Tier-1")
with col3:
    st.metric("Distance", "8,620 KM", "Perigee Locked")

# --- THE TEAM (The Oputa Brothers) ---
st.write("---")
st.header("The Intelligence Core")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Daniel Oputa")
    st.caption("Lead Architect")
    st.write("Creator of the Orion Intelligence Layer. Daniel directs the lab's spectroscopic research and valuation logic.")

with col_b:
    st.subheader("Emmanuel Oputa")
    st.caption("Chief of Operations")
    st.write("Lead of orbital logistics and trajectory integrity. Emmanuel oversees the operational security of all mission-critical data.")

# --- CONTACT CTA ---
st.write("---")
st.button("REQUEST SECURE DATA ACCESS (MNDA REQUIRED)")
