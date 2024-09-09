import streamlit as st
import qrcode

link = st.text_input('Link do QR Code',key='link1')
data = link
criar = st.button('Criar QR Code')
if criar == True:
    qrcode = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,)
    qrcode.add_data(data)
    qrcode.make(fit=True)
    img = qrcode.make_image(fill='black', back_color='white')
    salva = st.button('Baixar QrCode')
    if salva == True:
        img.save("qrcode.png")
