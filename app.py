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
    .stRadio label, .stRadio span, .stSelectbox label {
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
    
    /* Strong White styling for the bottom right footer text */
    .footer-white-right {
        text-align: right !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 0.9rem;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Comprehensive Multilingual Dictionary Translation Layer
translations = {
    "English": {
        "sidebar_title": "Airport Fiscal Engine",
        "dev_by": "Developed by:",
        "lang_select": "Select Language:",
        "curr_select": "Select Display Currency Layer:",
        "gourde_opt": "Haitian Gourde (HTG 🇭🇹)",
        "usd_opt": "US Dollar (USD 🇺🇸)",
        "tip": "💡 **Tip:** Hover your cursor over any point on the chart profile to reveal exact yearly totals instantly.",
        "nat_focus": "National Focus",
        "nat_desc": "Financial data framework representing state revenue generation streams monitored at Toussaint Louverture Airport hub.",
        "main_title": "✈️ Toussaint Louverture Airport Revenue Tracking",
        "main_sub": "National Treasury Ingestion Overview (2010 - 2021)",
        "cum_usd": "Cumulative Revenue (USD)",
        "cum_htg": "Cumulative Revenue (HTG)",
        "graph_title": "Annual Airport Revenue Graph Generation",
        "graph_x": "Fiscal Year",
        "graph_y_usd": "Revenue in US Dollars (USD)",
        "graph_y_htg": "Revenue in Gourdes (HTG)",
        "generated": "Generated",
        "ledger_title": "📊 Comprehensive Fiscal Summary Ledger",
        "col_year": "Year",
        "col_usd": "Revenue (USD)",
        "col_rate": "Avg Exchange Rate",
        "col_htg": "Revenue (HTG)",
        "report_btn": "📥 Download Full Fiscal Report (.TXT)",
        "report_success": "Report generated successfully! Check your downloads folder."
    },
    "Français": {
        "sidebar_title": "Moteur Fiscal Aéroportuaire",
        "dev_by": "Développé par :",
        "lang_select": "Sélectionner la Langue :",
        "curr_select": "Sélectionner la Devise d'Affichage :",
        "gourde_opt": "Gourde Haïtienne (HTG 🇭🇹)",
        "usd_opt": "Dollar Américain (USD 🇺🇸)",
        "tip": "💡 **Conseil :** Passez votre curseur sur un point du graphique pour révéler instantanément les totaux annuels exacts.",
        "nat_focus": "Objectif National",
        "nat_desc": "Cadre de données financières représentant les flux de génération de revenus de l'État contrôlés à l'aéroport Toussaint Louverture.",
        "main_title": "✈️ Suivi des Revenus de l'Aéroport Toussaint Louverture",
        "main_sub": "Aperçu de l'Ingestion du Trésor National (2010 - 2021)",
        "cum_usd": "Revenu Cumulé (USD)",
        "cum_htg": "Revenu Cumulé (HTG)",
        "graph_title": "Génération du Graphique des Revenus Annuels de l'Aéroport",
        "graph_x": "Année Fiscale",
        "graph_y_usd": "Revenus en Dollars US (USD)",
        "graph_y_htg": "Revenus en Gourdes (HTG)",
        "generated": "Généré",
        "ledger_title": "📊 Grand Livre Récapitulatif Fiscal Complet",
        "col_year": "Année",
        "col_usd": "Revenu (USD)",
        "col_rate": "Taux de Change Moyen",
        "col_htg": "Revenu (HTG)",
        "report_btn": "📥 Télécharger le Rapport Fiscal Complet (.TXT)",
        "report_success": "Rapport généré avec succès ! Vérifiez votre dossier de téléchargement."
    },
    "Kreyòl Ayisyen": {
        "sidebar_title": "Motè Fiskal Ayewopò",
        "dev_by": "Devlope pa:",
        "lang_select": "Chwazi Lang:",
        "curr_select": "Chwazi Lajan pou Montre a:",
        "gourde_opt": "Goud Ayisyen (HTG 🇭🇹)",
        "usd_opt": "Dola Ameriken (USD 🇺🇸)",
        "tip": "💡 **Konsèy:** Pase kòrsè a sou nenpòt pwen nan grafik la pou wè kantite lajan egzak pou chak ane imedyatman.",
        "nat_focus": "Fokus Nasyonal",
        "nat_desc": "Kadr done finansye ki montre lajan Leta Ayisyen fè nan ayewopò Entènasyonal Toussaint Louverture.",
        "main_title": "✈️ Swiv Revni Ayewopò Toussaint Louverture",
        "main_sub": "Apèsi sou Lajan ki Antre nan Trezò Piblik (2010 - 2021)",
        "cum_usd": "Tout Revni Ansanm (USD)",
        "cum_htg": "Tout Revni Ansanm (HTG)",
        "graph_title": "Grafik Kwasans Revni Ayewopò a pa Ane",
        "graph_x": "Ane Fiskal",
        "graph_y_usd": "Revni an Dola Ameriken (USD)",
        "graph_y_htg": "Revni an Goud (HTG)",
        "generated": "Lajan Fèt",
        "ledger_title": "📊 Kanè Rezime Fiskal Konplè",
        "col_year": "Ane",
        "col_usd": "Revni (USD)",
        "col_rate": "Taux de Chanj Mwayen",
        "col_htg": "Revni (HTG)",
        "report_btn": "📥 Telechaje Rapò Fiskal Konplè a (.TXT)",
        "report_success": "Rapò a fèt byen! Tcheke dosye telechajman ou."
    }
}

# 4. Data Matrix Load Engine (2010 - 2021)
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

# 5. Sidebar Setup & Language Matrix Mapping
st.sidebar.markdown("## 🌐 GlobalInternet.py")

# Language Selector Setup
selected_lang = st.sidebar.selectbox(
    "Select Language / Chwazi Lang / Sélectionner Langue",
    ["English", "Français", "Kreyòl Ayisyen"]
)

# Lock active translation library context
ln = translations[selected_lang]

st.sidebar.markdown(f"### {ln['sidebar_title']}")
st.sidebar.markdown(f"{ln['dev_by']} **Gesner DESLANDES**")
st.sidebar.markdown("---")

# Currency Toggle Engine mapped dynamically to selections
currency_choice = st.sidebar.radio(
    ln["curr_select"],
    [ln["gourde_opt"], ln["usd_opt"]]
)

st.sidebar.markdown("---")
st.sidebar.markdown(ln["tip"])

# 6. Core Interface Split: Left Section (National Symbol) & Right Workspace
col_left, col_right = st.columns([1, 3.2])

with col_left:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader(ln["nat_focus"])
    
    # Active stable online flag reference from verified Wikimedia asset tree
    haitian_flag_url = "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Haiti.svg"
    st.image(haitian_flag_url, caption="République d'Haïti", width='stretch')
    
    st.markdown(
        f"<p style='font-size: 0.85rem; color: #cbd5e1 !important; margin-top: 10px;'>"
        f"{ln['nat_desc']}</p>",
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.title(ln["main_title"])
    st.markdown(f"### {ln['main_sub']}")
    
    # Mathematical Cumulative Calculation Aggregation
    total_usd = df["Revenue_USD"].sum()
    total_htg = df["Revenue_HTG"].sum()
    
    # Render Interactive Metrics Blocks
    kpi1, kpi2 = st.columns(2)
    with kpi1:
        st.markdown(
            f'<div class="metric-box"><h4>{ln["cum_usd"]}</h4><h2>${total_usd:,.2f} USD</h2></div>', 
            unsafe_allow_html=True
        )
    with kpi2:
        st.markdown(
            f'<div class="metric-box"><h4>{ln["cum_htg"]}</h4><h2>{total_htg:,.2f} HTG</h2></div>', 
            unsafe_allow_html=True
        )
        
    st.markdown("---")
    
    # Set context colors and selection mappings base on translated string comparisons
    if currency_choice == ln["gourde_opt"]:
        y_column = "Revenue_HTG"
        y_title = ln["graph_y_htg"]
        line_color = "#38bdf8"  # High contrast bright cyan
        hover_format = "HTG %{y:,.2f}"
    else:
        y_column = "Revenue_USD"
        y_title = ln["graph_y_usd"]
        line_color = "#f43f5e"  # High contrast vivid coral pink
        hover_format = "$%{y:,.2f}"
        
    # Generate Interactive Plotly Line Framework
    fig = px.line(
        df, 
        x="Year", 
        y=y_column, 
        title=f"{ln['graph_title']} ({y_title})",
        labels={"Year": ln["graph_x"], y_column: y_title},
        markers=True
    )
    
    fig.update_traces(
        line_color=line_color, 
        line_width=4, 
        marker=dict(size=10, color="#ffffff", line=dict(color=line_color, width=2)),
        hovertemplate="<b>" + ln["graph_x"] + ":</b> %{x}<br><b>" + ln["generated"] + ":</b> " + hover_format + "<extra></extra>"
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
    st.markdown(f"### {ln['ledger_title']}")
    
    display_df = df.copy()
    
    # Dynamic Renaming of Columns for the interactive UI matrix view
    display_df.columns = [ln["col_year"], ln["col_usd"], ln["col_rate"], ln["col_htg"]]
    
    # Formatted mapping views
    display_df[ln["col_usd"]] = display_df[ln["col_usd"]].map("${:,.2f}".format)
    display_df[ln["col_htg"]] = display_df[ln["col_htg"]].map("{:,.2f} HTG".format)
    display_df[ln["col_rate"]] = display_df[ln["col_rate"]].map("{:.2f}".format)
    
    st.dataframe(display_df, width='stretch', hide_index=True)

    st.markdown("---")
    
    # 7. Dynamic Data Engine Report Compiler Execution Block
    report_string = f"=== TOUSSAINT LOUVERTURE AIRPORT FISCAL REPORT ({selected_lang.upper()}) ===\n"
    report_string += f"System Generated Archive under GlobalInternet.py Architecture Core\n"
    report_string += f"Developer Lead: Gesner DESLANDES\n"
    report_string += f"--------------------------------------------------\n"
    report_string += f"TOTAL CUMULATIVE VOLUME USD: ${total_usd:,.2f} USD\n"
    report_string += f"TOTAL CUMULATIVE VOLUME HTG: {total_htg:,.2f} HTG\n"
    report_string += f"--------------------------------------------------\n\n"
    report_string += f"YEAR | REVENUE (USD) | EXCHANGE RATE | REVENUE (HTG)\n"
    
    for idx, row in df.iterrows():
        report_string += f"{int(row['Year'])} | ${row['Revenue_USD']:,.2f} | {row['Avg_Exchange_Rate']:.2f} | {row['Revenue_HTG']:,.2f} HTG\n"
        
    report_string += f"\n=== END OF REPORT - SECURITY VERIFIED ARCHIVE ==="

    # Interactive Downloader Button Element
    st.download_button(
        label=ln["report_btn"],
        data=report_string,
        file_name=f"toussaint_louverture_airport_report_{selected_lang.lower().replace(' ', '_')}.txt",
        mime="text/plain"
    )

# 8. Global Platform Footer (Strong white alignment lock, pushed to the right side)
st.markdown(
    """
    <div class="footer-white-right">
        © 2026 GLOBALINTERNET.PY | Global Software Architectures & Technology Innovation.
    </div>
    """,
    unsafe_allow_html=True
)
