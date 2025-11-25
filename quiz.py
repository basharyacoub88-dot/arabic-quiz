import streamlit as st
import time
from datetime import datetime

# -------------------------
# Basic Styling
# -------------------------
st.set_page_config(page_title="Quiz App", layout="centered")

st.markdown(
    """
    <style>
    body {font-family: 'Arial';}
    .timer {
        font-size: 28px;
        font-weight: bold;
        color: #e63946;
        text-align:center;
        padding: 10px;
    }
    .question-box {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 0 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
        font-size: 22px;
    }
    .answer-btn button{
        width: 100%;
        padding: 12px;
        margin: 8px 0;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Quiz Data
# -------------------------
questions = [
    {
        "q": "ما هي عاصمة فرنسا؟",
        "options": ["برلين", "باريس", "مدريد", "روما"],
        "answer": 1,
    },
    {
        "q": "كم عدد الكواكب في المجموعة الشمسية؟",
        "options": ["7", "8", "9", "6"],
        "answer": 1,
    },
    {
        "q": "ما هو الحيوان الأسرع؟",
        "options": ["الفهد", "النمر", "الغزال", "الأسد"],
        "answer": 0,
    },
]

# -------------------------
# App State
# -------------------------
if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "finished" not in st.session_state:
    st.session_state.finished = False

TOTAL_TIME = 12   # seconds per question

# -------------------------
# Timer Logic (always counting)
# -------------------------
def get_time_left():
    elapsed = time.time() - st.session_state.start_time
    remaining = TOTAL_TIME - elapsed
    return max(0, int(remaining))

# -------------------------
# Quiz Finished
# -------------------------
if st.session_state.finished:
    st.markdown("<h2 style='text-align:center;'>🎉 النتيجة النهائية</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;'>نتيجتك: {st.session_state.score} / {len(questions)}</h3>", unsafe_allow_html=True)
    st.stop()

# -------------------------
# Timer Display
# -------------------------
time_left = get_time_left()
st.markdown(f"<div class='timer'>⏳ الوقت المتبقي: {time_left} ثانية</div>", unsafe_allow_html=True)

# If time runs out → auto next
if time_left == 0:
    st.session_state.index += 1
    st.session_state.start_time = time.time()
    if st.session_state.index >= len(questions):
        st.session_state.finished = True
    st.experimental_rerun()

# -------------------------
# Show Question
# -------------------------
current = questions[st.session_state.index]
st.markdown(f"<div class='question-box'>{current['q']}</div>", unsafe_allow_html=True)

# -------------------------
# Show Answers
# -------------------------
for i, opt in enumerate(current["options"]):
    if st.button(opt, key=f"opt_{i}"):
        if i == current["answer"]:
            st.session_state.score += 1

        st.session_state.index += 1
        st.session_state.start_time = time.time()

        if st.session_state.index >= len(questions):
            st.session_state.finished = True

        st.experimental_rerun()

# -------------------------
# Auto refresh every second for timer updates
# -------------------------
st.experimental_rerun()
