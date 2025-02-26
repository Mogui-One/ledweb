import streamlit as st
import time
import serial

# Função para comunicar com o Arduino
def enviar_comando_para_arduino(cor):
    try:
        ser = serial.Serial('COM5', 9600)  # Substitua 'COM5' pela porta correta do seu Arduino
        time.sleep(2)  # Aguarda a conexão ser estabelecida
        ser.write(f'{cor}\n'.encode())  # Envia a cor para o Arduino
        ser.close()
    except Exception as e:
        st.error(f"Erro ao conectar na porta serial: {e}")

# Interface Streamlit
st.title("Controle de LED com Arduino")

# Escolha de cor com o color picker
cor_led = st.color_picker("Escolha a cor do LED", "#000000")  # Cor inicial é preta

# Converter a cor para o formato adequado para o Arduino (RGB)
def converter_cor_hex_para_rgb(cor_hex):
    # Remove o '#' e converte os valores hexadecimais para inteiros
    r = int(cor_hex[1:3], 16)
    g = int(cor_hex[3:5], 16)
    b = int(cor_hex[5:7], 16)
    return f'R{r} G{g} B{b}'  # Formato que o Arduino entende

# Se o usuário escolheu uma cor, envia para o Arduino
if cor_led:
    cor_rgb = converter_cor_hex_para_rgb(cor_led)
    enviar_comando_para_arduino(cor_rgb)
    st.write(f"Cor enviada para o Arduino: {cor_rgb}")
