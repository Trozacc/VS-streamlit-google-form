"""
Custom CSS styles for the Vigyan Shaala Attendance app.
Injects a modern, branded light theme with green accents.
"""

import streamlit as st


def inject_styles():
    """Inject custom CSS into the Streamlit page."""
    st.markdown(
        """
        <style>
        /* ============================================================
           GOOGLE FONTS
           ============================================================ */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

        /* ============================================================
           CSS VARIABLES - LIGHT THEME
           ============================================================ */
        :root {
            --bg-primary: #FFFFFF;
            --bg-secondary: #F5F9F5;
            --bg-card: #FFFFFF;
            --bg-card-hover: #F0F7F0;
            --border-color: #99B898;
            --border-dark: #4A6E4A;
            --border-accent: #5CED73;
            --text-primary: #1A2E1A;
            --text-secondary: #4A6E4A;
            --text-muted: #6B8E6B;
            --accent-green: #5CED73;
            --accent-green-dark: #45D05B;
            --accent-teal: #2ECC71;
            --accent-teal-dark: #27AE60;
            --accent-red: #E74C3C;
            --accent-yellow: #F39C12;
            --accent-blue: #3498DB;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 14px rgba(0,0,0,0.1);
            --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
        }

        /* ============================================================
           GLOBAL PAGE & SCROLL CONTROL
           ============================================================ */
        html, body {
            min-height: 100vh !important;
            overflow-y: auto !important;
            margin: 0 !important;
            padding: 0 !important;
            font-family: 'Outfit', sans-serif !important;
            color: var(--text-primary) !important;
            background: var(--bg-primary) !important;
        }

        [data-testid="stAppViewContainer"] {
            background: var(--bg-primary) !important;
            min-height: 100vh !important;
            overflow-y: auto !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
            height: 0 !important;
            visibility: hidden !important;
        }

        .block-container {
            max-width: 800px !important;
            padding-top: 0.75rem !important;
            padding-bottom: 4rem !important;
            padding-left: 1.5rem !important;
            padding-right: 1.5rem !important;
        }

        /* ============================================================
           LOGO HEADER BACKGROUND (LIGHT GREEN)
           ============================================================ */
        .logo-header-bg {
            background: #5CED73;
            margin: -0.75rem calc(50% - 50vw) 0 calc(50% - 50vw);
            padding: 1rem 1.5rem;
            display: flex;
            justify-content: center;
            width: 100vw;
        }

        /* ============================================================
           COMPACT LOGO
           ============================================================ */
        .logo-container {
            display: flex;
            justify-content: center;
            padding: 0 0 0 0;
            margin-bottom: 2.8rem;
        }

        .logo-img {
            max-width: none;
            width: auto;
            height: 170px;
            filter: drop-shadow(0 2px 8px rgba(0,0,0,0.1));
            transition: transform 0.3s ease, filter 0.3s ease;
        }

        .logo-img:hover {
            transform: scale(1.03);
            filter: drop-shadow(0 4px 14px rgba(0,0,0,0.15));
        }

        /* ============================================================
           COMPACT FORM TITLE
           ============================================================ */
        .form-title-container {
            text-align: center;
            margin: 1.5rem 0 0.5rem 0;
        }

        .form-title {
            font-family: 'Outfit', sans-serif !important;
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: var(--text-primary) !important;
            margin: 0 !important;
            padding: 0 !important;
            letter-spacing: -0.3px;
            line-height: 1.25 !important;
        }

        .form-subtitle {
            color: var(--text-secondary) !important;
            font-size: 0.88rem !important;
            font-weight: 400;
            margin: 0.2rem 0 0 0 !important;
        }

        /* ============================================================
           SECTION INDICATOR
           ============================================================ */
        .section-indicator {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-bottom: 0.8rem;
        }

        .section-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: var(--border-dark);
            transition: all 0.3s ease;
        }

        .section-dot.active {
            background: var(--accent-green);
            box-shadow: 0 0 6px rgba(92,237,115,0.5);
            width: 24px;
            border-radius: 4px;
        }

        /* ============================================================
           FORM CARDS
           ============================================================ */
        .form-card {
            background: var(--bg-card);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-md);
            padding: 1.4rem 1.6rem;
            margin-bottom: 1rem;
            box-shadow: var(--shadow-sm);
        }

        .form-card-header {
            font-family: 'Outfit', sans-serif;
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.4rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .form-card-description {
            color: var(--text-secondary);
            font-size: 0.85rem;
            margin-bottom: 0;
            line-height: 1.45;
        }

        /* ============================================================
           STREAMLIT WIDGETS
           ============================================================ */
        [data-testid="stSelectbox"] {
            margin-bottom: 0.75rem !important;
        }

        [data-testid="stSelectbox"] > div > div {
            background: var(--bg-secondary) !important;
            border: 2px solid var(--border-dark) !important;
            border-radius: var(--radius-sm) !important;
            color: var(--text-primary) !important;
            min-height: 40px !important;
        }

        [data-testid="stSelectbox"] > div > div:focus-within {
            border-color: var(--accent-green) !important;
            box-shadow: 0 0 0 2px rgba(92,237,115,0.15) !important;
        }

        [data-testid="stSelectbox"] label {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 500 !important;
            color: var(--text-primary) !important;
            font-size: 0.9rem !important;
            margin-bottom: 0.25rem !important;
        }

        [data-testid="stSelectbox"] [data-baseweb="select"] > div:first-child {
            color: var(--text-primary) !important;
        }

        [data-testid="stSelectbox"] [data-baseweb="select"] [aria-selected="false"] {
            color: var(--text-primary) !important;
        }

        /* Radio Buttons (Strict Single-Line Horizontal) */
        [data-testid="stRadio"] {
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stRadio"] > div,
        [data-testid="stRadio"] [role="radiogroup"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 0.45rem !important;
            white-space: nowrap !important;
        }

        [data-testid="stRadio"] label[data-baseweb="radio"] {
            background: var(--bg-secondary) !important;
            border: 2px solid var(--border-dark) !important;
            border-radius: var(--radius-sm) !important;
            padding: 0.25rem 0.75rem !important;
            font-size: 0.8rem !important;
            white-space: nowrap !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            margin: 0 !important;
            flex-shrink: 0 !important;
            min-width: 70px !important;
            transition: all 0.15s ease !important;
            cursor: pointer !important;
            color: var(--text-primary) !important;
        }

        [data-testid="stRadio"] label[data-baseweb="radio"]:hover {
            border-color: var(--accent-green) !important;
            background: var(--bg-card-hover) !important;
        }

        /* ============================================================
           COLLEGE HEADER
           ============================================================ */
        .college-header {
            background: linear-gradient(135deg, rgba(92,237,115,0.15), rgba(46,204,113,0.1));
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-sm);
            padding: 0.75rem 1.2rem;
            margin-bottom: 0.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .college-name {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .student-count {
            background: var(--accent-green);
            color: #1A2E1A;
            padding: 0.25rem 0.75rem;
            border-radius: 14px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        /* ============================================================
           ATTENDANCE GRID HEADER
           ============================================================ */
        .attendance-header-bar {
            background: linear-gradient(135deg, #E8F5E8, #F0F7F0);
            padding: 0.6rem 0.9rem;
            border-radius: var(--radius-sm) var(--radius-sm) 0 0;
            border: 2px solid var(--border-dark);
            border-bottom: none;
            display: grid;
            grid-template-columns: 0.25fr 1.15fr 0.9fr 1.3fr;
            gap: 0.5rem;
            font-weight: 600;
            font-size: 0.78rem;
            color: var(--accent-teal);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* ============================================================
           STUDENT ROWS
           ============================================================ */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-color: var(--border-dark) !important;
            border-width: 2px !important;
            border-radius: 0 0 var(--radius-sm) var(--radius-sm) !important;
            background: var(--bg-card) !important;
        }

        .student-number {
            color: var(--text-muted);
            font-weight: 600;
            font-size: 0.82rem;
        }

        .student-name {
            color: var(--text-primary);
            font-weight: 500;
            font-size: 0.88rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .student-stream {
            color: var(--text-secondary);
            font-size: 0.8rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* Status column radio button alignment */
        [data-testid="column"]:has([data-testid="stRadio"]) {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* ============================================================
           SUMMARY STATS
           ============================================================ */
        .stats-row {
            display: flex;
            gap: 0.6rem;
            margin: 0.75rem 0 0.5rem 0;
        }

        .stat-card {
            flex: 1;
            background: var(--bg-card);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-sm);
            padding: 0.5rem 0.6rem;
            text-align: center;
        }

        .stat-value {
            font-size: 1.25rem;
            font-weight: 700;
            line-height: 1.1;
        }

        .stat-label {
            font-size: 0.72rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.3px;
            margin-top: 0.2rem;
        }

        .stat-present .stat-value { color: #27AE60; }
        .stat-absent .stat-value { color: #E74C3C; }
        .stat-total .stat-value { color: var(--accent-teal); }
        .stat-unmarked .stat-value { color: #F39C12; }

        /* ============================================================
           BUTTONS
           ============================================================ */
        .stButton > button {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            border-radius: var(--radius-sm) !important;
            padding: 0.5rem 1.2rem !important;
            min-height: 38px !important;
            transition: all 0.2s ease !important;
            border: 1px solid transparent !important;
        }

        .stButton > button[kind="primary"],
        div[data-testid="stForm"] .stButton > button {
            background: linear-gradient(135deg, var(--accent-green), var(--accent-green-dark)) !important;
            color: #1A2E1A !important;
            box-shadow: 0 2px 8px rgba(92,237,115,0.3) !important;
        }

        .stButton > button[kind="primary"]:hover {
            box-shadow: 0 4px 14px rgba(92,237,115,0.4) !important;
            transform: translateY(-1px) !important;
        }

        .stButton > button[kind="secondary"] {
            background: var(--bg-secondary) !important;
            border: 2px solid var(--border-dark) !important;
            color: var(--text-primary) !important;
        }

        .stButton > button[kind="secondary"]:hover {
            border-color: var(--accent-green) !important;
            color: var(--accent-teal) !important;
        }

        /* ============================================================
           SUCCESS BOX
           ============================================================ */
        .success-box {
            background: rgba(46,204,113,0.1);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            text-align: center;
            margin: 1.2rem 0;
        }

        .success-box h3 {
            color: #27AE60;
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
        }

        .success-box p {
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin: 0;
        }

        /* ============================================================
           SCROLLBARS
           ============================================================ */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }

        ::-webkit-scrollbar-track {
            background: var(--bg-primary);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 3px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--accent-green);
        }

        /* ============================================================
           HIDE STREAMLIT DEFAULTS
           ============================================================ */
        #MainMenu { visibility: hidden; display: none; }
        footer { visibility: hidden; display: none; }
        header[data-testid="stHeader"] { visibility: hidden; display: none; }
        [data-testid="stDecoration"] { display: none; }

        /* ============================================================
           RESPONSIVE BREAKPOINTS
           ============================================================ */

        /* Tablet Landscape (1024px and below) */
        @media (max-width: 1024px) {
            .block-container {
                max-width: 100% !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                padding-top: 0.5rem !important;
            }

            .logo-img {
                height: 150px;
            }

            .form-title {
                font-size: 1.3rem !important;
            }

            .form-subtitle {
                font-size: 0.8rem !important;
            }

            .attendance-header-bar {
                grid-template-columns: 0.3fr 1.2fr 1fr 1.5fr;
                font-size: 0.7rem;
                padding: 0.5rem 0.6rem;
            }

            .form-card {
                padding: 1.2rem 1.2rem;
            }

            .stat-value {
                font-size: 1.1rem;
            }
        }

        /* Tablet Portrait (768px and below) */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 0.75rem !important;
                padding-right: 0.75rem !important;
            }

            .logo-header-bg {
                padding: 0.75rem 1rem;
            }

            .logo-img {
                height: 130px;
            }

            .form-title {
                font-size: 1.15rem !important;
            }

            .form-subtitle {
                font-size: 0.75rem !important;
            }

            .logo-container {
                margin-bottom: 1.5rem;
            }

            [data-testid="stSelectbox"] > div > div {
                min-height: 44px !important;
                font-size: 0.95rem !important;
            }

            [data-testid="stSelectbox"] label {
                font-size: 0.85rem !important;
            }

            .college-header {
                flex-direction: column;
                gap: 0.5rem;
                text-align: center;
                padding: 0.75rem 1rem;
            }

            .student-count {
                font-size: 0.75rem;
                padding: 0.2rem 0.6rem;
            }

            .attendance-header-bar {
                display: none;
            }

            [data-testid="column"] {
                padding: 0 !important;
            }

            .student-number,
            .student-name,
            .student-stream {
                font-size: 0.8rem;
            }

            [data-testid="stRadio"] > div,
            [data-testid="stRadio"] [role="radiogroup"] {
                gap: 0.3rem !important;
            }

            [data-testid="stRadio"] label[data-baseweb="radio"] {
                padding: 0.3rem 0.5rem !important;
                font-size: 0.75rem !important;
                min-width: 60px !important;
            }

            .stats-row {
                flex-wrap: wrap;
                gap: 0.4rem;
            }

            .stat-card {
                flex: 1 1 calc(50% - 0.2rem);
                min-width: 120px;
                padding: 0.5rem 0.4rem;
            }

            .stat-value {
                font-size: 1rem;
            }

            .stat-label {
                font-size: 0.65rem;
            }

            .stButton > button {
                font-size: 0.85rem !important;
                padding: 0.55rem 1rem !important;
                min-height: 42px !important;
            }

            .success-box {
                padding: 1.2rem;
            }

            .success-box h3 {
                font-size: 1.1rem;
            }

            .success-box p {
                font-size: 0.85rem;
            }
        }

        /* Mobile Landscape (480px and below) */
        @media (max-width: 480px) {
            .block-container {
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
                padding-bottom: 2rem !important;
            }

            .logo-header-bg {
                margin: -0.5rem calc(50% - 50vw) 0 calc(50% - 50vw) !important;
                padding: 0.6rem 0.75rem;
            }

            .logo-img {
                height: 110px;
            }

            .form-title {
                font-size: 1rem !important;
            }

            .form-subtitle {
                font-size: 0.7rem !important;
            }

            .logo-container {
                margin-bottom: 1rem;
            }

            .form-card {
                padding: 1rem 0.8rem;
                border-radius: var(--radius-sm);
            }

            .form-card-header {
                font-size: 0.95rem;
            }

            .form-card-description {
                font-size: 0.78rem;
            }

            [data-testid="stSelectbox"] > div > div {
                min-height: 44px !important;
                font-size: 0.9rem !important;
            }

            .college-header {
                padding: 0.6rem 0.75rem;
            }

            .college-name {
                font-size: 0.9rem;
            }

            .student-number,
            .student-name,
            .student-stream {
                font-size: 0.75rem;
            }

            [data-testid="stVerticalBlockBorderWrapper"] > div {
                padding: 0.4rem 0.2rem !important;
            }

            [data-testid="stRadio"] label[data-baseweb="radio"] {
                padding: 0.25rem 0.4rem !important;
                font-size: 0.7rem !important;
                min-width: 55px !important;
            }

            .stats-row {
                gap: 0.3rem;
            }

            .stat-card {
                flex: 1 1 100%;
                min-width: 100%;
            }

            .stButton > button {
                width: 100% !important;
                font-size: 0.85rem !important;
                padding: 0.6rem 1rem !important;
            }

            .btn_col1, .btn_col2 {
                width: 100% !important;
            }
        }

        /* Mobile Portrait (320px and below) */
        @media (max-width: 320px) {
            .block-container {
                padding-left: 0.4rem !important;
                padding-right: 0.4rem !important;
            }

            .logo-img {
                height: 95px;
            }

            .form-title {
                font-size: 0.9rem !important;
            }

            .logo-container {
                margin-bottom: 0.75rem;
            }
        }

        /* Touch-friendly adjustments */
        @media (hover: none) and (pointer: coarse) {
            .stButton > button {
                min-height: 44px !important;
            }

            [data-testid="stSelectbox"] > div > div {
                min-height: 44px !important;
            }

            [data-testid="stRadio"] label[data-baseweb="radio"] {
                min-height: 40px !important;
                min-width: 70px !important;
            }
        }

        /* High DPI / Retina displays */
        @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
            .logo-img {
                image-rendering: -webkit-optimize-contrast;
                image-rendering: crisp-edges;
            }
        }

        /* Landscape orientation adjustments */
        @media (orientation: landscape) and (max-height: 600px) {
            .block-container {
                padding-top: 0.25rem !important;
                padding-bottom: 1.5rem !important;
            }

            .logo-img {
                height: 100px;
            }

            .logo-container {
                margin-bottom: 1rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )