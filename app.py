import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ==============================
# НАСТРОЙКА СТРАНИЦЫ
# ==============================

st.set_page_config(
    page_title="Аэрофлот Аналитика",
    page_icon="✈️",
    layout="wide"
)


# ==============================
# СТИЛИ VOXR AI STYLE
# ==============================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');


html, body, [data-testid="stAppViewContainer"] {
    background:
    radial-gradient(circle at top left, #3b0764 0%, transparent 35%),
    radial-gradient(circle at top right, #581c87 0%, transparent 25%),
    #050507 !important;

    color: #E5E7EB;
    font-family: 'Inter', sans-serif;
}


/* убираем стандартные отступы */
.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}


/* Заголовки */

h1, h2, h3 {
    color: white !important;
}


/* Главный заголовок */

.hero-title {

    font-size: 48px;
    font-weight: 700;
    text-align:center;

    background:
    linear-gradient(
    90deg,
    #ffffff,
    #c084fc
    );

    -webkit-background-clip:text;
    color:transparent;

    margin-bottom:10px;
}


.hero-text {

    text-align:center;
    color:#a1a1aa;
    font-size:18px;

}


/* Карточки */

.card {

background:
linear-gradient(
145deg,
rgba(255,255,255,0.08),
rgba(255,255,255,0.02)
);

border:

1px solid rgba(168,85,247,0.25);

border-radius:20px;

padding:25px;

box-shadow:
0 0 30px rgba(168,85,247,0.15);

}


/* Метрики */


.metric-title {

color:#a1a1aa;
font-size:14px;

}


.metric-value {

font-size:32px;
font-weight:700;
color:white;

}


.metric-change {

color:#c084fc;
font-size:14px;

}



/* кнопки */

.stButton button {

background:

linear-gradient(
90deg,
#9333ea,
#c026d3
);


border:none;

border-radius:30px;

color:white;

padding:10px 30px;

font-weight:600;

}


/* вкладки */


button[data-baseweb="tab"] {

background:#111018;

border-radius:20px;

padding:12px 25px;

color:white;

}


button[data-baseweb="tab"][aria-selected="true"] {

background:
linear-gradient(
90deg,
#7e22ce,
#c026d3
);

}



/* графики */

[data-testid="stPlotlyChart"] {

background:

rgba(255,255,255,0.03);

border-radius:20px;

padding:15px;

}


</style>

""", unsafe_allow_html=True)



# ==============================
# ДАННЫЕ
# ==============================


@st.cache_data
def get_data():

    df = pd.DataFrame({

        "Год":
        [2023,2024,2025],

        "Выручка":
        [612.2,856.8,920],

        "EBITDA":
        [213.4,258.1,280],

        "Чистая прибыль":
        [-14,55,70]

    })

    return df



df = get_data()



# ==============================
# ВЕРХНИЙ ЭКРАН
# ==============================


st.markdown(
"""
<div class="hero-title">
Аэрофлот Аналитика
</div>

<div class="hero-text">

Интеллектуальная система финансового анализа,
прогнозирования и оценки рисков

</div>

<br>

""",
unsafe_allow_html=True
)



col1,col2,col3 = st.columns(3)


with col1:

    st.markdown(
    """
    <div class="card">

    <div class="metric-title">
    Выручка 2024
    </div>

    <div class="metric-value">
    856.8 млрд ₽
    </div>

    <div class="metric-change">
    ↑ 40% к 2023
    </div>

    </div>

    """,
    unsafe_allow_html=True
    )


with col2:

    st.markdown(
    """
    <div class="card">

    <div class="metric-title">
    EBITDA
    </div>

    <div class="metric-value">
    258.1 млрд ₽
    </div>

    <div class="metric-change">
    ↑ 21%
    </div>

    </div>

    """,
    unsafe_allow_html=True
    )


with col3:

    st.markdown(
    """
    <div class="card">

    <div class="metric-title">
    Чистая прибыль
    </div>

    <div class="metric-value">
    55 млрд ₽
    </div>

    <div class="metric-change">
    Восстановление
    </div>

    </div>

    """,
    unsafe_allow_html=True
    )



st.write("")
# ==============================
# ОСНОВНАЯ НАВИГАЦИЯ
# ==============================


tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Финансовый анализ",
        "Прогнозирование",
        "Оценка рисков",
        "Стресс-тест"
    ]
)



# ==============================
# ФИНАНСОВЫЙ АНАЛИЗ
# ==============================

with tab1:


    st.subheader("Финансовая динамика компании")


    fig = go.Figure()


    fig.add_trace(
        go.Bar(
            x=df["Год"],
            y=df["Выручка"],
            name="Выручка",
            marker_color="#a855f7"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=df["Год"],
            y=df["EBITDA"],
            name="EBITDA",
            mode="lines+markers",
            line=dict(
                color="#22c55e",
                width=3
            )
        )
    )


    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=450,

        legend=dict(
            orientation="h"
        )

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    st.subheader("Ключевые показатели")


    col1,col2,col3 = st.columns(3)


    with col1:

        st.markdown(
        """
        <div class="card">

        <div class="metric-title">
        Рост выручки
        </div>

        <div class="metric-value">
        +40%
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col2:

        st.markdown(
        """
        <div class="card">

        <div class="metric-title">
        Рост EBITDA
        </div>

        <div class="metric-value">
        +21%
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col3:

        st.markdown(
        """
        <div class="card">

        <div class="metric-title">
        Рентабельность
        </div>

        <div class="metric-value">
        6.4%
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )



# ==============================
# ПРОГНОЗИРОВАНИЕ
# ==============================


with tab2:


    st.subheader(
        "Прогноз финансовых показателей"
    )


    st.info(
        "Прогноз рассчитан на основе динамики 2023–2024 годов"
    )


    forecast = df[df["Год"] == 2025]


    col1,col2,col3 = st.columns(3)



    with col1:

        st.markdown(
        f"""
        <div class="card">

        <div class="metric-title">
        Прогноз выручки 2025
        </div>

        <div class="metric-value">
        {forecast["Выручка"].iloc[0]} млрд ₽
        </div>

        <div class="metric-change">
        +7.4% к 2024
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col2:

        st.markdown(
        f"""
        <div class="card">

        <div class="metric-title">
        Прогноз EBITDA
        </div>

        <div class="metric-value">
        {forecast["EBITDA"].iloc[0]} млрд ₽
        </div>


        </div>
        """,
        unsafe_allow_html=True
        )



    with col3:

        st.markdown(
        f"""
        <div class="card">

        <div class="metric-title">
        Прогноз прибыли
        </div>

        <div class="metric-value">
        {forecast["Чистая прибыль"].iloc[0]} млрд ₽
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )



    fig_forecast = px.line(

        df,

        x="Год",

        y=[
            "Выручка",
            "EBITDA",
            "Чистая прибыль"
        ],

        markers=True

    )


    fig_forecast.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"

    )


    st.plotly_chart(
        fig_forecast,
        use_container_width=True
    )





# ==============================
# ОЦЕНКА РИСКОВ
# ==============================


with tab3:


    st.subheader(
        "Комплексная оценка финансовых рисков"
    )


    # условный индекс риска

    risk_score = 25



    if risk_score < 40:

        risk_status = "НИЗКИЙ"

    elif risk_score < 70:

        risk_status = "СРЕДНИЙ"

    else:

        risk_status = "ВЫСОКИЙ"



    col1,col2 = st.columns(2)



    with col1:


        st.markdown(
        f"""
        <div class="card">

        <div class="metric-title">
        Индекс риска
        </div>

        <div class="metric-value">
        {risk_score} / 100
        </div>

        <div class="metric-change">
        Уровень: {risk_status}
        </div>


        </div>

        """,

        unsafe_allow_html=True

        )



    with col2:


        st.markdown(
        """

        <div class="card">

        <div class="metric-title">
        Аналитическое заключение
        </div>


        <p>
        ✓ Рост выручки положительный
        </p>

        <p>
        ✓ EBITDA увеличивается
        </p>

        <p>
        ✓ Компания восстановила прибыльность
        </p>


        </div>

        """,

        unsafe_allow_html=True

        )



    risk_data = pd.DataFrame({

        "Фактор":

        [
        "Ликвидность",
        "Прибыльность",
        "Рост выручки",
        "Долговая нагрузка"
        ],

        "Оценка":

        [
        85,
        75,
        90,
        70
        ]

    })



    fig_risk = px.bar(

        risk_data,

        x="Фактор",

        y="Оценка"

    )


    fig_risk.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"

    )


    st.plotly_chart(

        fig_risk,

        use_container_width=True

    )



# ==============================
# СТРЕСС-ТЕСТ
# ==============================


with tab4:


    st.subheader(
        "Моделирование негативных сценариев"
    )


    shock = st.slider(

        "Снижение выручки (%)",

        0,

        50,

        10

    )


    current_revenue = 856.8


    new_revenue = current_revenue * (
        1 - shock / 100
    )


    new_profit = 55 * (
        1 - shock / 100
    )



    col1,col2 = st.columns(2)



    with col1:


        st.markdown(

        f"""

        <div class="card">


        <div class="metric-title">
        Новая выручка
        </div>


        <div class="metric-value">
        {new_revenue:.1f} млрд ₽
        </div>


        </div>

        """,

        unsafe_allow_html=True

        )



    with col2:


        st.markdown(

        f"""

        <div class="card">


        <div class="metric-title">
        Прогноз прибыли
        </div>


        <div class="metric-value">
        {new_profit:.1f} млрд ₽
        </div>


        </div>

        """,

        unsafe_allow_html=True

        )



    if shock > 25:

        st.error(
            "Высокий уровень риска: требуется антикризисный сценарий"
        )

    elif shock > 10:

        st.warning(
            "Средний уровень риска"
        )

    else:

        st.success(
            "Компания сохраняет устойчивость"
        )