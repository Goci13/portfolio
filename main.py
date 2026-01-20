import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(page_title='Portfolio', page_icon='logo.PNG')


################## Hintergrundbild setzen ###################
# # Base64-kodiertes Bild einfügen
# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()

# image_base64 = get_base64_image('bg.jpeg')

# # page_bg_img = f'''
# # <style>
# # .stApp {{
# #     background-image: url("data:image/jpeg;base64,{image_base64}");
# #     background-size: cover;
# #     background-position: center;
# #     background-repeat: no-repeat;
# #     background-attachment: fixed;
# # }}
# # </style>
# # '''

# # st.markdown(page_bg_img, unsafe_allow_html=True)
##############################################################

# CSS, um den oberen Abstand der Seite zu verkleinern
st.markdown(
    """
    <style>
    div.block-container {
        padding-top: 0rem; /* Reduziert den Abstand nach oben */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Burger entfernen
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# HTML und CSS für die Überschrift mit gleichmäßigen Linien
html_code = """
<div style="display: flex; align-items: center; justify-content: center;">
    <div style="flex: 1; height: 2px; background-color: white; margin: 0 30px 0 10px;"></div>
    <h2 style="margin: 0; font-size: 44px; font-weight: bold; text-align: center;">Goran Mikic</h2>
    <div style="flex: 1; height: 2px; background-color: white; margin: 0 10px 0 10px;"></div>
</div>
"""

# Einfügen des HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)

###################################################


selected = option_menu(
    menu_title=None,
    options=['Home', 'Projekte', 'Kontakt'],
    icons=['house', 'book', 'envelope'], # bootstrap icons
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {"background-color": "#e4ebf7"},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "black"},
        "nav-link-selected": {"background-color": "#00FFC4", "color": "black"},
    }
)

####################### Erste Zeile ##########################
# st.write('##')
if selected == 'Home':
    st.write('##')
    col1, col2 = st.columns(2)
    with col1:
        st.image('assets/foto.png')
    with col2:
        st.write("<h2 style='color: #00FFC4;'>Etwas über mich:</h2>", unsafe_allow_html=True)
        st.write(
            """
            Nach 20 Jahren in der Industrie habe
            ich beschlossen, meine Leidenschaft
            für das Programmieren zu verfolgen.
            Mit frischem Elan und umfassender 
            Erfahrung starte ich nun meinen Weg 
            als Programmierer, um mich in einer 
            dynamischen, technologiegetriebenen 
            Welt weiterzuentwickeln und kreative 
            Lösungen zu finden.
            """
        )
    st.write('---')

######################## Zweite Zeile ########################
    st.write('##')
    spalte1, spalte2 = st.columns(2)
    with spalte1:
        st.write("<h2 style='color: #00FFC4;'>Was ich mache:</h2>", unsafe_allow_html=True)
        st.write(
            """
            - Python programmieren
            - Webanwendungen erstellen
            - Machine Learning
            - Grafische UI erstellen
            - Computer Vision
            - Deep Learning
            """
        )
    with spalte2:
        st.image('assets/python.jpg')
    st.write('---')

########################## Dritte Zeile #########################

    st.write('##')
    st.write("<h2 style='color: #00FFC4;'>Meine Zertifikate</h2>", unsafe_allow_html=True)
    st.write('##')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Python Bootcamp')
        st.write('OpenCV')
    with col2:
        st.write('Streamlit')
        st.write('Daten Analyse')
    with col3:
        st.write('Machine Learning')
        st.write('Deep Learning')

    st.write('---')
    st.write("<p style='color: gray;'>Made by Goran Mikic</p>", unsafe_allow_html=True)


######################### Projekte ###############################
if selected == 'Projekte':
    st.title(f'Ein paar {selected}: ')
    st.write('---')
    st.markdown(
    "<p style='text-align:center;'>Machine Learning</p>",
    unsafe_allow_html=True)
    st.image('assets/projekt_1.1.png')
    st.image('assets/projekt_1.2.png')
    st.write('---')
    st.markdown(
    "<p style='text-align:center;'>Graphical UI</p>",
    unsafe_allow_html=True)
    st.image('assets/projekt_gui.png', use_container_width=True)
    st.write('---')
    st.markdown(
    "<p style='text-align:center;'>Etwas Robotik</p>",
    unsafe_allow_html=True)
    st.video('assets/My Project.mp4')
    st.video('assets/My Project2.mp4')
    st.video('assets/My Project3.mp4')
    st.caption(
    "Entwicklung und Programmierung verschiedener Roboter mit Fokus auf "
    "Computer Vision. Die Roboter erkennen Farben über Kamerasysteme und "
    "sortieren Objekte automatisch anhand definierter Kriterien."
)



########################## Kontakt #################################
if selected == 'Kontakt':
    st.write('##')
    st.subheader('Goran Mikic')
    st.write(
        """
        Domstiftstr. 12\n
        68307 Mannheim\n
        Germany\n
        ---\n
        """
    )

    st.write("<p style='color: #00FFC4;'>mikic-clan@freenet.de</p>", unsafe_allow_html=True)

