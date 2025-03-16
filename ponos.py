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


#---------------------------------------DEF


#SIDEBAR----------------------------------

with st.sidebar:
  st.header("Charger une base de donnée")




#----------------------------------SIDEBAR





if page == "Univers professionnels":
  st.header("Univers professionnels")







#---------------------Univers professionnels




if page == "Formations professionnels":
  st.header("Formations professionnels")







#---------------------Univers professionnels





if page == "Stages en entreprise":
  st.header("Stages en entreprise")







#---------------------Univers professionnels
