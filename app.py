import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Toussaint Louverture Airport Revenue Analytics",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Strict CSS Injection: Forcing Uniform Background & Eliminating White Sidebar Elements
st.markdown(
    """
    <style>
    /* Force identical background canvas on both the Main App and the Sidebar containers */
    .stApp, 
    [data-testid="stSidebar"], 
    section[data-testid="stSidebar"], 
    div[data-testid="stSidebarUserContent"],
    [data-testid="stSidebarUserContent"] > div {
        background-color: #0f172a !important;
        background-image: radial-gradient(at 0% 0%, hsla(222,47%,16%,1) 0, transparent 50%), 
                          radial-gradient(at 100% 0%, hsla(354,85%,18%,1) 0, transparent 50%),
                          radial-gradient(at 50% 100%, hsla(215,80%,20%,1) 0, transparent 50%) !important;
        background-attachment: fixed !important;
    }
    
    /* Subtle vertical boundary divider replacing default harsh borders */
    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Global text contrast enforcement across fields, labels, and widget choices */
    h1, h2, h3, h4, p, span, label, li, 
    div[data-testid="stWidgetLabel"] p, 
    div[data-testid="stMarkdownContainer"] p,
    .stRadio label, .stRadio span {
        color: #ffffff !important;
    }
    
    /* Card structural layout for specific component emphasis */
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

# 3. Data Matrix Load Engine (2010 - 2021)
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

# 4. Sidebar Branding Module (Fully readable text on dark background layer)
st.sidebar.markdown("## 🌐 GlobalInternet.py")
st.sidebar.markdown("### Airport Fiscal Engine")
st.sidebar.markdown("Developed by: **Gesner DESLANDES**")
st.sidebar.markdown("---")

# User Interactive Layer Toggle
currency_choice = st.sidebar.radio(
    "Select Display Currency Layer:",
    ["Haitian Gourde (HTG 🇭🇹)", "US Dollar (USD 🇺🇸)"]
)

st.sidebar.markdown("---")
st.sidebar.caption("💡 **Tip:** Hover your cursor over any point on the chart profile to reveal exact yearly totals instantly.")

# 5. Core Interface Split: Left Section (National Symbol) & Right Workspace
col_left, col_right = st.columns([1, 3.2])

with col_left:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("National Focus")
    
    # Active stable online flag reference from verified Wikimedia asset tree
    haitian_flag_url = "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Haiti.svg"
    st.image(haitian_flag_url, caption="République d'Haïti", width='stretch')
    
    st.markdown(
        "<p style='font-size: 0.85rem; color: #cbd5e1 !important; margin-top: 10px;'>"
        "Financial data framework representing state revenue generation streams monitored at "
        "Toussaint Louverture Airport hub.</p>",
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.title("✈️ Toussaint Louverture Airport Revenue Tracking")
    st.markdown("### National Treasury Ingestion Overview (2010 - 2021)")
    
    # Mathematical Cumulative Calculation Aggregation
    total_usd = df["Revenue_USD"].sum()
    total_htg = df["Revenue_HTG"].sum()
    
    # Render Interactive Metrics Blocks
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
    
    # Set context color scales based on layout selections
    if currency_choice == "Haitian Gourde (HTG 🇭🇹)":
        y_column = "Revenue_HTG"
        y_title = "Revenue in Gourdes (HTG)"
        line_color = "#38bdf8"  # High contrast bright cyan
        hover_format = "HTG %{y:,.2f}"
    else:
        y_column = "Revenue_USD"
        y_title = "Revenue in US Dollars (USD)"
        line_color = "#f43f5e"  # High contrast vivid coral pink
        hover_format = "$%{y:,.2f}"
        
    # Generate Interactive Plotly Line Framework
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
        xaxis=dict(tickmode="linear", tick0=2010, dtick=1, gridcolor="rgba(255,255,255,0.1)", title_font=dict(color="#ffffff"), tickfont=dict(color="#ffffff")),
        yaxis=dict(tickformat=",.0f", gridcolor="rgba(255,255,255,0.1)", title_font=dict(color="#ffffff"), tickfont=dict(color="#ffffff")),
        title_font_color="#ffffff"
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Structural Ledger Summary Dataframe Viewport
    st.markdown("### 📊 Comprehensive Fiscal Summary Ledger")
    
    display_df = df.copy()
    display_df["Revenue_USD"] = display_df["Revenue_USD"].map("${:,.2f}".format)
    display_df["Revenue_HTG"] = display_df["Revenue_HTG"].map("{:,.2f} HTG".format)
    display_df["Avg_Exchange_Rate"] = display_df["Avg_Exchange_Rate"].map("{:.2f}".format)
    
    st.dataframe(display_df, width='stretch', hide_index=True)

# 6. Global Platform Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); color: #94a3b8 !important; font-size: 0.85rem;">
        © 2026 GLOBALINTERNET.PY | Global Software Architectures & Technology Innovation.
    </div>
    """,
    unsafe_allow_html=True
)
