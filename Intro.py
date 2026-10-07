import streamlit as st
from PIL import Image

st.title("Aplicaciones de Streamlit.")

with st.sidebar:
    st.subheader("Aplicaciones de streamlit.")
    parrafo = (
        "Los aprendizajes realizados en computacion avanzada "
        "se pueden ver reflejados en las apps que se encuentran en esta pagina "
    )
    st.write(parrafo)

url_streamlit = "https://share.streamlit.io/"
st.subheader("En el siguiente enlace puedes encontrar las apps hechas en streamlit")
st.write(f"Enlace para apps: [Enlace]({url_streamlit})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("App de frutas")
    image = Image.open('Frutas.jpg')
    st.image(image, width=190)
    st.write("En la siguiente enlace usaremos una de las aplicaciones creadas en streamlit")
    url = "https://programacion-avanzada-actividad-clase-jq6yobt3sfba2urcfygbb4.streamlit.app/"
    st.write(f"App #1: [Enlace]({url})")

    st.subheader("Gradiente")
    image = Image.open('gradiente.png')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos el gradiente.")
    url = "https://programacion-actividad-2-3rztfuvzjgzv6dazscpbsf.streamlit.app/"
    st.write(f"App #2: [Enlace]({url})")

    st.subheader("Detector de anomalias")
    image = Image.open('anomalia.png')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos un detector de anomalias.")
    url = "https://programacion-avanzada-actividad-3-ipyiwyybco2ednwtk7babr.streamlit.app/"
    st.write(f"App #3: [Enlace]({url})")

with col2:
    st.subheader("Datos:preparacion y estructura")
    image = Image.open('Datos y preparacion.png')
    st.image(image, width=200)
    st.write("En la siguiente veremos una aplicación que usa Data sets para entender, limpiar y estructurar los datos disponibles.")
    url = "https://programacion-act-4-jdbxkux2k6dmuhb6lbesxh.streamlit.app/"
    st.write(f"App #4: [Enlace]({url})")

    st.subheader("App cornare: nivel del agua")
    image = Image.open('nivel agua.png')
    st.image(image, width=190)
    st.write("En la siguiente enlace veremos la app de cornare donde se pueden analizar datos sobre el nivel del agua segun la estacion.")
    url = "https://prog-act-5-jbq8a3uusg953xty9o7whr.streamlit.app/"
    st.write(f"App # 5: [Enlace]({url})")

    st.subheader("Regresion")
    image = Image.open('regresion.png')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la regresion y sus conceptos clave.")
    url = "https://prog-act-6-iuftpuv6jxtxxwfme75hx2.streamlit.app/"
    st.write(f"App #6: [Enlace]({url})")

    st.subheader("KNN Agrosavia")
    image = Image.open('knn.png')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la app que explora KNN con datos de suelos de AGROSAVIA.")
    url = "https://computacion-avanzada-sesion-13-avrj5spayb9r8diappgl8ty.streamlit.app/"
    st.write(f"App #11: [Enlace]({url})")

with col3:
    st.subheader("Series de tiempo")
    image = Image.open('series de tiempo.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa series de tiempo.")
    url = "https://prog-avanzada-act-7-4abkehuwn887pxoprmw8ax.streamlit.app/"
    st.write(f"App #7: [Enlace]({url})")

    st.subheader("Pronostico cornare")
    image = Image.open('calidad aire.png')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la app para predecir la calidad del aire.")
    url = "https://prog-act-8-qubkilwwfvmmqf3yqtd2vu.streamlit.app/"
    st.write(f"App #8: [Enlace]({url})")

    st.subheader("Sensasion termica")
    image = Image.open('sensacion termica.png')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos el predictor de sensasion termica.")
    url = "https://prog-act-9-kaujppc44xbqjer5qnwc5c.streamlit.app/"
    st.write(f"App #9: [Enlace]({url})")

    st.subheader("Regresion logistica")
    image = Image.open('regresion logistica.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación de regresion logistica.")
    url = "https://prog-sesion-11-oj9mtmfymjqfwwqzsuyixg.streamlit.app/"
    st.write(f"App #10: [Enlace]({url})")
