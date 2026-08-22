import streamlit as st

from rag_pipeline import ask_question
from eligibility import check_eligibility

st.set_page_config(
    page_title="GovAssist AI",
    page_icon="🇮🇳",
    layout="wide"
)

# ---------- CUSTOM CSS ---------- #

st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom right, #f8fbff, #eef4ff);
}

.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
}

.scheme-card {
    background: black;
    padding: 20px;
    border-radius: 16px;
    margin-top: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border-left: 6px solid #2563eb;
}

.stButton > button {
    width: 100%;
    height: 3.2em;
    border-radius: 12px;
    border: none;
    background-color: #2563eb;
    color: white;
    font-size: 16px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

.footer {
    text-align: center;
    padding: 20px;
    color: gray;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ---------- #

st.markdown("""
<div class="hero">
    <h1>🇮🇳 GovAssist AI</h1>
    <p>
        AI Powered Government Scheme Recommendation System
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- TABS ---------- #

tab1, tab2 = st.tabs([
    "🎯 Eligibility Checker",
    "💬 Ask Questions"
])

# ---------- TAB 1 ---------- #

with tab1:

    st.subheader("Find Government Schemes You May Be Eligible For")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=21
        )

        occupation = st.selectbox(
            "Occupation",
            [
                "student",
                "farmer",
                "artisan",
                "vendor"
            ]
        )

    with col2:

        income = st.number_input(
            "Annual Income (₹)",
            value=100000
        )

    if st.button("🔍 Find Eligible Schemes"):

        schemes = check_eligibility(
            age,
            income,
            occupation
        )

        if schemes:

            st.success(
                f"Found {len(schemes)} matching schemes"
            )

            for scheme in schemes:

                st.markdown(
                    "<div class='scheme-card'>",
                    unsafe_allow_html=True
                )

                st.subheader(f"📌 {scheme}")

                try:

                    with st.spinner(
                        "Generating AI explanation..."
                    ):

                        answer = ask_question(
                            f"""
                            Explain eligibility,
                            benefits,
                            and purpose of {scheme}
                            """
                        )

                    st.write(answer)

                except Exception:

                    st.warning("""
                    Daily AI quota limit reached.

                    Please try again tomorrow or
                    continue using the eligibility checker.
                    """)

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

        else:

            st.error(
                "No matching schemes found."
            )

# ---------- TAB 2 ---------- #

with tab2:

    st.subheader(
        "Ask Questions About Government Schemes"
    )

    query = st.text_input(
        "Example: Who is eligible for PM Kisan?"
    )

    if st.button("🤖 Ask AI"):

        if query:

            try:

                with st.spinner(
                    "Searching documents..."
                ):

                    answer = ask_question(query)

                st.markdown(
                    f"""
                    <div class='scheme-card'>
                    {answer}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception:

                st.warning("""
                AI service is temporarily unavailable
                because the daily free quota has been exhausted.

                Please try again tomorrow.
                """)

