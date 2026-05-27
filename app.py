import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Title
st.set_page_config(
    page_title="Toussaint Louverture Airport Revenue Analytics",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Injection (Synchronized Sidebar and Main Page Gradients)
st.markdown(
    """
    <style>
    /* Gradient styling for the global background canvas and the sidebar */
    .stApp, div[data-testid="stSidebar"] {
        background-color: #0f172a !important;
        background-image: radial-gradient(at 0% 0%, hsla(222,47%,16%,1) 0, transparent 50%), 
                          radial-gradient(at 100% 0%, hsla(354,85%,18%,1) 0, transparent 50%),
                          radial-gradient(at 50% 100%, hsla(215,80%,20%,1) 0, transparent 50%) !important;
        background-attachment: fixed !important;
    }
    
    /* Remove default Streamlit border line on the sidebar for a seamless look */
    div[data-testid="stSidebar"] {
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Strict high-contrast text color overrides for absolute visibility */
    h1, h2, h3, h4, p, span, label, div[data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
    }
    
    /* Semi-transparent blur effect cards for metrics and features */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    .metric-box {
        background: rgba(15, 23, 42, 0.6);
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #f1b517;
        margin-bottom: 15px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .highlight-text {
        color: #f1b517 !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Hardcoded Historical Data Dictionary (2010 - 2021)
@st.cache_data
def load_airport_data():
    data = {
        "Year": list(range(2010, 2022)),
        "Revenue_USD": [
            11500000, 12200000, 13400000, 14100000, 15500000, 
            16200000, 17000000, 18500000, 19200000, 15800000, 
            8400000, 11000000
        ],
        "Avg_Exchange_Rate": [
            40.2, 41.5, 42.8, 44.1, 46.5, 
            53.2, 62.8, 65.1, 72.4, 95.0, 
            108.5, 98.2
        ]
    }
    df = pd.DataFrame(data)
    df["Revenue_HTG"] = df["Revenue_USD"] * df["Avg_Exchange_Rate"]
    return df

df = load_airport_data()

# 4. Sidebar Branding Controls (Now completely readable with Dark Background)
st.sidebar.markdown("## 🌐 GlobalInternet.py")
st.sidebar.markdown("### Airport Fiscal Engine")
st.sidebar.markdown("Developed by: **Gesner DESLANDES**")
st.sidebar.markdown("---")

# User Interactive State Controls
currency_choice = st.sidebar.radio(
    "Select Display Currency Layer:",
    ["Haitian Gourde (HTG 🇭🇹)", "US Dollar (USD 🇺🇸)"]
)

st.sidebar.markdown("---")
st.sidebar.caption("💡 **Tip:** Hover your cursor over any point on the chart profile to reveal exact yearly totals instantly.")

# 5. Layout Setup: Left National Feature & Main Workspace Splitting
col_left, col_right = st.columns([1, 3.2])

with col_left:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("National Focus")
    
    # Online asset mirroring using verified stable Wikimedia Commons server
    haitian_flag_url = "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Haiti.svg"
    st.image(haitian_flag_url, caption="République d'Haïti", use_container_width=True)
    
    st.markdown(
        "<p style='font-size: 0.85rem; color: #cbd5e1 !important;'>"
        "Financial data framework representing state revenue generation streams monitored at "
        "Toussaint Louverture Airport hub.</p>",
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.title("✈️ Toussaint Louverture Airport Revenue Tracking")
    st.markdown("### National Treasury Ingestion Overview (2010 - 2021)")
    
    # Calculate totals
    total_usd = df["Revenue_USD"].sum()
    total_htg = df["Revenue_HTG"].sum()
    
    # Render High-Contrast KPI Cards
    kpi1, kpi2 = st.columns(2)
    with kpi1:
        st.markdown(
            f'<div class="metric-box"><h4>Cumulative Revenue (USD)</h4><h2>${total_usd:,.2f} USD</h2></div>', 
            unsafe_allow_html=True
        )
    with kpi2:
        st.markdown(
            f'<div class="metric-box"><h4>Cumulative Revenue (HTG)</h4><h2>{total_htg:,.2f} HTG</h2></div>', 
            unsafe_allow_html=True
        )
        
    st.markdown("---")
    
    # Determine chart configuration based on sidebar choice
    if currency_choice == "Haitian Gourde (HTG 🇭🇹)":
        y_column = "Revenue_HTG"
        y_title = "Revenue in Gourdes (HTG)"
        line_color = "#38bdf8"  # Beautiful bright cyan accent
        hover_format = "HTG %{y:,.2f}"
    else:
        y_column = "Revenue_USD"
        y_title = "Revenue in US Dollars (USD)"
        line_color = "#f43f5e"  # Vivid coral pink accent
        hover_format = "$%{y:,.2f}"
        
    # Generate Interactive Graph Line
    fig = px.line(
        df, 
        x="Year", 
        y=y_column, 
        title=f"Annual Airport Revenue Graph Generation ({y_title})",
        labels={"Year": "Fiscal Year", y_column: y_title},
        markers=True
    )
    
    fig.update_traces(
        line_color=line_color, 
        line_width=4, 
        marker=dict(size=10, color="#ffffff", line=dict(color=line_color, width=2)),
        hovertemplate="<b>Year:</b> %{x}<br><b>Generated:</b> " + hover_format + "<extra></extra>"
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified",
        xaxis=dict(tickmode="linear", tick0=2010, dtick=1, gridcolor="rgba(255,255,255,0.1)"),
        yaxis=dict(tickformat=",.0f", gridcolor="rgba(255,255,255,0.1)"),
        title_font_color="#ffffff"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Structural Summary Matrix Ledger Dataframe Display
    st.markdown("### 📊 Comprehensive Fiscal Summary Ledger")
    
    display_df = df.copy()
    display_df["Revenue_USD"] = display_df["Revenue_USD"].map("${:,.2f}".format)
    display_df["Revenue_HTG"] = display_df["Revenue_HTG"].map("{:,.2f} HTG".format)
    display_df["Avg_Exchange_Rate"] = display_df["Avg_Exchange_Rate"].map("{:.2f}".format)
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)

# 6. Global Platform Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); color: #94a3b8 !important; font-size: 0.85rem;">
        © 2026 GLOBALINTERNET.PY | Global Software Architectures & Technology Innovation.
    </div>
    """,
    unsafe_allow_html=True
)
