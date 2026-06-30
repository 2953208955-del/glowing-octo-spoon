import gradio as gr
import numpy as np
import plotly.graph_objects as go

def calc_arrhenius(Ea, A):
    T = np.linspace(300, 1000, 100)
    k = (A*1e12)*np.exp(-Ea*1000/(8.314*T))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=T, y=k))
    return fig

def calc_langmuir(K):
    P = np.linspace(0, 10, 200)
    theta = (K*P)/(1+K*P)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=P, y=theta))
    return fig

# Blocks 实现多模型切换
with gr.Blocks(title='化学面板集成') as demo:
    gr.Markdown('# 🔬 化学动力学工具包')
    with gr.Tab('阿伦尼乌斯'):
        ea = gr.Slider(50, 200, label='活化能')
        a = gr.Slider(1, 100, label='指前因子')
        btn1 = gr.Button('计算')
        plot1 = gr.Plot()
        btn1.click(calc_arrhenius, [ea, a], plot1)
    with gr.Tab('Langmuir 吸附'):
        k = gr.Slider(0.1, 100, label='K')
        btn2 = gr.Button('计算')
        plot2 = gr.Plot()
        btn2.click(calc_langmuir, k, plot2)

demo.launch()