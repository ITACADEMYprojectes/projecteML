import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('linear_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Título de la aplicación
st.title('Predicción del Gasto Anual de clientes de una Tienda de Ropa (Regresión Lineal)')

# Entrada de datos del usuario
length_of_membership = st.number_input('Length of Membership (meses)', min_value=0)
time_on_app = st.number_input('Time on App (minutos)', min_value=0)
avg_session_length = st.number_input('Avg. Session Length (minutos)', min_value=0)

# Crear un DataFrame con las entradas
user_data = pd.DataFrame({
    'Length of Membership': [length_of_membership],
    'Time on App': [time_on_app],
    'Avg. Session Length': [avg_session_length]
})

# Estandarizar las entradas
user_data_standardized = scaler.transform(user_data)

# Realizar la predicción
prediction = model.predict(user_data_standardized)

# Mostrar la predicción
st.write(f'Predicción del Gasto Anual: {prediction[0]:.2f}')

