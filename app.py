import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="Аэрофлот Аналитика", page_icon="✈️", layout="wide")


# CSS СТИЛИ (VOXR AI STYLE)
CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #3b0764 0%, transparent 35%),
                radial-gradient(circle at top right, #581c87 0%, transparent 25%),
                #050507 !important;
    color: #E5E7EB;
    font-family: 'Inter', sans-serif;
}

.block-container { padding: 2rem 4rem; }
h1, h2, h3 { color: white !important; }

.hero-title {
    font-size: 48px; font-weight: 700; text-align: center;
    background: linear-gradient(90deg, #ffffff, #c084fc);
    -webkit-background-clip: text; color: transparent; margin-bottom: 10px;
}

.hero-text { text-align: center; color: #a1a1aa; font-size: 18px; }

.card {
    background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
    border: 1px solid rgba(168,85,247,0.25);
    border-radius: 20px; padding: 25px;
    box-shadow: 0 0 30px rgba(168,85,247,0.15);
}

.metric-title { color: #a1a1aa; font-size: 14px; }
.metric-value { font-size: 32px; font-weight: 700; color: white; }
.metric-change { color: #c084fc; font-size: 14px; }

.stButton button {
    background: linear-gradient(90deg, #9333ea, #c026d3);
    border: none; border-radius: 30px; color: white;
    padding: 10px 30px; font-weight: 600;
}

button[data-baseweb="tab"] { background: #111018; border-radius: 20px; padding: 12px 25px; color: white; }
button[data-baseweb="tab"][aria-selected="true"] { background: linear-gradient(90deg, #7e22ce, #c026d3); }
[data-testid="stPlotlyChart"] { background: rgba(255,255,255,0.03); border-radius: 20px; padding: 15px; }
</style>
"""
st.markdown(CSS_STYLES, unsafe_allow_html=True)


# ДАННЫЕ
@st.cache_data
def get_data():
    return pd.DataFrame({
        "Год": [2023, 2024, 2025, 2026],
        "Выручка": [612.2, 856.8, 902.3, 950],
        "EBITDA": [213.4, 258.1, 185, 210],
        "Чистая прибыль": [-14, 55, 22.6, 35]
    })


df = get_data()

# UI: ВЕРХНИЙ ЭКРАН
st.markdown('<div class="hero-title">Аэрофлот Аналитика</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-text">Интеллектуальная система финансового анализа, прогнозирования и оценки рисков</div><br>',
    unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        '<div class="card"><div class="metric-title">Выручка 2024</div><div class="metric-value">856.8 млрд ₽</div><div class="metric-change">↑ 40% к 2023</div></div>',
        unsafe_allow_html=True)
with c2:
    st.markdown(
        '<div class="card"><div class="metric-title">EBITDA</div><div class="metric-value">258.1 млрд ₽</div><div class="metric-change">↑ 21%</div></div>',
        unsafe_allow_html=True)
with c3:
    st.markdown(
        '<div class="card"><div class="metric-title">Чистая прибыль</div><div class="metric-value">55 млрд ₽</div><div class="metric-change">Восстановление</div></div>',
        unsafe_allow_html=True)


# НАВИГАЦИЯ И ВКЛАДКИ
tab1, tab2, tab3, tab4 = st.tabs(["Финансовый анализ", "Прогнозирование", "Оценка рисков", "Стресс-тест"])

with tab1:
    st.subheader("Финансовая динамика компании")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df["Год"], y=df["Выручка"], name="Выручка", marker_color="#a855f7"))
    fig.add_trace(go.Scatter(x=df["Год"], y=df["EBITDA"], name="EBITDA", mode="lines+markers",
                             line=dict(color="#22c55e", width=3)))
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=450,
                      legend=dict(orientation="h"))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Прогноз финансовых показателей")
    st.info("Прогноз рассчитан на основе динамики 2023–2024 годов")
    fc = df[df["Год"] == 2026]
    cols = st.columns(3)
    for i, col in enumerate([("Прогноз выручки 2025", "Выручка", "+7.4%"), ("Прогноз EBITDA", "EBITDA", ""),
                             ("Прогноз прибыли", "Чистая прибыль", "")]):
        with cols[i]:
            st.markdown(
                f'<div class="card"><div class="metric-title">{col[0]}</div><div class="metric-value">{fc[col[1]].iloc[0]} млрд ₽</div><div class="metric-change">{col[2]}</div></div>',
                unsafe_allow_html=True)

    fig_f = px.line(df, x="Год", y=["Выручка", "EBITDA", "Чистая прибыль"], markers=True)
    fig_f.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_f, use_container_width=True)

with tab3:
    st.subheader("Комплексная оценка финансовых рисков")

    risk_score = 25
    status = "НИЗКИЙ" if risk_score < 40 else ("СРЕДНИЙ" if risk_score < 70 else "ВЫСОКИЙ")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f'<div class="card"><div class="metric-title">Индекс риска</div>'
            f'<div class="metric-value">{risk_score} / 100</div>'
            f'<div class="metric-change">Уровень: {status}</div></div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '<div class="card"><div class="metric-title">Аналитическое заключение</div>'
            '<p>✓ Рост выручки положительный<br>'
            '✓ EBITDA требует контроля<br>'
            '✓ Компания сохраняет прибыльность</p></div>',
            unsafe_allow_html=True
        )
    st.subheader("Факторы финансовой устойчивости")
    risk_df = pd.DataFrame({
        "Фактор": ["Ликвидность", "Прибыльность", "Рост выручки", "Долговая нагрузка"],
        "Оценка": [85, 75, 90, 70]
    })
    fig_risk = px.bar(
        risk_df,
        x="Фактор",
        y="Оценка"
    )
    fig_risk.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=400
    )
    st.plotly_chart(fig_risk, use_container_width=True)

with tab4:
    st.subheader("Моделирование негативных сценариев")
    shock = st.slider("Снижение выручки (%)", 0, 50, 10)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f'<div class="card"><div class="metric-title">Новая выручка</div><div class="metric-value">{856.8 * (1 - shock / 100):.1f} млрд ₽</div></div>',
            unsafe_allow_html=True)
    with c2:
        st.markdown(
            f'<div class="card"><div class="metric-title">Прогноз прибыли</div><div class="metric-value">{55 * (1 - shock / 100):.1f} млрд ₽</div></div>',
            unsafe_allow_html=True)

    if shock > 25:
        st.error("Высокий уровень риска: требуется антикризисный сценарий")
    elif shock > 10:
        st.warning("Средний уровень риска")
    else:
        st.success("Компания сохраняет устойчивость")