import streamlit as st
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# Configuración de la página
st.set_page_config(
    page_title="Simulador de neurona",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Imagen
st.image("neurona.png", width=400)

# Título
st.title("Simulador de neurona - MGE")

# CSS personalizado para mejorar la apariencia
st.markdown("""
    <style>
    .stSlider > div > div > div > div {
        background-color: #ff4b4b;
    }
    .stNumberInput > div > div > input {
        background-color: #1e1e1e;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Selector de número de entradas/pesos
st.write("Elige el número de entradas/pesos que tendrá la neurona")
num_inputs = st.slider("", min_value=1, max_value=10, value=1, key="num_inputs")

# Sección de Pesos
st.header("Pesos")
weights = []
for i in range(num_inputs):
    w = st.number_input(f"w{i}", value=0.0, format="%.2f", key=f"weight_{i}")
    weights.append(w)

# Mostrar lista de pesos
st.write(f"w = {weights}")

# Sección de Entradas
st.header("Entradas")
inputs = []
for i in range(num_inputs):
    x = st.number_input(f"x{i}", value=0.0, format="%.2f", key=f"input_{i}")
    inputs.append(x)

# Mostrar lista de entradas
st.write(f"x = {inputs}")

# Sección de Sesgo y Función de activación
col1, col2 = st.columns(2)

with col1:
    st.header("Sesgo")
    st.write("Introduce el valor del sesgo")
    bias = st.number_input("", value=0.0, format="%.2f", key="bias")

with col2:
    st.header("Función de activación")
    st.write("Elige la función de activación")
    activation_function = st.selectbox(
        "",
        ["Sigmoide", "Relu", "Tangente hiperbólica"],
        key="activation"
    )

# Botón para calcular
if st.button("Calcular la salida", type="primary"):
    # Calcular la suma ponderada
    weighted_sum = np.dot(weights, inputs) + bias
    
    # Aplicar la función de activación
    if activation_function == "Sigmoide":
        result = sigmoid(weighted_sum)
    elif activation_function == "Relu":
        result = relu(weighted_sum)
    else:  # Tangente hiperbólica
        result = tanh(weighted_sum)
    
    # Mostrar resultado
    st.write("---")
    st.write(f"Salida de la neurona: {result:.4f}")

st.write("---")
st.write("Desarrollado por [Marcos Garcia Estevez](https://github.com/warc0s)")