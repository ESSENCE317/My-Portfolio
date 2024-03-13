import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Assets
lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")
lottie_contact = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")
image = Image.open("dark-mode-bugs.jpg")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
local_css(r"C:\Users\Cody\PycharmProjects\My-Portfolio\Style\style.css")

st.write("##")
st.subheader("Hi There! :wave:")
st.title("My Portfolio Website")

st.write("""
Blah blah blah Blah blah blah Blah blah blah Blah blah blah Blah blah blah
""")

# Links
st.write("[Read More](https://github.com/ESSENCE317)")

# Divider
st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation = 'horizontal'
    )

# About Me section
if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Cody Thomas")
            st.title("Software Engineer/Python Developer")
        with col2:
            st_lottie(lottie_coder)

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            My Full Skillset
            - Python
                - Developing apps and writing scripts in either Linux(Ubuntu) or Windows
                - IT Automation with Python (Google Certified)
                - Databases with SQL and Scientific Computing (Matplotlib, Pandas, NumPy)
                - Familiar with using Version Control Systems and repositories for shell scripting, file management, and debugging 
            - Web Dev
                - HTML/CSS (Responsive Web Design)
                - Flask
                - Django
                - React
            - Technical Support/IT
                - Source Control(Git & Github)
                - Networking/Troubleshooting and Debugging
                - Customer Service
            - Video Game Development
                - 2D Animation/Pixel Art Graphics(Michigan State University Cert)
                - Pygame/Aseprite/Photoshop
                - Indie Game Dev
            """)
        with col4:
            st.subheader("""
            My Goals & Ambitions
                - I am currently on my journey to receive my PCEP Certification and my CCNA
                - Focused on landing my first tech experience
                - Committed to being a lifetime learner I am constantly in pursuit of improving and educating myself
                - I want to make the world a better place and aid tech in the future 
            """)

if selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns((1, 2))
        with col5:
            st.image(image)
        with col6:
            st.subheader("Hangman(Video Game)")
            st.markdown("[Visit Github Repo](https://github.com/ESSENCE317)")

if selected == "Contact":
    with st.container():
        st.header("Get in touch with me here!")
        st.write("##")
        st.write('##')

        contact_form = """
        <form action="https://formsubmit.co/codyatwell4315@gamil.com method="POST">
        <input type = "hidden" name ="_captcha" value = "false">
        <input type="text" name="name" placeholder = " Your name" required>
        <input type="email" name="email" placeholder = " Your email" required>
        <textarea name = "message" placeholder = "Your message" required></textarea>
        <button type="submit">Send</button>
        </form>
        
        """
        left_col, right_col = st.columns((2, 1))
        with left_col:
            st.markdown(contact_form, unsafe_allow_html= True)
        with right_col:
            st.lottie(lottie_contact,height=300)
