import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import html as _html
from datetime import datetime, timedelta

st.set_page_config(page_title="Exploração de Carteira", layout="wide")

# ============================================================
# ESTILO GLOBAL
# ============================================================
st.markdown("""<style>
.stApp {background-color:#ffffff}
[data-testid="stMainBlockContainer"] {
    background-color:#ffffff;
    padding-top:0rem;
    padding-bottom:0rem !important;
    padding-left:1.2rem;
    padding-right:1.2rem;
    max-width:100% !important;
    width:100% !important;
}
[data-testid="stHeader"] {background-color:#ffffff}
[data-testid="stSidebar"] {background-color:#ffffff}
div[data-testid="stMetric"] {text-align:center}
div[data-testid="stMetricValue"] {font-size:1.6rem; font-weight:700; color:#111111 !important}
div[data-testid="stMetricLabel"] {color:#111111 !important}

div[data-testid="stCaptionContainer"],
div[data-testid="stCaptionContainer"] p,
[data-testid="stMarkdownContainer"] small {
    color:#111111 !important;
}

div[data-testid="stSelectbox"] label p {
    font-size:0.9rem !important;
    color:#1f2b45 !important;
    font-weight:600 !important;
}
div[data-baseweb="select"] > div {
    background-color:#ffffff !important;
    border:1px solid #b9bfc7 !important;
    border-radius:2px !important;
    min-height:34px !important;
    box-shadow:none !important;
}
div[data-baseweb="select"] > div:hover {
    border-color:#8a9099 !important;
}
div[data-baseweb="select"] div[data-testid="stMarkdownContainer"],
div[data-baseweb="select"] span {
    color:#111111 !important;
}
div[data-baseweb="select"] svg {
    color:#1a1a1a !important;
    fill:#1a1a1a !important;
}
div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="popover"] div[role="listbox"],
ul[role="listbox"] {
    background-color:#ffffff !important;
    border-radius:2px !important;
}
div[data-baseweb="popover"] div[role="listbox"] {
    border:1px solid #b9bfc7 !important;
    box-shadow:0 2px 8px rgba(0,0,0,0.12) !important;
}
ul[role="listbox"] li,
div[role="listbox"] li,
li[role="option"] {
    background-color:#ffffff !important;
    color:#111111 !important;
    font-size:0.88rem !important;
}
ul[role="listbox"] li:hover,
li[role="option"]:hover,
li[role="option"][aria-selected="true"] {
    background-color:#eef2f8 !important;
    color:#111111 !important;
}
div[data-baseweb="select"] input {
    color:#111111 !important;
}
div[data-baseweb="popover"],
div[data-baseweb="popover"] *,
div[data-baseweb="menu"],
div[data-baseweb="menu"] *,
ul[role="listbox"],
div[role="listbox"] {
    scrollbar-color: #c3ccd8 #ffffff !important;
    scrollbar-width: thin !important;
}
div[data-baseweb="popover"] *::-webkit-scrollbar,
div[data-baseweb="menu"] *::-webkit-scrollbar,
ul[role="listbox"]::-webkit-scrollbar,
div[role="listbox"]::-webkit-scrollbar,
div[role="listbox"] *::-webkit-scrollbar {
    width:11px !important; height:11px !important; background:#ffffff !important;
}
div[data-baseweb="popover"] *::-webkit-scrollbar-track,
div[data-baseweb="menu"] *::-webkit-scrollbar-track,
ul[role="listbox"]::-webkit-scrollbar-track,
div[role="listbox"]::-webkit-scrollbar-track,
div[role="listbox"] *::-webkit-scrollbar-track {
    background:#ffffff !important;
}
div[data-baseweb="popover"] *::-webkit-scrollbar-thumb,
div[data-baseweb="menu"] *::-webkit-scrollbar-thumb,
ul[role="listbox"]::-webkit-scrollbar-thumb,
div[role="listbox"]::-webkit-scrollbar-thumb,
div[role="listbox"] *::-webkit-scrollbar-thumb {
    background:#c3ccd8 !important; border-radius:6px !important;
    border:2px solid #ffffff !important;
}
div[data-baseweb="popover"] *::-webkit-scrollbar-thumb:hover,
div[data-baseweb="menu"] *::-webkit-scrollbar-thumb:hover,
ul[role="listbox"]::-webkit-scrollbar-thumb:hover,
div[role="listbox"]::-webkit-scrollbar-thumb:hover,
div[role="listbox"] *::-webkit-scrollbar-thumb:hover {
    background:#aab3c0 !important;
}

.js-plotly-plot {margin:0 auto}
thead th {background:#f0f0f0 !important; color:#111111 !important}

div[data-testid="stButton"] > button {
    background:#f4f6f9 !important;
    color:#1f2b45 !important;
    border:1px solid #d7dce3 !important;
    border-radius:3px !important;
    font-size:0.8rem !important;
    font-weight:600 !important;
}
div[data-testid="stButton"] > button:hover {
    background:#e6ebf3 !important;
    border-color:#b9bfc7 !important;
    color:#132339 !important;
}

[data-testid="stDataFrame"],
[data-testid="stDataFrame"] > div,
[data-testid="stDataFrame"] canvas {
    background-color:#ffffff !important;
}
.gdg-wmyidgi, .gdg-happ90p, [data-testid="stDataFrameResizable"] {
    background-color:#ffffff !important;
    --gdg-bg-cell: #ffffff !important;
    --gdg-bg-cell-medium: #f5f7fa !important;
    --gdg-bg-header: #ffffff !important;
    --gdg-bg-header-has-focus: #eef2f8 !important;
    --gdg-bg-header-hovered: #eef2f8 !important;
    --gdg-text-dark: #111111 !important;
    --gdg-text-header: #111111 !important;
    --gdg-text-light: #333333 !important;
    --gdg-border-color: #e2e2e2 !important;
    --gdg-cell-horizontal-padding: 8px !important;
}
[data-testid="stDataFrame"] ::-webkit-scrollbar {width:11px; height:11px;}
[data-testid="stDataFrame"] ::-webkit-scrollbar-track {background:#ffffff !important;}
[data-testid="stDataFrame"] ::-webkit-scrollbar-thumb {
    background:#c3ccd8 !important; border-radius:6px; border:2px solid #ffffff;
}
[data-testid="stDataFrame"] ::-webkit-scrollbar-thumb:hover {background:#aab3c0 !important;}

@media (max-width: 640px) {
    [data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
        gap: 8px !important;
    }
    [data-testid="stHorizontalBlock"] > [data-testid="column"],
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 0 !important;
    }
    [data-testid="stMainBlockContainer"] {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    [data-testid="stMarkdownContainer"] div[style*="justify-content:space-between"] {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 14px !important;
    }
    h1 { font-size: 1.35rem !important; }
    h3 { font-size: 1.05rem !important; }
    [data-testid="stDataFrame"] { overflow-x: auto !important; }
}
</style>""", unsafe_allow_html=True)

# ============================================================
# DADOS
# ============================================================
@st.cache_data(ttl=600)
def load_contas():
    np.random.seed(42)
    n = 120
    empresas = [f"Grupo {chr(65 + i%26)} {100 + i}" for i in range(n)]
    responsaveis = ["Carlos Andrade", "Mariana Rios", "Fernanda Santos", "Ricardo Lima", "Beatriz Castro"]
    unidades = ["Matriz", "Regional Sul", "Regional SP", "Regional RJ"]
    classificacoes = ["Cliente Ativo e Recorrente", "Cliente Ativo e Sem Recorrência", "Prospecção"]
    prioridades = ["A - Prioritário", "B - Relevante", "C - Não Prioritário"]
    
    hoje = datetime.now()
    data = []
    for i in range(n):
        meses = int(np.random.choice([1, 2, 4, 7, 13, 19], p=[0.3, 0.25, 0.2, 0.1, 0.1, 0.05]))
        dt_ref = hoje - timedelta(days=meses * 30)
        
        data.append({
            "CONTA_NOME": empresas[i],
            "CLASSIFICACAO_DA_CONTA_ZOHO": np.random.choice(classificacoes, p=[0.45, 0.25, 0.3]),
            "PRIORIDADE_CONTA_NOME": np.random.choice(prioridades, p=[0.3, 0.4, 0.3]),
            "RESPONSAVEL_CONTA_NOME": np.random.choice(responsaveis),
            "UNIDADE_RESPONSAVEL": np.random.choice(unidades),
            "QTDE_MESES_SEM_INTERACAO": meses,
            "ULTIMA_REUNIAO_DATA": dt_ref if np.random.rand() > 0.3 else None,
            "ULTIMA_PROPOSTA_DATA": dt_ref if np.random.rand() > 0.4 else None,
            "ULTIMO_CONTRATO_DATA": dt_ref if np.random.rand() > 0.5 else None,
            "ULTIMO_FATURAMENTO_DATA": dt_ref if np.random.rand() > 0.2 else None,
            "ULTIMO_TIMESHEET_DATA": dt_ref if np.random.rand() > 0.3 else None,
        })
    return pd.DataFrame(data)

@st.cache_data(ttl=600)
def load_ultimas_atualizacoes():
    hoje_txt = datetime.now().strftime("%d/%m/%Y 08:00:00")
    return pd.DataFrame([
        {"FONTE_DADOS": "Senior", "DATA_HORA_EXTRACAO_MAIS_ANTIGA": hoje_txt},
        {"FONTE_DADOS": "Zoho", "DATA_HORA_EXTRACAO_MAIS_ANTIGA": hoje_txt}
    ])

def build_ultimas_atualizacoes_html():
    dfu = load_ultimas_atualizacoes()
    linhas = ""
    for _, row in dfu.iterrows():
        fonte = _html.escape(str(row["FONTE_DADOS"]))
        dt_txt = str(row["DATA_HORA_EXTRACAO_MAIS_ANTIGA"])
        linhas += (
            "<div style='display:flex; justify-content:space-between; gap:18px; "
            "padding:1px 0; font-size:0.82rem; line-height:1.5;'>"
            f"<span style='color:#e5ebf3;'>{fonte}</span>"
            f"<span style='color:#ffffff; font-variant-numeric:tabular-nums;'>{dt_txt}</span>"
            "</div>"
        )
    return (
        "<div style='background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.22); "
        "border-radius:6px; padding:14px 16px 12px 16px; min-width:230px; margin:6px 0;'>"
        "<div style='color:#ffffff; font-weight:600; font-size:0.85rem; "
        "text-align:center; margin:0 0 8px 0;'>&#9432; Últimas atualizações</div>"
        f"{linhas}"
        "</div>"
    )

# ============================================================
# CORES
# ============================================================
COR_ATIVO   = "#7cae54"
COR_RISCO   = "#e8a33d"
COR_INATIVO = "#c9424f"
AZUL_HEADER = "#1B2A4A"

# ============================================================
# ESTADO DOS FILTROS
# ============================================================
if "xfilter" not in st.session_state:
    st.session_state.xfilter = {
        "prioridade": None,
        "status": None,
        "conta": None,
        "grupo": None,
    }

def clear_xfilter():
    st.session_state.xfilter = {"prioridade": None, "status": None, "conta": None, "grupo": None}

def _styler_centralizado(df):
    sty = df.style
    sty = sty.set_properties(**{"text-align": "center"})
    sty = sty.set_table_styles(
        [{"selector": "th", "props": [("text-align", "center")]}],
        overwrite=False,
    )
    return sty

def render_tabela(df_exib, column_config, param_key, altura=560):
    st.dataframe(
        _styler_centralizado(df_exib),
        column_config=column_config,
        hide_index=True,
        use_container_width=True,
        height=altura,
        key=param_key,
    )

# ============================================================
# HEADER
# ============================================================
st.markdown(f"""
<div style="background:linear-gradient(90deg,#132339 0%,{AZUL_HEADER} 45%,#294a7d 100%);
            padding:38px 26px; border-radius:4px; margin-bottom:8px;
            display:flex; justify-content:space-between; align-items:center; gap:24px;">
    <div>
        <h1 style="color:white; margin:0; font-size:1.9rem; font-weight:700;">Exploração de Carteira</h1>
        <p style="color:#c7d0dc; margin:2px 0 0 0; font-size:0.95rem;">A, B, C e P</p>
    </div>
    {build_ultimas_atualizacoes_html()}
</div>
""", unsafe_allow_html=True)

# ============================================================
# CARREGAR E PREPARAR DADOS
# ============================================================
df = load_contas()

df["PRIORIDADE_GRUPO"] = df["PRIORIDADE_CONTA_NOME"].apply(
    lambda x: "A - Prioritário" if x == "A - Prioritário"
    else "B - Relevante" if x == "B - Relevante"
    else "C - Não Prioritário")

_dt_cols = ["ULTIMO_TIMESHEET_DATA", "ULTIMA_REUNIAO_DATA", "ULTIMA_PROPOSTA_DATA",
            "ULTIMO_CONTRATO_DATA", "ULTIMO_FATURAMENTO_DATA"]
_dt_exist = [c for c in _dt_cols if c in df.columns]
df["ULTIMA_INTERACAO_DATA"] = df[_dt_exist].apply(pd.to_datetime, errors="coerce").max(axis=1)

CLIENTES = ["Cliente Ativo e Recorrente", "Cliente Ativo e Sem Recorrência"]
PROSPECCAO = ["Prospecção"]

def classe_grupo(v):
    if v in CLIENTES:
        return "Cliente"
    if v in PROSPECCAO:
        return "Prospecção"
    return "Outro"
df["GRUPO_CLASSE"] = df["CLASSIFICACAO_DA_CONTA_ZOHO"].apply(classe_grupo)

def calc_status(row):
    m = row["QTDE_MESES_SEM_INTERACAO"] or 0
    if row["GRUPO_CLASSE"] == "Cliente":
        if m >= 18: return "Inativo"
        if m >= 12: return "Em risco"
        return "Ativo"
    else:
        if m >= 6: return "Inativo"
        if m >= 3: return "Em risco"
        return "Ativo"
df["STATUS_NIVEL"] = df.apply(calc_status, axis=1)

col_u, col_c, col_p = st.columns(3)
with col_u:
    unidades = sorted(df["UNIDADE_RESPONSAVEL"].dropna().unique().tolist())
    filtro_unidade = st.selectbox("Unidade", [None] + unidades,
                                 format_func=lambda x: "Todas" if x is None else x)
with col_c:
    contas_list = sorted(df["CONTA_NOME"].dropna().unique().tolist())
    filtro_conta = st.selectbox("Conta", [None] + contas_list,
                                format_func=lambda x: "Todas" if x is None else x)
with col_p:
    profissionais = sorted(df["RESPONSAVEL_CONTA_NOME"].dropna().unique().tolist())
    filtro_prof = st.selectbox("Profissional", [None] + profissionais,
                               format_func=lambda x: "Todos" if x is None else x)

df_f = df.copy()
if filtro_unidade: df_f = df_f[df_f["UNIDADE_RESPONSAVEL"] == filtro_unidade]
if filtro_conta:   df_f = df_f[df_f["CONTA_NOME"] == filtro_conta]
if filtro_prof:    df_f = df_f[df_f["RESPONSAVEL_CONTA_NOME"] == filtro_prof]

xf = st.session_state.xfilter
df_x = df_f.copy()
if xf["prioridade"]: df_x = df_x[df_x["PRIORIDADE_GRUPO"] == xf["prioridade"]]
if xf["status"]:     df_x = df_x[df_x["STATUS_NIVEL"] == xf["status"]]
if xf["conta"]:      df_x = df_x[df_x["CONTA_NOME"] == xf["conta"]]
if xf["grupo"]:      df_x = df_x[df_x["GRUPO_CLASSE"] == xf["grupo"]]

ativos_labels = []
if xf["grupo"]:      ativos_labels.append(f"Grupo: {xf['grupo']}")
if xf["prioridade"]: ativos_labels.append(f"Prioridade: {xf['prioridade']}")
if xf["status"]:     ativos_labels.append(f"Status: {xf['status']}")
if xf["conta"]:      ativos_labels.append(f"Conta: {xf['conta']}")
if ativos_labels:
    cflt, cbtn = st.columns([6, 1])
    with cflt:
        st.info("🔗 Filtros ativos por clique: " + "  •  ".join(ativos_labels))
    with cbtn:
        if st.button("Limpar", use_container_width=True):
            clear_xfilter()
            st.rerun()

df_cli = df_x[df_x["GRUPO_CLASSE"] == "Cliente"]
df_pro = df_x[df_x["GRUPO_CLASSE"] == "Prospecção"]

st.markdown("""
<div style="background:#ffffff; border:1px solid #e2e2e2; border-radius:6px;
            padding:12px 18px; margin-bottom:16px; font-size:0.8rem; color:#111111;
            display:flex; gap:26px; align-items:flex-start;">
  <div style="font-weight:700; min-width:70px;">Legenda:</div>
  <div style="line-height:1.7;">
    <div>✅ <b>Ativo</b></div>
    <div>⚠️ <b>Em risco</b> (<b>Contas A, B e C:</b> 12 meses sem interação &nbsp;|&nbsp; <b>Prospecção A, B e C:</b> 3 meses sem interação)</div>
    <div>❌ <b>Inativo</b> (<b>Contas A, B e C:</b> 18 meses sem interação &nbsp;|&nbsp; <b>Prospecção A, B e C:</b> 6 meses sem interação)</div>
  </div>
</div>
""", unsafe_allow_html=True)

def count_pri(dataframe):
    c = dataframe["PRIORIDADE_GRUPO"].value_counts()
    return (int(c.get("A - Prioritário", 0)),
            int(c.get("B - Relevante", 0)),
            int(c.get("C - Não Prioritário", 0)))

def status_counts(dataframe, pri):
    s = dataframe[dataframe["PRIORIDADE_GRUPO"] == pri]
    a = int((s["STATUS_NIVEL"] == "Ativo").sum())
    r = int((s["STATUS_NIVEL"] == "Em risco").sum())
    i = int((s["STATUS_NIVEL"] == "Inativo").sum())
    return a, r, i

def barra_empilhada(a, b, c, key):
    total = a + b + c
    if total == 0:
        st.write("")
        return
    fig = go.Figure()
    fig.add_bar(y=[""], x=[a], orientation="h", marker_color=COR_ATIVO,
                text=[a], textposition="inside", insidetextanchor="middle",
                customdata=["A - Prioritário"], hovertemplate="A - Prioritário: %{x}<extra></extra>")
    fig.add_bar(y=[""], x=[b], orientation="h", marker_color=COR_RISCO,
                text=[b], textposition="inside", insidetextanchor="middle",
                customdata=["B - Relevante"], hovertemplate="B - Relevante: %{x}<extra></extra>")
    fig.add_bar(y=[""], x=[c], orientation="h", marker_color=COR_INATIVO,
                text=[c], textposition="inside", insidetextanchor="middle",
                customdata=["C - Não Prioritário"], hovertemplate="C - Não Prioritário: %{x}<extra></extra>")
    fig.update_layout(
        barmode="stack", height=48, showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False, fixedrange=True),
        yaxis=dict(visible=False, fixedrange=True),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", size=11),
        dragmode=False,
    )
    ev = st.plotly_chart(fig, use_container_width=True, key=key,
                         on_select="rerun", selection_mode="points",
                         config={"displayModeBar": False, "staticPlot": False,
                                 "scrollZoom": False, "doubleClick": False})
    if ev and ev.get("selection", {}).get("points"):
        pt = ev["selection"]["points"][0]
        pri = pt.get("customdata")
        if isinstance(pri, list): pri = pri[0]
        if pri:
            st.session_state.xfilter["prioridade"] = pri
            st.rerun()

def mini_barras_status(a, r, i, labels, key, ymax=None):
    fig = go.Figure()
    fig.add_bar(
        x=labels, y=[a, r, i],
        marker_color=[COR_ATIVO, COR_RISCO, COR_INATIVO],
        text=[a, r, i], textposition="outside",
        textfont=dict(color="#111111", size=11),
        customdata=["Ativo", "Em risco", "Inativo"],
        hovertemplate="%{x}: %{y}<extra></extra>",
        width=0.55,
    )
    if ymax is None:
        ymax = max(a, r, i, 1)
    fig.update_layout(
        height=150, showlegend=False,
        margin=dict(l=0, r=0, t=18, b=0),
        yaxis=dict(visible=False, range=[0, ymax * 1.25], fixedrange=True),
        xaxis=dict(tickfont=dict(size=9, color="#111111"), showgrid=False, fixedrange=True),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(size=9, color="#111111"),
        bargap=0.35,
        dragmode=False,
    )
    ev = st.plotly_chart(fig, use_container_width=True, key=key,
                         on_select="rerun", selection_mode="points",
                         config={"displayModeBar": False, "staticPlot": False,
                                 "scrollZoom": False, "doubleClick": False})
    if ev and ev.get("selection", {}).get("points"):
        pt = ev["selection"]["points"][0]
        stt = pt.get("customdata")
        if isinstance(stt, list): stt = stt[0]
        if stt:
            st.session_state.xfilter["status"] = stt
            st.rerun()

def status_icon(nivel):
    return {"Ativo": "🟢", "Em risco": "🟡", "Inativo": "🔴"}.get(nivel, "🟢")

def status_label(nivel, is_cli=True):
    base = "Cliente" if is_cli else "Prospecção"
    txt = {"Ativo": "ativo" if is_cli else "ativa",
           "Em risco": "em risco",
           "Inativo": "inativo" if is_cli else "inativa"}.get(nivel, "ativo")
    return f"{base} {txt}"

def _ymax_global():
    vals = [1]
    for base in (df_cli, df_pro):
        for pri in ["A - Prioritário", "B - Relevante", "C - Não Prioritário"]:
            vals.extend(status_counts(base, pri))
    return max(vals)
YMAX_STATUS = _ymax_global()

a_c, b_c, c_c = count_pri(df_cli)
t_c = a_c + b_c + c_c

st.markdown(f"<h3 style='text-align:center; margin-top:14px; color:#111111;'>"
            f"Total de Contas Cliente A, B e C:&nbsp; {t_c}</h3>", unsafe_allow_html=True)

_, cbar, _ = st.columns([1, 4, 1])
with cbar:
    barra_empilhada(a_c, b_c, c_c, key="bar_cli")

m1, m2, m3 = st.columns(3)
for col, pri, tot in [(m1, "A - Prioritário", a_c), (m2, "B - Relevante", b_c), (m3, "C - Não Prioritário", c_c)]:
    with col:
        titulo = {"A - Prioritário": "Total A - Prioritário",
                  "B - Relevante": "Total B - Relevante",
                  "C - Não Prioritário": "Total C - Não Prioritário"}[pri]
        st.markdown(f"<p style='text-align:center;font-size:0.95rem;margin-bottom:0;color:#111111;'>"
                    f"{titulo}: &nbsp;<b>{tot}</b></p>", unsafe_allow_html=True)
        a, r, i = status_counts(df_cli, pri)
        mini_barras_status(a, r, i,
                           ["Cliente ativo", "Cliente em risco", "Cliente inativo"],
                           key=f"mini_cli_{pri}", ymax=YMAX_STATUS)

st.markdown("<hr style='border:none;border-top:1px solid #eee;margin:18px 0'>", unsafe_allow_html=True)

a_p, b_p, c_p = count_pri(df_pro)
t_p = a_p + b_p + c_p

st.markdown(f"<h3 style='text-align:center; margin-top:6px; color:#111111;'>"
            f"Total de Contas Prospecção A, B e C:&nbsp; {t_p}</h3>", unsafe_allow_html=True)

_, pbar, _ = st.columns([1, 4, 1])
with pbar:
    barra_empilhada(a_p, b_p, c_p, key="bar_pro")

m1, m2, m3 = st.columns(3)
for col, pri, tot in [(m1, "A - Prioritário", a_p), (m2, "B - Relevante", b_p), (m3, "C - Não Prioritário", c_p)]:
    with col:
        titulo = {"A - Prioritário": "Total A - Prioritário",
                  "B - Relevante": "Total B - Relevante",
                  "C - Não Prioritário": "Total C - Não Prioritário"}[pri]
        st.markdown(f"<p style='text-align:center;font-size:0.95rem;margin-bottom:0;color:#111111;'>"
                    f"{titulo}: &nbsp;<b>{tot}</b></p>", unsafe_allow_html=True)
        a, r, i = status_counts(df_pro, pri)
        mini_barras_status(a, r, i,
                           ["Prospecção ativa", "Prospecção em risco", "Prospecção inativa"],
                           key=f"mini_pro_{pri}", ymax=YMAX_STATUS)

st.markdown("<hr style='border:none;border-top:1px solid #eee;margin:18px 0'>", unsafe_allow_html=True)

st.markdown("<h3 style='color:#111111;'>Visão por Contas Clientes - A, B e C</h3>", unsafe_allow_html=True)
if not df_cli.empty:
    t = df_cli[["CONTA_NOME", "RESPONSAVEL_CONTA_NOME", "PRIORIDADE_GRUPO",
                "ULTIMO_FATURAMENTO_DATA", "ULTIMO_CONTRATO_DATA",
                "ULTIMO_TIMESHEET_DATA", "ULTIMA_INTERACAO_DATA",
                "QTDE_MESES_SEM_INTERACAO", "STATUS_NIVEL"]].copy()

    for c in ["ULTIMO_FATURAMENTO_DATA", "ULTIMO_CONTRATO_DATA",
              "ULTIMO_TIMESHEET_DATA", "ULTIMA_INTERACAO_DATA"]:
        t[c] = pd.to_datetime(t[c], errors="coerce")
    t["QTDE_MESES_SEM_INTERACAO"] = pd.to_numeric(t["QTDE_MESES_SEM_INTERACAO"], errors="coerce")
    t["STATUS_NIVEL"] = t["STATUS_NIVEL"].apply(lambda n: f"{status_icon(n)} {status_label(n, True)}")

    t.columns = ["Conta", "Profissional", "Prioridade", "Último faturamento",
                 "Último contrato", "Último Timesheet", "Última interação",
                 "Meses sem interação", "Status"]
    t = t.sort_values(["Prioridade", "Conta"]).reset_index(drop=True)

    cfg_cli = {
        "Conta":        st.column_config.TextColumn("Conta", width="medium"),
        "Profissional": st.column_config.TextColumn("Profissional", width="medium"),
        "Prioridade":   st.column_config.TextColumn("Prioridade", width="small"),
        "Último faturamento": st.column_config.DateColumn("Último faturamento", format="DD/MM/YYYY", width="small"),
        "Último contrato":    st.column_config.DateColumn("Último contrato", format="DD/MM/YYYY", width="small"),
        "Último Timesheet":   st.column_config.DateColumn("Último Timesheet", format="DD/MM/YYYY", width="small"),
        "Última interação":   st.column_config.DateColumn("Última interação", format="DD/MM/YYYY", width="small"),
        "Meses sem interação": st.column_config.NumberColumn("Meses sem interação", format="%d meses", width="small"),
        "Status":       st.column_config.TextColumn("Status", width="small"),
    }
    render_tabela(t, cfg_cli, param_key="tab_cli", altura=520)
else:
    st.caption("Nenhum registro para os filtros atuais.")

st.markdown("<hr style='border:none;border-top:1px solid #eee;margin:18px 0'>", unsafe_allow_html=True)

st.markdown("<h3 style='color:#111111;'>Visão por Contas Prospecção - A, B e C</h3>", unsafe_allow_html=True)
if not df_pro.empty:
    t = df_pro[["CONTA_NOME", "RESPONSAVEL_CONTA_NOME", "PRIORIDADE_GRUPO",
                "ULTIMA_PROPOSTA_DATA", "ULTIMA_REUNIAO_DATA",
                "ULTIMA_INTERACAO_DATA", "QTDE_MESES_SEM_INTERACAO",
                "STATUS_NIVEL"]].copy()

    for c in ["ULTIMA_PROPOSTA_DATA", "ULTIMA_REUNIAO_DATA", "ULTIMA_INTERACAO_DATA"]:
        t[c] = pd.to_datetime(t[c], errors="coerce")
    t["QTDE_MESES_SEM_INTERACAO"] = pd.to_numeric(t["QTDE_MESES_SEM_INTERACAO"], errors="coerce")
    t["STATUS_NIVEL"] = t["STATUS_NIVEL"].apply(lambda n: f"{status_icon(n)} {status_label(n, False)}")

    t.columns = ["Conta", "Profissional", "Prioridade", "Última proposta",
                 "Última Reunião", "Última interação", "Meses sem interação", "Status"]
    t = t.sort_values(["Prioridade", "Conta"]).reset_index(drop=True)

    cfg_pro = {
        "Conta":        st.column_config.TextColumn("Conta", width="medium"),
        "Profissional": st.column_config.TextColumn("Profissional", width="medium"),
        "Prioridade":   st.column_config.TextColumn("Prioridade", width="small"),
        "Última proposta":  st.column_config.DateColumn("Última proposta", format="DD/MM/YYYY", width="small"),
        "Última Reunião":   st.column_config.DateColumn("Última Reunião", format="DD/MM/YYYY", width="small"),
        "Última interação": st.column_config.DateColumn("Última interação", format="DD/MM/YYYY", width="small"),
        "Meses sem interação": st.column_config.NumberColumn("Meses sem interação", format="%d meses", width="small"),
        "Status":       st.column_config.TextColumn("Status", width="small"),
    }
    render_tabela(t, cfg_pro, param_key="tab_pro", altura=520)
else:
    st.caption("Nenhum registro para os filtros atuais.")
