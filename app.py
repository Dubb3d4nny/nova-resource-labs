import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Nova Resource Labs", page_icon="🛰️", layout="wide")

# --- CUSTOM THEME (AstroForge Style) ---
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    div.stButton > button:first-child {
        background-color: #0078D4; color: white; border-radius: 5px;
    }
    .stMarkdown h1 { color: #E0E0E0; font-family: 'Inter', sans-serif; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("NOVA RESOURCE LABS")
    st.subheader("Architecting the Next Frontier of Mineral Intelligence.")
    st.write("Specializing in high-fidelity spectroscopic tracking and orbital resource valuation.")

# --- MISSION STATUS (The Countdown) ---
st.divider()
target_date = datetime.datetime(2026, 4, 14, 12, 0)
time_left = target_date - datetime.datetime.now()

st.metric(label="TIME TO PERIGEE (2013 GM3)", value=f"{time_left.days} Days", delta="-1.2% Orbital Decay")

# --- ABOUT US / THE CORE TEAM ---
st.header("The Intelligence Core")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### Daniel [Your Last Name]")
    st.caption("Lead Architect & Orbital Strategist")
    st.write("Pioneering localized deep-space tracking systems. Daniel leads the development of the Orion Interface, bridging the gap between raw spectral data and trillion-dollar asset valuation.")

with col_b:
    st.markdown("### Emmanuel [Last Name]")
    st.caption("Chief of Orbital Operations")
    st.write("Expert in orbital logistics and mission-critical data integrity. Emmanuel ensures the precision of Nova's trajectory modeling and international telemetry sync.")

# --- FOOTER ---
st.divider()
st.info("📩 Inquiries for Secure Data Access (MNDA required) available via DMs.")
