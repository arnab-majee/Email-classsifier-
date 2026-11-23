import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model= pickle.load(open('model.pkl', 'rb'))

st.set_page_config(
    page_title="SpamGuard | Email & SMS Security",
    page_icon="🛡️",
    layout="wide"
)


# == WEBSITE DESIGN ==

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, #172554 0%, transparent 40%),
        radial-gradient(ellipse at 90% 90%, #312e81 0%, transparent 35%),
        #070b16;
    font-family: 'Inter', sans-serif;
    color: #ffffff;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.brand {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px 0 30px 0;
}

.brand-icon {
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    border-radius: 16px;
    font-size: 27px;
    box-shadow: 0 0 25px #3b82f655;
}

.brand-name {
    font-size: 25px;
    font-weight: 900;
    color: white;
}

.brand-sub {
    font-size: 11px;
    color: #94a3b8;
    letter-spacing: 2px;
}

.hero {
    text-align: center;
    padding: 35px 15px;
}

.hero-tag {
    display: inline-block;
    padding: 8px 17px;
    border: 1px solid #3b82f666;
    border-radius: 30px;
    color: #93c5fd;
    background: #1e3a8a33;
    font-size: 12px;
    letter-spacing: 2px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 900;
    margin: 20px 0 10px;
    background: linear-gradient(90deg,#ffffff,#93c5fd,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #94a3b8;
    font-size: 16px;
}

.stTextInput input {
    background-color: #0b1220 !important;
    color: white !important;
    border: 1px solid #475569 !important;
    border-radius: 12px !important;
    min-height: 48px;
}

.stTextInput input:focus {
    border-color: #60a5fa !important;
    box-shadow: 0 0 15px #2563eb44 !important;
}

.stButton button {
    width: 100%;
    min-height: 52px;
    border-radius: 12px;
    border: 1px solid #6366f1;
    background: linear-gradient(100deg,#2563eb,#7c3aed);
    color: white;
    font-size: 16px;
    font-weight: 800;
    transition: 0.3s;
}

.stButton button:hover {
    box-shadow: 0 0 25px #6366f188;
    transform: translateY(-3px);
}

div[data-testid="stAlert"] {
    border-radius: 16px;
    padding: 18px;
    border: 1px solid #475569;
}

label, .stMarkdown p {
    color: #cbd5e1;
}

.footer {
    border-top: 1px solid #263449;
    margin-top: 60px;
    padding: 25px 5px;
    text-align: center;
    color: #64748b;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# ================= END PREMIUM DESIGN =================

st.title("Email or SMS Classifier")

# == WEBSITE HEADER ==

st.markdown("""
<div class="brand">
    <div class="brand-icon">🛡️</div>
    <div>
        <div class="brand-name">SpamGuard</div>
        <div class="brand-sub">MESSAGE SECURITY SYSTEM</div>
    </div>
</div>

<div class="hero">
    <span class="hero-tag">EMAIL & SMS PROTECTION</span>
    <h1>Stay Safe. Stay Protected.</h1>
    <p>Identify unwanted messages with your spam detection system.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# == END HEADER ==
st.subheader("🔍 Check Your Message")
input_sms= st.text_input("Enter Email or SMS")

#preprocess
#vectorize
#predict
#Display
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

if st.button("Predict"):
    #preprocess
    transformed_text = transform_text(input_sms)
    #vectorize
    vector_input = tfidf.transform([transformed_text])
    #predict
    result = model.predict (vector_input)
    #Display
    if result == 1:
        st.title("Spam")
    else:
        st.title("Not Spam")

# == WEBSITE FOOTER ==

st.markdown("""
<div class="footer">
    <h3 style="color:#93c5fd;">🛡️ SpamGuard</h3>
    <p>Email & SMS Spam Detection System</p>
    <p>Designed & Developed by ARM</p>
    <p>Python • Streamlit • Machine Learning</p>
    <p>© 2026 SpamGuard. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)

# == END FOOTER ==