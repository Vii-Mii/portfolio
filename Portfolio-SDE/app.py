import streamlit as st
from components import home_show, experience_show, projects_show, education_show, skills_show

# Force light mode settings
st.set_page_config(
    page_title="Vijayaraj Pushpalingam | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for navigation buttons and other elements
st.markdown("""
<style>

    
    /* Navigation Button Styles */
    .stButton > button {
        width: 100%;
        border-radius: 5px;
        height: 40px;
        margin: 5px 0;
        background-color: #white;
        color: black;
        border: none;
        font-weight: bold;
    }
    

</style>
""", unsafe_allow_html=True)

# Sidebar navigation
def navigation():
    with st.sidebar:
        st.title("Navigation 🧭")
        pages = {
            "Home": home_show,
            "Experience": experience_show,
            "Skills": skills_show,
            "Projects": projects_show,
            "Education": education_show,
            
        }
        
        for page_name, page_func in pages.items():
            if st.button(
                page_name,
                key=page_name,
                use_container_width=True,
            ):
                st.session_state.current_page = page_name

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

navigation()

# Display current page
if st.session_state.current_page == "Home":
    home_show()
elif st.session_state.current_page == "Experience":
    experience_show()
elif st.session_state.current_page == "Projects":
    projects_show()
elif st.session_state.current_page == "Education":
    education_show()
elif st.session_state.current_page == "Skills":
    skills_show() 