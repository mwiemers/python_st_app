import streamlit as st
import pandas as pd
from load_css import local_css


st.set_page_config(
    page_title='Python Workshop Format',
    page_icon='👨‍🏫'
)

local_css("css/style.css")

st.title("Python for Statistics Pre-Sessional Bootcamp Format")

st.markdown("""

## Python for Statistics Pre-Sessional Bootcamp Format
            
### Workshop Format

The primary focus of our workshops is to support you in developing skills and strategies that will enable you to continue to learn programming 
and related digital skills independently. Our lessons are designed as projects which are broken down into a series of smaller, more maneagble tasks. 
To solve these tasks, you will use the same resources that coders around the world rely on when they don't know how to do something – 
online resources/tools, colleagues, and trial and error.
            
This bootcamp runs from 9-6pm. We will run an introduction session to explain the format of the bootcamp and run regular reviews to
ensure that everyone is at the same pace.

### The Python workshops series

The Python workshops are for beginners that have no prior experience in programming with Python and cover the following topics:

- Numerical variables
- String variables
- Converting types
- Lists
- For loops
- Conditionals
- Writing functions
- Dictionaries
- While loops
- Final Coding Challenges

&nbsp; 
            
Each of the notebooks will take you roughly 1 hour to complete. By the end of this bootcamp everyone should have completed all six projects.
            
""",
            unsafe_allow_html=True
            )
