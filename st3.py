import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title='Arrhenius 完整版')
st.title('阿伦尼乌斯公式 · 科研完整版')

# === 侧边栏参数（st.sidebar：将控件集中到左侧） ===
with st.sidebar:
    st.header('⚙️ 参数设置')
    Ea = st.slider('活化能 Ea (kJ/mol)', 50, 200, 100)
    A = st.slider('指前因子 A (×10¹²)', 1.0, 100.0, 10.0)
    T_min = st.number_input('起始温度 (K)', 200, 500, 300)
    T_max = st.number_input('终止温度 (K)', 500, 1500, 1000)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# === 多温度区间分色展示 ===
R = 8.314;  Ea_J = Ea * 1000
T = np.linspace(T_min, T_max, 200)
k = (A * 1e12) * np.exp(-Ea_J / (R * T))

fig = go.Figure()
fig.add_trace(go.Scatter(x=T, y=k, mode='lines',
    name=f'Ea={Ea} kJ/mol', line=dict(color=colors[0], width=3)))

st.plotly_chart(fig, width="stretch")

# === 数据导出功能（满足论文可复现要求） ===
if st.button('导出数据为 CSV'):
    df = pd.DataFrame({'温度 T (K)': T, '速率常数 k (s⁻¹)': k})
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button('点此下载 CSV', csv, 'arrhenius_data.csv')