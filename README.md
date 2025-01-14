# Simulador de Neurona Artificial
Trabajo de Clase - Neurona genérica con función de activación (perceptrón simple). Esta aplicación web simula el funcionamiento de una neurona artificial, permitiendo ajustar sus parámetros y visualizar su salida.

![Neurona Artificial](https://github.com/warc0s/neurona_generica/blob/main/foto.jpg?raw=true)


## Características

- Selección de hasta 10 entradas/pesos
- Actualización dinámica de los valores
- Tres funciones de activación: Sigmoide, ReLU y Tangente Hiperbólica
- Interfaz moderna y fácil de usar

## Instalación

1. Asegúrate de tener Python instalado en tu sistema
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación:
```bash
streamlit run app.py
```

## Uso

1. Selecciona el número de entradas/pesos usando el deslizador
2. Ajusta los valores de los pesos (w)
3. Introduce los valores de entrada (x)
4. Establece el valor del sesgo
5. Selecciona la función de activación deseada
6. Haz clic en "Calcular la salida" para ver el resultado
