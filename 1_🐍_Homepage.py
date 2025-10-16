import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='DSL Python for Statistics Pre-Sessional Bootcamp',
    page_icon="🐍"
)

local_css("css/style.css")

st.title("DSL Python for Statistics Pre-Sessional Bootcamp")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Development Lead - Academic Partnerships
    """)

st.image("img/lse_dsl_logo.png", width=400)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/python_logo.png", width=150)


st.markdown(
    """
    Having a working Python and installation alongside VS Code is a requirement for attending the Python for Statistics Pre-Sessional Bootcamp.
    
    To install Python on your personal laptop, please follow the instructions on this website to install Python + VS Code to use Jupyter Notebooks.
    
    We recommend to set apart 30 minutes to work through this tutorial (excluding the optional sections on installing libraries and managing environments).

    Please work through the pages from the sidebar menu for information about:
    * Why Python is one of the most popular programming languages and why you should learn it.
    * How to get access to Anthropics Claude GenAI tool.
    * Most effective ways of using Claude for your digital skills development.
    * How you can install Python + VS Code on your personal laptop.
    * The Python for Statistics Pre-Sessional Bootcamp format and timetable.
    * How to access the Python workshop materials from this website.
    * How to access and work with jupyter noteboos in VS Code.
    * How to install libraries and create and manage environments with conda (optional).
    * Filling in the confidence checks to asses the impact of the bootcamp.
    
    &nbsp;

    <div class="highlight blue">
    Our trainers can help you with fixing your installation issues at the start of the bootcamp.  
    </div>
    """, unsafe_allow_html=True
)
