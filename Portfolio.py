import streamlit as st
from PIL import Image, ImageDraw
import base64
from io import BytesIO

# ✅ Page Config
st.set_page_config(
    page_title="Portfolio - Shahjhan Gondal", 
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"  # Sidebar open by default
)

# ✅ Portfolio Information
name = "Muhammad Shahjhan Gondal"
email = "shahjhangondal99@gmail.com"
phone = "+923406337733"
address = "DHA 4, Lahore, Pakistan"
linkedin = "https://linkedin.com/in/muhammad-shahjhan-gondal-493884311"
github = "https://github.com/shahjhan99"

# ✅ Load & Process Profile Picture
image_path = r"pic.jpg"
img = Image.open(image_path)

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

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

# ✅ Session State for Sidebar Toggle
if 'show_contact' not in st.session_state:
    st.session_state.show_contact = True  # Sidebar open by default

# ✅ Centered Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Display the centered circular image
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{}" 
                 style="width: 200px; border-radius: 50%;" />
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

    # Centered Contact Info Button Below Title
    st.markdown(
        """
        <style>
        .stButton>button {
            font-size: 16px !important;
            padding: 6px 20px !important; /* Adjust padding */
            width: 410px !important; /* Set button width */
            margin: 0 auto !important; /* Center the button */
            display: block !important; /* Ensure the button is centered */
            background-color: #2C3E50 !important; /* Dark gray background */
            color: white !important; /* White text */
            border: none !important; /* Remove border */
            border-radius: 5px !important; /* Rounded corners */
        }
        .stButton>button:hover {
            background-color: #34495E !important; /* Slightly lighter gray on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Button to toggle contact info
    if st.button("📬 Contact Info"):
        st.session_state.show_contact = not st.session_state.get("show_contact", True)

# ✅ Sidebar Contact Information Toggle
if st.session_state.show_contact:
    st.sidebar.header("📬 Contact Information")
    st.sidebar.write(f"📧 Email: {email}")
    st.sidebar.write(f"📞 Phone: {phone}")
    st.sidebar.write(f"📍 Address: {address}")
    st.sidebar.write(f"🔗 [LinkedIn]({linkedin})")
    st.sidebar.write(f"💻 [GitHub]({github})")

# ✅ Centered Education
st.markdown("---")
st.header("🎓 Education")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.write("""
    - **BS Software Engineering** - Government College University, Faisalabad
    - **Intermediate (12th) Science Group** - Pak Garrison College, Nankana Sahib
    """)

st.markdown("---")

# ✅ Skills & Interests
st.header("🚀 Skills & Interest")
st.write("""
- **Languages:** C#, C++, Python
- **Tools/IDE:** VS Code, Jupyter, Visual Studio, PyCharm, Google Colab
- **Libraries & Frameworks:** Git, GitHub, YOLO, Streamlit, Hugging Face, Gradio, Transformers, Prompt Engineering, LLaMA3 (Groq), GPT-2/GPT-based Fine-Tuning
- **API & Integration:** Groq LLM API Integration, Hugging Face Model Access via API Tokens, Secure API Key Management (Google Colab)
- **Database:** SQL, Firebase, MySQL, FAISS (Vector Store)
- **Laboratory:** RAG Application, Agile Methodologies, Waterfall, Data Preprocessing
- **Interests:** Artificial Intelligence, Deep Learning, Machine Learning, Generative AI, NLP
""")

# ✅ Certifications
st.header("🎓 Certifications")
st.write("""
- Artificial Intelligence/ML (Microsoft Certificate -TEVTA)
- Deep Learning (iCodeGuru)
- Python
- CCNA, CCNP (CORVIT SYSTEM)
- MCSE
- Generative AI (iCodeGuru)
""")

# ✅ Core Concepts
st.header("🧠 Core Concepts")
st.write("""
- Linear Regression Model
- Neural Network Model
- Convolution Neural Network Model
- K-Means Clustering
- Recurrent Neural Network
- LSTM
- Transformers NLP
""")

st.markdown("---")

# ✅ Projects Section
st.header("📂 Projects")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.subheader("Final Year Project")
    st.write("**AI Resume Analyzer:** Created an AI-driven system to analyze and score resumes, assisting in the recruitment process by matching candidates with job requirements.")
    
    st.subheader("Generative AI Projects")
    st.write("""
    - **Visual Intelligence RAG System:** Gradio app for document Q&A with FAISS-based semantic search; text embedding via Hugging Face all-Minil.M-L6-v2; context-aware answer generation using LLaMA3-70B API.
    - **GenAI Chatbot:** Gradio + Groq LLaMA3-based chatbot with secure API handling, structured replies, and user interaction controls.
    - **Speech Diarization & Transcription App:** Gradio app using Whisper + pyAnnote for labeled transcription, with Groq's LLaMA3 generating summaries and recommended questions; includes visual speaker plot and metadata export.
    """)
    
    st.subheader("AI/ML Projects")
    st.write("""
    - **Next Word Predictor (LSTM):** NLP-based word prediction using tokenization, embeddings, and a trained language model for autocomplete/chat tools.
    - **Mango Variety Classification:** Random Forest Classification (Scikit-Learn, Pandas)
    - **Iris Flower Prediction:** Classification App (Streamlit, Scikit-Learn)
    - **Face Recognition:** Deep Learning (OpenCV, TensorFlow, Keras)
    - **House Price Prediction:** Regression (Scikit-Learn, Pandas)
    - **Student Performance Prediction:** Machine Learning (Scikit-Learn, Pandas)
    - **Salary Prediction:** Multi-Feature Regression (Scikit-Learn, TensorFlow)
    - **Used Car Price Prediction:** Regression (Scikit-Learn, Pandas)
    - **Voice-to-Text:** Speech Recognition (DeepSpeech, TensorFlow)
    """)
    
    st.subheader("YOLO Projects")
    st.write("""
    - **License Plate Detection & Recognition:** YOLOv8 (Real-time detection for traffic and security).
    - **Vehicle Parking Space Detection:** YOLOv8 (Real-time space occupancy monitoring with empty & filled spot accounting).
    """)
    
    st.subheader("Other Projects")
    st.write("""
    - **Optics Store** (Real-Time Running Software)
    - **Pharmacy Management**
    - **Messenger Application (Chat)**
    - **ATM System**
    - **Car Racing Game**
    - **Bricks Breaking Game**
    - **Media Player**
    - **Weather Application**
    """)

st.markdown("---")
st.write(f"Feel free to connect with me via [LinkedIn]({linkedin}) or explore my [GitHub]({github}) repositories!")
