import streamlit as st

isim=st.header("Karayolu hız hesaplama")
hiz=st.number_input("Hızınızı Giriniz :",10,140,40,10)

a=st.checkbox("Sağ")
b=st.checkbox("Orta")
c=st.checkbox("Sol")

if st.button("Hesaplama"):
    if hiz<40 and c:
        st.write("Hızınız bu şeride için çok düşük.")
    elif hiz>=40 and c:
        st.write("Hızınız bu şerit için uygundur.")
    elif hiz>90 and c:
        st.write("Hızınız bu şerit için çok yüksek.")
    elif hiz<90 and b:
        st.write("Hızınız bu şeride için çok düşük.")
    elif hiz>=90 and b:
        st.write("Hızınız bu şerit için uygundur.")
    elif hiz>120 and b:
        st.write("Hızınız bu şerit için çok yüksek.")
    elif hiz<100 and a:
        st.write("Hızınız bu şeride için çok düşük.")
    elif hiz>=100 and a:
        st.write("Hızınız bu şerit için uygundur.")
    elif hiz>140 and a:
        st.write("Hızınz karayolları için çok yüksek. ")



