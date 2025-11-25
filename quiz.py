import streamlit as st
import time

# -----------------------------
# قائمة الأسئلة (10 أسئلة متنوعة)
# -----------------------------
QUESTIONS = [
    {"id": 1, "question": "ما هو الكوكب الذي يُعرف بالكوكب الأحمر؟", "choices": ["الزهرة", "المريخ", "عطارد", "المشتري"], "answer": "المريخ", "explanation": "لونه الأحمر بسبب أكسيد الحديد."},
    {"id": 2, "question": "ما هو أسرع حيوان بري؟", "choices": ["الفهد", "الأسد", "الغزال", "الذئب"], "answer": "الفهد", "explanation": "تصل سرعته إلى 110 كم/ساعة."},
    {"id": 3, "question": "في أي قارة يقع نهر الأمازون؟", "choices": ["أفريقيا", "آسيا", "أمريكا الجنوبية", "أوروبا"], "answer": "أمريكا الجنوبية", "explanation": "يعد من أطول أنهار العالم."},
    {"id": 4, "question": "كم عدد أركان الإسلام؟", "choices": ["3", "4", "5", "6"], "answer": "5", "explanation": "الشهادتان، الصلاة، الزكاة، الصوم، الحج."},
    {"id": 5, "question": "ما هي الدولة العربية الأكبر مساحة؟", "choices": ["السعودية", "الجزائر", "السودان", "مصر"], "answer": "الجزائر", "explanation": "مساحتها 2.38 مليون كم²."},
    {"id": 6, "question": "ما هي اللغة الأكثر انتشاراً في العالم؟", "choices": ["الإنجليزية", "العربية", "الإسبانية", "الصينية"], "answer": "الصينية", "explanation": "لغة الماندرين يتحدث بها أكثر من مليار شخص."},
    {"id": 7, "question": "كم يساوي مجموع زوايا المثلث؟", "choices": ["120", "360", "90", "180"], "answer": "180", "explanation": "قانون ثابت في الهندسة."},
    {"id": 8, "question": "من هو مؤسس علم الجبر؟", "choices": ["الخوارزمي", "ابن سينا", "ابن الهيثم", "ابن رشد"], "answer": "الخوارزمي", "explanation": "له كتاب 'الجبر والمقابلة'."},
    {"id": 9, "question": "من هو أول من مشى على سطح القمر؟", "choices": ["نيل آرمسترونغ", "يوري غاغارين", "مايكل كولينز", "ألدرين"], "answer": "نيل آرمسترونغ", "explanation": "كان ذلك عام 1969."},
    {"id": 10, "question": "ما هي أكبر قارات العالم؟", "choices": ["أفريقيا", "آسيا", "أوروبا", "أمريكا الشمالية"], "answer": "آسيا", "explanation": "مساحتها 44.5 مليون كم²."}
]

st.set_page_config(page_title="اختبار الثقافة العامة", layout="centered")

# صفحة البداية
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown("""
        <div style='text-align:center; margin-top:40px;'>
            <h1 style='font-size:36px;'>📘 اختبار الثقافة العامة</h1>
            <p style='font-size:20px; color:#555;'>اختبار ممتع مكوّن من 10 أسئلة متنوعة</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 ابدأ الاختبار", use_container_width=True):
        st.session_state.started = True
        st.rerun()

    st.stop()

# دعم الهواتف
st.markdown("""
<style>
@media (max-width: 600px) {
    .block-container { padding-left: 10px !important; padding-right: 10px !important; }
    h1, h2, h3 { text-align: center !important; font-size: 22px !important; }
    .stButton>button { width: 100% !important; font-size: 18px !important; padding: 10px; }
}
</style>
""", unsafe_allow_html=True)

# حالة الجلسة
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "finished" not in st.session_state:
    st.session_state.finished = False

# المؤقت
TOTAL_TIME = 180
elapsed = int(time.time() - st.session_state.start_time)

# تحديث كل ثانية
st.markdown("""
<meta http-equiv="refresh" content="1">
""", unsafe_allow_html=True)

time_left = TOTAL_TIME - elapsed
if time_left <= 0:
    st.session_state.finished = True

# شريط التقدم
progress = (st.session_state.q_index + 1) / len(QUESTIONS)

st.markdown(f"""
<div style='width:100%; background:#e0e0e0; border-radius:25px; height:18px;'>
  <div style='width:{progress*100}%; height:100%; background:linear-gradient(90deg, #4CAF50, #2E7D32); border-radius:25px;'></div>
</div>
<p style='text-align:center; font-size:16px; margin-top:5px;'>السؤال {st.session_state.q_index + 1} من {len(QUESTIONS)}</p>
""", unsafe_allow_html=True)

# مؤقت دائري
st.markdown(
    """
    <div style='display:flex; justify-content:center; margin-top:10px;'>
        <div style='
            width:120px;
            height:120px;
            border-radius:50%;
            border:10px solid #ddd;
            border-top-color:#4CAF50;
            animation: spin 1s linear infinite;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:22px;
            font-weight:bold;
            color:#333;'>
                TIMELEFT_REPLACE
        </div>
    </div>
    <style>
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    </style>
    """.replace("TIMELEFT_REPLACE", str(time_left)),
    unsafe_allow_html=True,
)

st.sidebar.success(f"⏳ الوقت المتبقي: {time_left//60:02d}:{time_left%60:02d}")
st.sidebar.info(f"📊 السؤال: {st.session_state.q_index + 1} / {len(QUESTIONS)}")
st.sidebar.warning(f"⭐ نتيجتك: {st.session_state.score}")

# انتهاء الاختبار
if st.session_state.finished or st.session_state.q_index >= len(QUESTIONS):
    st.markdown("## 🎉 انتهى الاختبار!")
    st.markdown(f"### نتيجتك النهائية: **{st.session_state.score} / {len(QUESTIONS)}**")

    if st.session_state.score == len(QUESTIONS):
        st.success("🎯 ممتاز! إجاباتك كلها صحيحة!")
    elif st.session_state.score >= len(QUESTIONS) / 2:
        st.info("🙂 أداء جيد، استمر!")
    else:
        st.error("😕 تحتاج المزيد من التدريب.")

    if st.button("🔄 إعادة المحاولة", use_container_width=True):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.session_state.finished = False
        st.rerun()

    st.stop()

# عرض السؤال الحالي
question = QUESTIONS[st.session_state.q_index]
st.markdown(f"## ❓ {question['question']}")

choice = st.radio("اختر الإجابة:", question["choices"])
