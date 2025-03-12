import streamlit as st
from PIL import Image, ImageDraw

# ✅ Page Config
st.set_page_config(
    page_title="Portfolio - Shahjhan Gondal", 
    page_icon="📄",  # You can use a local path for an icon
    layout="wide"
)

# ✅ Portfolio Information
name = "Muhammad Shahjhan Gondal"
email = "shahjhangondal99@gmail.com"
phone = "+923406337733"
address = "DHA 4, Lahore, Pakistan"
linkedin = "https://linkedin.com/in/muhammad-shahjhan-gondal-493884311"
github = "https://github.com/shahjhan99"

import base64
from io import BytesIO

# ✅ Load & Process Profile Picture
image_path = r"G:\Jupyter Projects\Portfolio\pic.jpg"
img = Image.open(image_path)

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def make_circle(image, new_size=(200, 200)):  # Adjust size
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

# ✅ Centered Section
col1, col2, col3 = st.columns([1, 2, 1])  # Center content
with col2:
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{}" 
                 style="width: 200px; padding-left: -10px; padding-right: 20px; border-radius: 50%;" />
        </div>
        """.format(image_to_base64(circular_image)),
        unsafe_allow_html=True
    )
    
    # Centered Name & Title using HTML
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="font-size: 36px; margin-bottom: 5px;">Muhammad Shahjhan Gondal</h1>
            <p style="font-size: 18px; color: gray;">Software Engineer | AI & Machine Learning Enthusiast</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ✅ Centered Education
st.markdown("---")
st.header("🎓 Education", divider="gray")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.write("""
    - **BS Software Engineering** - Government College University, Faisalabad (2020-2024)
    - **Intermediate (12th) Science Group** - Pak Garrison College, Nankana Sahib (2018-2020)
    """)

st.markdown("---")

# ✅ Sidebar Contact Information
st.sidebar.header("📬 Contact Information")
st.sidebar.write(f"📧 Email: {email}")
st.sidebar.write(f"📞 Phone: {phone}")
st.sidebar.write(f"📍 Address: {address}")
st.sidebar.write(f"🔗 [LinkedIn]({linkedin})")
st.sidebar.write(f"💻 [GitHub]({github})")

# ✅ Skills
st.header("🚀 Skills"  ,divider="gray")
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
st.header("🎓 Certifications" , divider="gray")
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

# ✅ Projects Section (Centered)
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
