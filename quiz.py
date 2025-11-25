import streamlit as st
import time

# -----------------------------
# قائمة الأسئلة
# -----------------------------
QUESTIONS = [
    {"question": "ما هو الكوكب الذي يُعرف بالكوكب الأحمر؟", 
     "choices": ["الزهرة", "المريخ", "عطارد", "المشتري"], 
     "answer": "المريخ"},
    
    {"question": "ما هو أسرع حيوان بري؟", 
     "choices": ["الفهد", "الأسد", "الغزال", "الذئب"], 
     "answer": "الفهد"},
    
    {"question": "في أي قارة يقع نهر الأمازون؟", 
     "choices": ["أفريقيا", "آسيا", "أمريكا الجنوبية", "أوروبا"], 
     "answer": "أمريكا الجنوبية"},
    
    {"question": "كم عدد أركان الإسلام؟", 
     "choices": ["3", "4", "5", "6"], 
     "answer": "5"},
    
    {"question": "ما هي الدولة العربية الأكبر مساحة؟", 
     "choices": ["السعودية", "الجزائر", "السودان", "مصر"], 
     "answer": "الجزائر"},
    
    {"question": "ما هي اللغة الأكثر انتشاراً في العالم؟", 
     "choices": ["الإنجليزية", "العربية", "الإسبانية", "الصينية"], 
     "answer": "الصينية"},
    
    {"question": "كم يساوي مجموع زوايا المثلث؟", 
     "choices": ["120", "360", "90", "180"], 
     "answer": "180"},
    
    {"question": "من هو مؤسس علم الجبر؟", 
     "choices": ["الخوارزمي", "ابن سينا", "ابن الهيثم", "ابن رشد"], 
     "answer": "الخوارزمي"},
    
    {"question": "من هو أول من مشى على سطح القمر؟", 
     "choices": ["نيل آرمسترونغ", "يوري غاغارين", "مايكل كولينز", "ألدرين"], 
     "answer": "نيل آرمسترونغ"},
    
    {"question": "ما هي أكبر قارات العالم؟", 
     "choices": ["أفريقيا", "آسيا", "أوروبا", "أمريكا الشمالية"], 
     "answer": "آسيا"}
]

TOTAL_TIME = 180  # 3 دقائق

# -----------------------------
# تهيئة حالة الجلسة
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = 0

# -----------------------------
# شاشة البداية
# -----------------------------
if not st.session_state.started:
    st.title("📘 اختبار الثقافة العامة")

    if st.button("🚀 ابدأ الاختبار", use_container_width=True):
        st.session_state.started = True
        st.session_state.start_time = time.time()
        st.rerun()

    st.stop()

# -----------------------------
# المؤقت
# -----------------------------
elapsed = int(time.time() - st.session_state.start_time)
remaining = TOTAL_TIME - elapsed

if remaining <= 0:
    st.session_state.index = len(QUESTIONS)

st.sidebar.title("⏳ الوقت المتبقي")
st.sidebar.success(f"{remaining//60:02d}:{remaining%60:02d}")

# -----------------------------
# انتهاء الاختبار
# -----------------------------
if st.session_state.index >= len(QUESTIONS):
    st.title("🎉 انتهى الاختبار!")
    st.subheader(f"⭐ نتيجتك: {st.session_state.score} / {len(QUESTIONS)}")

    if st.button("🔄 إعادة المحاولة", use_container_width=True):
        st.session_state.started = False
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.start_time = 0
        st.rerun()

    st.stop()

# -----------------------------
# عرض السؤال
# -----------------------------
q = QUESTIONS[st.session_state.index]

st.header(f"❓ السؤال {st.session_state.index + 1}")
st.write(q["question"])

choice = st.radio("اختر الإجابة:", q["choices"], index=None)

if st.button("التالي ➡", use_container_width=True):
    if choice == q["answer"]:
        st.session_state.score += 1
    st.session_state.index += 1
    st.rerun()
