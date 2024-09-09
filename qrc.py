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
    qr = qrcode.make_image(fill='black', back_color='white')
    qr.save("qrcode.png")
    save = "qrcode.png"
    st.download_button("Baixar QR Code",save,"qrcode.png")