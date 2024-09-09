import streamlit as st
import qrcode as qr

link = st.text_input('Link do QR Code',key='link')
data = link
criar = st.button('Criar QR Code')
if criar == True:
    qr = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    salv = img.save()
    salver = st.download_button('Baixar QCode',salv,"qrcode_exemplo.png")

