import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Nova Resource Labs", page_icon="🛰️", layout="wide")

# --- CSS: THE "ASTROFORGE" UPGRADE ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    
    /* Glass Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    
    /* Neon Text */
    .neon-text {
        color: #00d4ff;
        text-shadow: 0 0 10px #00d4ff;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Ticker Animation */
    @keyframes scroll {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    .ticker {
        white-space: nowrap;
        overflow: hidden;
        background: #111;
        padding: 10px 0;
        border-top: 1px solid #333;
        border-bottom: 1px solid #333;
        color: #00ff00;
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOP TICKER ---
st.markdown("""<div class="ticker">
    IRIDIUM: $5,120.00 (+2.4%) | PLATINUM: $1,085.50 (+0.8%) | OSMIUM: $400.00 (+0.1%) | NOVA STATUS: ORBITAL LOCK CONFIRMED
    </div>""", unsafe_allow_html=True)

# --- HEADER ---
st.title("NOVA RESOURCE LABS")
st.write("### Oputa Orbital Systems & Mineral Intelligence")

# --- THE LIVE STAR MAP ---
st.write("#### Live Celestial Tracking (Sector 0-14)")
# This embeds a live interactive star map
st.components.v1.iframe("https://slowe.github.io/VirtualSky/embed?longitude=3.3792&latitude=6.5244&projection=gnomic&constellations=true&constellationlabels=true&showstarlabels=true&live=true", height=500)

# --- MISSION TILES ---
st.write("---")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="glass-card"><h2 class="neon-text">$1.2B</h2><p>Projected Bounty</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="glass-card"><h2 class="neon-text">18%</h2><p>Iridium Concentration</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="glass-card"><h2 class="neon-text">Apr 14</h2><p>2026 Perigee Window</p></div>', unsafe_allow_html=True)

# --- THE OPUTA LEGACY (Bios) ---
st.header("Strategic Leadership")
ba, bb = st.columns(2)
with ba:
    st.subheader("Daniel Oputa")
    st.caption("Lead Architect")
    st.write("Proprietary Orion Intelligence Layer development and spectroscopic logic.")
with bb:
    st.subheader("Emmanuel Oputa")
    st.caption("Chief of Operations")
    st.write("Orbital logistics, telemetry integrity, and secure data-rights acquisition.")

# --- FOOTER ---
st.button("ENCRYPTED INQUIRY / MNDA REQUEST")
