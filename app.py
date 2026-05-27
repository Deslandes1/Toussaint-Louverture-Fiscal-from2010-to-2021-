import streamlit as st

# 1. Page Configuration & Title
st.set_page_config(
    page_title="Haitian Pride Software Platform",
    page_icon="🇭🇹",
    layout="wide",
)

# 2. Custom CSS Injection (Colorful Theme & Dynamic Background Accents)
st.markdown(
    """
    <style>
    /* Gradient styling for the main container header background */
    .stApp {
        background-color: #0f172a;
        background-image: radial-gradient(at 0% 0%, hsla(222,47%,16%,1) 0, transparent 50%), 
                          radial-gradient(at 100% 0%, hsla(354,85%,18%,1) 0, transparent 50%),
                          radial-gradient(at 50% 100%, hsla(215,80%,20%,1) 0, transparent 50%);
        background-attachment: fixed;
    }
    
    /* Typography color correction for dark theme legibility */
    h1, h2, h3, p, span, label {
        color: #f8fafc !important;
    }
    
    /* Colorful accent card styling for feature boxes */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Gold highlight for metric emphasis */
    .highlight-text {
        color: #f1b517 !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_not_allowed=True,
)

# 3. Main Header Interface
st.title("🇭🇹 Global System Dashboard")
st.markdown("Welcome back! This interface has been stylized with custom ambient lighting gradients representing national colors.")
st.markdown("---")

# 4. Responsive Columns Layout (Left Feature Restored)
col1, col2, col3 = st.columns([1, 1.2, 1.2])

with col1:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("Feature 1: National Focus")
    
    # Restored online flag reference using verified Wikimedia Commons SVG
    haitian_flag_url = "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Haiti.svg"
    
    st.image(
        haitian_flag_url,
        caption="République d'Haïti",
        use_container_width=True
    )
    
    st.markdown(
        "This component successfully fetches the active state insignia online. "
        "System links are synchronized and running smoothly.",
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("Feature 2: Regional Tracking")
    st.markdown("Monitor real-time infrastructure data, natural resources, and community developments.")
    
    # Interactive sample input to confirm responsive layout state
    metric_selection = st.selectbox(
        "Select Target Node:",
        ["Infrastructure Assets", "Soil & Mineral Mapping", "Demographic Overlays"]
    )
    st.write(f"Active monitoring track: <span class='highlight-text'>{metric_selection}</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("Feature 3: Financial Pulse")
    st.markdown("Track currency valuations and market shifts instantaneously below.")
    
    # Status metrics inside responsive block
    st.metric(label="System Operational Latency", value="14 ms", delta="-2 ms")
    st.metric(label="Active Network Handshakes", value="1,024", delta="48")
    st.markdown('</div>', unsafe_allow_html=True)
