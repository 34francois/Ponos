import streamlit as st
from streamlit_navigation_bar import st_navbar
pages = ["Univers professionnels","Formations professionnelles","Stages en entreprise"]

styles = {
  "nav": {"background-color": "#9ea4f0", "justify-content": "left"},
    "img": {"padding-right": "14px"},
    "span": {"color": "white", "padding": "14px"},
    "active": {"background-color": "white", "color": "var(--text-color)", "font-weight": "normal", "padding": "14px"},
}

options = {"show_menu": False, "show_sidebar": False}
page = st_navbar(pages, styles=styles)

#Etat de session----------------------------


#----------------------------Etat de session



#BDA---------------------------------------




#--------------------------------------BDA



#DEF--------------------------------------

def questionnaire_orientation():
    st.title("Questionnaire d'Orientation Professionnelle")
    st.write("Réponds à ces questions pour découvrir les métiers qui te correspondent.")

    # Questions
    questions = {
        "Aimes-tu les mathématiques et la résolution de problèmes ?": ["Oui", "Non"],
        "Préfères-tu les activités créatives ?": ["Oui", "Non"],
        "Aimes-tu travailler en équipe ?": ["Oui", "Non"],
        "Es-tu à l'aise avec les nouvelles technologies ?": ["Oui", "Non"],
        "Aimes-tu aider les autres ?": ["Oui", "Non"],
    }

    reponses = {}
    for question, options in questions.items():
        reponses[question] = st.radio(question, options)

    # Analyse des réponses
    metiers_suggeres = []
    if reponses["Aimes-tu les mathématiques et la résolution de problèmes ?"] == "Oui":
        metiers_suggeres.extend(["Ingénieur", "Informaticien", "Scientifique"])
    if reponses["Préfères-tu les activités créatives ?"] == "Oui":
        metiers_suggeres.extend(["Artiste", "Designer", "Musicien"])
    if reponses["Aimes-tu travailler en équipe ?"] == "Oui":
        metiers_suggeres.extend(["Manager", "Enseignant", "Infirmier"])
    if reponses["Es-tu à l'aise avec les nouvelles technologies ?"] == "Oui":
        metiers_suggeres.extend(["Développeur web", "Data scientist", "Cybersecurity analyst"])
    if reponses["Aimes-tu aider les autres ?"] == "Oui":
        metiers_suggeres.extend(["Médecin", "Assistant social", "Psychologue"])

# Résultats
def questionnaire_orientation_resultat(metiers_suggeres):
    st.header("Résultats")
    if metiers_suggeres:
        st.write("En fonction de tes réponses, les métiers suivants pourraient te correspondre :")
        for metier in metiers_suggeres:
            st.write(f"- {metier}")
    else:
        st.write("Nous n'avons pas pu trouver de métiers correspondant à tes réponses. Essaye de répondre à plus de questions.")

#---------------------------------------DEF


#SIDEBAR----------------------------------

with st.sidebar:
  st.header("Charger une base de donnée")
  questionnaire_orientation()



#----------------------------------SIDEBAR





if page == "Univers professionnels":
  st.header("Univers professionnels")
  questionnaire_orientation_resultat(metiers_suggeres)




#---------------------Univers professionnels




if page == "Formations professionnels":
  st.header("Formations professionnels")







#---------------------Univers professionnels





if page == "Stages en entreprise":
  st.header("Stages en entreprise")







#---------------------Univers professionnels
