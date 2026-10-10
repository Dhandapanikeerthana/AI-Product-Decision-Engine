import re
import streamlit as st

from decision_engine import make_decision


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Product Decision Engine",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- APP BACKGROUND ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(139, 92, 246, 0.10),
                transparent 30%
            ),
            #080b14;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 45px;
        padding-bottom: 50px;
    }


    /* ---------- HEADER ---------- */

    .hero-title {
        font-size: 44px;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin-bottom: 4px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #a5b4fc;
        margin-bottom: 8px;
    }

    .hero-description {
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 30px;
        max-width: 850px;
    }


    /* ---------- SECTION TITLE ---------- */

    .section-label {
        font-size: 13px;
        font-weight: 700;
        color: #a5b4fc;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 12px;
    }


    /* ---------- INPUT CARD ---------- */

    .input-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 35px;
    }


    /* ---------- RESULT CARDS ---------- */

    .metric-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 16px;
        padding: 22px;
        min-height: 125px;
    }

    .metric-label {
        color: #64748b;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 23px;
        font-weight: 750;
    }

    .score-value {
        font-size: 34px;
        font-weight: 800;
        color: #a5b4fc;
    }

    .priority-high {
        color: #fb7185;
        font-size: 27px;
        font-weight: 800;
    }

    .priority-medium {
        color: #fbbf24;
        font-size: 27px;
        font-weight: 800;
    }

    .priority-low {
        color: #4ade80;
        font-size: 27px;
        font-weight: 800;
    }


    /* ---------- SCORE BREAKDOWN ---------- */

    .breakdown-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        min-height: 105px;
    }

    .breakdown-label {
        color: #94a3b8;
        font-size: 12px;
        margin-bottom: 8px;
    }

    .breakdown-value {
        color: #f8fafc;
        font-size: 27px;
        font-weight: 800;
    }


    /* ---------- REASON ---------- */

    .reason-card {
        background: rgba(30, 41, 59, 0.65);
        border-left: 4px solid #818cf8;
        border-radius: 12px;
        padding: 20px;
        color: #cbd5e1;
        line-height: 1.7;
    }


    /* ---------- EVIDENCE ---------- */

    .evidence-item {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 9px;
        color: #cbd5e1;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #475569;
        font-size: 12px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid rgba(148, 163, 184, 0.1);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="hero-title">🤖 AI Product Decision Engine</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'RAG + GenAI-based Evidence-Driven Feature Prioritization'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-description">'
    'Turn customer feedback, bug reports, feature requests, and previous '
    'product decisions into evidence-backed product priorities.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT
# ============================================================

st.markdown(
    '<div class="section-label">🔎 Product Decision</div>',
    unsafe_allow_html=True
)

query = st.text_input(
    "Question",
    placeholder="Ask which feature should be prioritized...",
    label_visibility="collapsed"
)

analyze = st.button(
    "🚀 Analyze Decision",
    type="primary",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if not query.strip():

        st.warning("Please enter a product decision question.")

    else:

        with st.spinner("Analyzing product evidence..."):

            result = make_decision(query)


        # ====================================================
        # PARSE RESULT
        # ====================================================

        feature_match = re.search(
            r"Feature:\s*(.+)",
            result
        )

        priority_match = re.search(
            r"Priority:\s*(.+)",
            result
        )

        score_match = re.search(
            r"Priority Score:\s*(\d+)",
            result
        )

        customer_match = re.search(
            r"Customer Impact:\s*(\d+)",
            result
        )

        bug_match = re.search(
            r"Bug Severity:\s*(\d+)",
            result
        )

        demand_match = re.search(
            r"Feature Demand:\s*(\d+)",
            result
        )

        previous_match = re.search(
            r"Previous Decision:\s*(\d+)",
            result
        )


        feature = (
            feature_match.group(1).strip()
            if feature_match
            else "Unknown"
        )

        priority = (
            priority_match.group(1).strip().upper()
            if priority_match
            else "UNKNOWN"
        )

        score = (
            score_match.group(1).strip()
            if score_match
            else "0"
        )

        customer = (
            customer_match.group(1).strip()
            if customer_match
            else "0"
        )

        bug = (
            bug_match.group(1).strip()
            if bug_match
            else "0"
        )

        demand = (
            demand_match.group(1).strip()
            if demand_match
            else "0"
        )

        previous = (
            previous_match.group(1).strip()
            if previous_match
            else "0"
        )


        # ====================================================
        # RESULT HEADER
        # ====================================================

        st.divider()

        st.markdown(
            '<div class="section-label">📊 Decision Result</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # MAIN METRICS
        # ====================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Feature</div>
                    <div class="metric-value">{feature}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            priority_class = {
                "HIGH": "priority-high",
                "MEDIUM": "priority-medium",
                "LOW": "priority-low"
            }.get(
                priority,
                "metric-value"
            )

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Priority</div>
                    <div class="{priority_class}">
                        {priority}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Priority Score</div>
                    <div class="score-value">{score}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # SCORE BREAKDOWN
        # ====================================================

        st.markdown(
            '<div class="section-label" style="margin-top:35px;">'
            '📈 Score Breakdown'
            '</div>',
            unsafe_allow_html=True
        )


        b1, b2, b3, b4 = st.columns(4)


        breakdown = [
            (b1, "Customer Impact", customer),
            (b2, "Bug Severity", bug),
            (b3, "Feature Demand", demand),
            (b4, "Previous Decision", previous)
        ]


        for column, label, value in breakdown:

            with column:

                st.markdown(
                    f"""
                    <div class="breakdown-card">
                        <div class="breakdown-label">{label}</div>
                        <div class="breakdown-value">{value}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ====================================================
        # AI REASON
        # ====================================================

        reason_match = re.search(
            r"Reason:\s*(.*?)(?=Supporting Evidence:|$)",
            result,
            re.DOTALL
        )


        if reason_match:

            reason = reason_match.group(1).strip()

            st.markdown(
                '<div class="section-label" style="margin-top:35px;">'
                '🧠 AI Reason'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="reason-card">
                    {reason}
                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # SUPPORTING EVIDENCE
        # ====================================================

        evidence_match = re.search(
            r"Supporting Evidence:\s*(.*)",
            result,
            re.DOTALL
        )


        if evidence_match:

            evidence_text = evidence_match.group(1).strip()

            evidence_lines = [
                line.strip()
                for line in evidence_text.splitlines()
                if line.strip()
            ]


            st.markdown(
                '<div class="section-label" style="margin-top:35px;">'
                '📚 Supporting Evidence'
                '</div>',
                unsafe_allow_html=True
            )


            for evidence in evidence_lines:

                evidence = evidence.lstrip("- ").strip()

                st.markdown(
                    f"""
                    <div class="evidence-item">
                        ✓ &nbsp; {evidence}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        AI Product Decision Engine · RAG · FAISS · Llama 3.2 · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)