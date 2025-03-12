import streamlit as st
from PIL import Image, ImageDraw
import base64
from io import BytesIO

# ✅ Page Configuration
st.set_page_config(
    page_title="Portfolio - Shahjhan Gondal", 
    page_icon="📄",
    layout="wide"
)

# ✅ Portfolio Information
name = "Muhammad Shahjhan Gondal"
email = "shahjhangondal99@gmail.com"
phone = "+923406337733"
address = "DHA 4, Lahore, Pakistan"
linkedin = "https://linkedin.com/in/muhammad-shahjhan-gondal-493884311"
github = "https://github.com/shahjhan99"

# ✅ Load & Process Profile Picture
image_path = "pic.jpg"  # Ensure this file is in your repo
img = Image.open(image_path)

# Function to Convert Image to Base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Function to Make Circular Image
def make_circle(image, new_size=(200, 200)):  
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    image = image.resize((size, size), Image.LANCZOS)
    circular_img = Image.new("RGBA", (size, size))
    circular_img.paste(image, (0, 0), mask)
    
    circular_img = circular_img.resize(new_size, Image.LANCZOS)
    return circular_img

circular_image = make_circle(img, new_size=(200, 200))

# ✅ Toggle Sidebar Position
if "show_contact" not in st.session_state:
    st.session_state.show_contact = False

# ✅ Centered Profile Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Profile Picture
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_to_base64(circular_image)}" 
                 style="width: 200px; border-radius: 50%;" />
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Name & Title
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="font-size: 36px; margin-bottom: 5px;">Muhammad Shahjhan Gondal</h1>
            <p style="font-size: 18px; color: gray;">Software Engineer | AI & Machine Learning Enthusiast</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Contact Button Below Name
    if st.button("📞 Contact Info", use_container_width=True):
        st.session_state.show_contact = not st.session_state.show_contact

st.markdown("---")

# ✅ Contact Section (Toggles Between Sidebar & Main Page)
if st.session_state.show_contact:
    st.header("📬 Contact Information")
    st.write(f"📧 Email: {email}")
    st.write(f"📞 Phone: {phone}")
    st.write(f"📍 Address: {address}")
    st.write(f"🔗 [LinkedIn]({linkedin})")
    st.write(f"💻 [GitHub]({github})")
else:
    st.sidebar.header("📬 Contact Information")
    st.sidebar.write(f"📧 Email: {email}")
    st.sidebar.write(f"📞 Phone: {phone}")
    st.sidebar.write(f"📍 Address: {address}")
    st.sidebar.write(f"🔗 [LinkedIn]({linkedin})")
    st.sidebar.write(f"💻 [GitHub]({github})")

st.markdown("---")

# ✅ Education Section
st.header("🎓 Education", divider="gray")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.write("""
    - **BS Software Engineering** - Government College University, Faisalabad (2020-2024)
    - **Intermediate (12th) Science Group** - Pak Garrison College, Nankana Sahib (2018-2020)
    """)

st.markdown("---")

# ✅ Skills Section
st.header("🚀 Skills", divider="gray")
st.write("""
- **Languages:** C#, C++, Python
- **Tools & IDEs:** VS Code, Jupyter, Visual Studio, PyCharm, Google Colab
- **Databases:** SQL, Firebase, MySQL
- **Other:** Git, Agile Methodologies, Data Preprocessing
""")

# ✅ Interests
st.header("💡 Interests", divider="gray")
st.write("""
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Natural Language Processing (NLP)
- Deep Learning
- Data Science
""")

# ✅ Certifications
st.header("🎓 Certifications", divider="gray")
st.write("""
- **Artificial Intelligence/ML (Microsoft Certificate - TEVTA)**
  - [View Certificate](https://drive.google.com/file/d/1L4XM5P_aOYgLO1ijiZ0Lh_RM-nRZvHmt/view?usp=sharing)
- **Deep Learning (iCodeGuru)**
  - [View Certificate](https://drive.google.com/file/d/10dT_8UjglJigB_2KoSd-MV1LSjnfb-6P/view?usp=sharing)
- **Python Certification**
  - [View Certificate](https://drive.google.com/file/d/1ypI2QM9zMy6b7N1M9Hk9mzxT03_sWVgt/view?usp=sharing)
- **CCNA, CCNP (CISCO & HUAWEI)**
- **MCSE**
""")

# ✅ Projects Section
st.header("📂 Projects", divider="gray")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.subheader("Final Year Project")
    st.write("**AI Resume Analyzer:** AI-driven system for analyzing and scoring resumes for recruitment.")

    # 🔹 AI & Python Projects
    st.subheader("AI & Python Projects")
    st.write("""
    - **Model Training & Fine-tuning**
    - **LSTM - Next Word Predictor**
    - **Face Recognition System**
    - **House Prices Prediction**
    - **Rainfall Prediction**
    - **Student Performance Prediction**
    - **Salary Prediction using Multi-Feature Regression**
    - **Old Car Price Prediction**
    - **Logic Gate Prediction using Regression & Neural Networks**
    - **Voice-to-Text System**
    """)

    # 🔹 YOLO Projects
    st.subheader("YOLO Projects")
    st.write("License Plate Detection & Recognition using YOLO for real-time applications.")

    # 🔹 GitHub Projects
    st.subheader("GitHub Projects")
    st.write("""
    - **Image Processing**
    - **Mango Variety Classification using Random Forest**
    - **Iris Flower Classification using Streamlit**
    """)

    # 🔹 C# Projects
    st.subheader("C# Projects")
    st.write("""
    - **Optics Store Management System** (Real-Time Functional)
    - **Messenger Chat Application**
    - **Pharmacy Management System**
    - **ATM System**
    - **Car Racing Game**
    - **Bricks Breaking Game**
    - **Media Player**
    - **Chat Bot**
    - **Weather Application**
    """)

st.markdown("---")
st.write(f"Feel free to connect with me via [LinkedIn]({linkedin}) or explore my [GitHub]({github}) repositories!")
