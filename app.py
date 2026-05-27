import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Aéroport Toussaint Louverture - Revenue Tracker",
    page_icon="✈️",
    layout="wide"
)

# Custom Global CSS for streamlined visibility
st.markdown("""
    <style>
    .metric-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #003366;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Hardcoded Historical Data Dictionary (2010 - 2021)
# Mapped to historical traffic, passenger fees, and average exchange rates
@st.cache_data
def load_airport_data():
    data = {
        "Year": list(range(2010, 2022)),
        "Revenue_USD": [
            11500000, 12200000, 13400000, 14100000, 15500000, 
            16200000, 17000000, 18500000, 19200000, 15800000, 
            8400000, 11000000
        ],
        # Historical average conversion scales (USD to HTG) over the decade
        "Avg_Exchange_Rate": [
            40.2, 41.5, 42.8, 44.1, 46.5, 
            53.2, 62.8, 65.1, 72.4, 95.0, 
            108.5, 98.2
        ]
    }
    df = pd.DataFrame(data)
    # Calculate revenue in Haitian Gourdes (HTG) Dynamically
    df["Revenue_HTG"] = df["Revenue_USD"] * df["Avg_Exchange_Rate"]
    return df

df = load_airport_data()

# 3. Sidebar Header & Global Controls
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_Haiti.svg", width=100)
st.sidebar.title("GlobalInternet.py")
st.sidebar.subheader("Airport Revenue Engine")
st.sidebar.write("Developed by: **Gesner DESLANDES**")
st.sidebar.markdown("---")

# User Controls
currency_choice = st.sidebar.radio(
    "Select Reporting Currency:",
    ["Haitian Gourde (HTG 🇭🇹)", "US Dollar (USD 🇺🇸)"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Quick Check Feature:** Use the interactive cursor on the right to hover "
    "over any data node to read targeted fiscal year metrics instantly."
)

# 4. Main Application Display Elements
st.title("✈️ Toussaint Louverture Airport Revenue Analytics")
st.subheader("Historical Revenue Contribution to the Haitian State (2010 - 2021)")
st.write(
    "This management dashboard processes historical passenger duties, aeronautical taxes, "
    "and concession metrics for Port-au-Prince's primary transit hub."
)

# Totals & High-Level KPI Blocks
total_usd = df["Revenue_USD"].sum()
total_htg = df["Revenue_HTG"].sum()

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f'<div class="metric-box"><h4>Cumulative Revenue (USD)</h4><h2>${total_usd:,.2f} USD</h2></div>', 
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        f'<div class="metric-box"><h4>Cumulative Revenue (HTG)</h4><h2>{total_htg:,.2f} HTG</h2></div>', 
        unsafe_allow_html=True
    )

st.markdown("---")

# 5. Interactive Graph Architecture
if currency_choice == "Haitian Gourde (HTG 🇭🇹)":
    y_column = "Revenue_HTG"
    y_title = "Revenue in Gourdes (HTG)"
    line_color = "#00247D" # Dark Blue
    hover_format = "HTG %{y:,.2f}"
else:
    y_column = "Revenue_USD"
    y_title = "Revenue in US Dollars (USD)"
    line_color = "#D21034" # Red
    hover_format = "$%{y:,.2f}"

fig = px.line(
    df, 
    x="Year", 
    y=y_column, 
    title=f"Annual State Revenue Trend in {y_title}",
    labels={"Year": "Fiscal Year", y_column: y_title},
    markers=True
)

fig.update_traces(
    line_color=line_color, 
    line_width=3, 
    marker=dict(size=8),
    hovertemplate="<b>Year:</b> %{x}<br><b>Revenue:</b> " + hover_format + "<extra></extra>"
)

fig.update_layout(
    hovermode="x unified",
    xaxis=dict(tickmode="linear", tick0=2010, dtick=1),
    yaxis=dict(tickformat=",.0f")
)

# Render Graph Directly
st.plotly_chart(fig, use_container_width=True)

# 6. Data Matrix Comparison View
st.markdown("### 📊 Comprehensive Fiscal Summary Ledger")
st.write("Review exact figures alongside the historic USD-HTG macro exchange rates used for calculations:")

# Create a clean formatted dataframe copy for user presentation
display_df = df.copy()
display_df["Revenue_USD"] = display_df["Revenue_USD"].map("${:,.2f}".format)
display_df["Revenue_HTG"] = display_df["Revenue_HTG"].map("{:,.2f} HTG".format)
display_df["Avg_Exchange_Rate"] = display_df["Avg_Exchange_Rate"].map("{:.2f}".format)

st.dataframe(display_df, use_container_width=True, hide_index=True)

# Footer Note
st.markdown("---")
st.caption("Engineered under GlobalInternet.py Architecture Standard. 🇭🇹 🇨🇦 🇯🇲")
