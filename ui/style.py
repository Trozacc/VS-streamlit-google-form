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
            --accent-green: #69ab4a;
            --accent-green-dark: #5a963f;
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
           HIDE STREAMLIT HEADING ANCHORS (app-wide)
           ============================================================ */
        /* Hide the link icon that appears on heading hover */
        h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
            display: none !important;
        }
        /* Hide the header action elements (anchor link buttons) */
        [data-testid="stHeaderActionElements"] {
            display: none !important;
        }
        /* Hide markdown heading anchors */
        .markdown-text-container h1 a,
        .markdown-text-container h2 a,
        .markdown-text-container h3 a,
        .markdown-text-container h4 a,
        .markdown-text-container h5 a,
        .markdown-text-container h6 a {
            display: none !important;
        }

/* ============================================================
           ADMIN DASHBOARD TITLE CENTERING
           ============================================================ */
        .admin-dashboard-header {
            text-align: center !important;
        }
        .admin-dashboard-header > div {
            display: inline-block !important;
            text-align: center !important;
        }
        .admin-dashboard-title {
            text-align: center !important;
            width: 100% !important;
        }
        .admin-dashboard-subtitle {
            text-align: center !important;
            width: 100% !important;
        }

        /* ============================================================
           HEADER COLUMN LAYOUT - Button in right column
           ============================================================ */
        /* Right column button styling */
        [data-testid="column"]:last-child .stButton > button {
            width: auto !important;
            min-width: 140px;
            max-width: 180px;
            white-space: nowrap;
        }

        /* On mobile: shrink button */
        @media (max-width: 768px) {
            [data-testid="column"]:last-child .stButton > button {
                min-width: 120px;
                padding: 0.4rem 0.8rem !important;
                font-size: 0.8rem !important;
            }
        }

        /* ============================================================
           LOGO HEADER BACKGROUND (LIGHT GREEN)
           ============================================================ */
        .logo-header-bg {
            background: #2d4a6a;
            margin: -0.75rem calc(50% - 50vw) 0 calc(50% - 50vw);
            padding: 0.5rem 1.5rem;
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
            margin-bottom: 1.5rem;
        }

        .logo-img {
            max-width: none;
            width: auto;
            height: 120px;
            border-radius: 12px;
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
            padding: 0.25rem 0.6rem !important;
            font-size: 0.78rem !important;
            white-space: nowrap !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            margin: 0 !important;
            flex-shrink: 0 !important;
            min-width: 65px !important;
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
            color: #FFFFFF;
            padding: 0.25rem 0.75rem;
            border-radius: 14px;
            font-size: 0.8rem;
            font-weight: 600;
        }

/* ============================================================
           ATTENDANCE GRID HEADER (CSS Grid - matches st.columns)
           ============================================================ */
        .attendance-header-bar {
            background: linear-gradient(135deg, #E8F5E8, #F0F7F0);
            border: 2px solid var(--border-dark);
            border-bottom: none;
            border-radius: var(--radius-sm) var(--radius-sm) 0 0;
            display: grid;
            gap: 0.5rem;
            padding: 0.75rem 0.9rem;
            font-weight: 600;
            font-size: 0.78rem;
            color: var(--accent-teal);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            align-items: center;
            margin-bottom: -1px; /* seamless join with roster box */
        }

        .attendance-header-cell {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
        }

        /* ============================================================
           STUDENT ROWS (matching st.columns layout)
           ============================================================ */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-color: var(--border-dark) !important;
            border-width: 2px !important;
            border-radius: 0 0 var(--radius-sm) var(--radius-sm) !important;
            background: var(--bg-card) !important;
        }

        /* Ensure columns in rows align with header - use same flex layout */
        [data-testid="stVerticalBlockBorderWrapper"] > div:has([data-testid="column"]) {
            display: flex !important;
            gap: 0.5rem !important;
            align-items: center !important;
            padding: 0.5rem 0.9rem !important;
            border-bottom: 1px solid var(--border-color) !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] > div:has([data-testid="column"]):last-child {
            border-bottom: none !important;
        }

        .student-number {
            color: var(--text-muted);
            font-weight: 600;
            font-size: 0.82rem;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
        }

        .student-name {
            color: var(--text-primary);
            font-weight: 500;
            font-size: 0.88rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            height: 100%;
            padding-left: 0.5rem;
        }

        .student-stream {
            color: var(--text-secondary);
            font-size: 0.8rem;
            white-space: normal;
            word-wrap: break-word;
            overflow-wrap: break-word;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            padding: 0.25rem 0.5rem;
        }

        /* Radio Buttons - Custom Styled for Visibility & Alignment */
        [data-testid="stRadio"] {
            margin: 0 !important;
            padding: 0 !important;
            width: 100% !important;
        }

        [data-testid="stRadio"] > div,
        [data-testid="stRadio"] [role="radiogroup"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            align-items: center !important;
            justify-content: flex-start !important;
            gap: 0.75rem !important;
            white-space: nowrap !important;
            width: 100% !important;
            padding-right: 1rem !important;
        }

        /* Hide native radio input, we'll style the label */
        [data-testid="stRadio"] input[type="radio"] {
            position: absolute !important;
            opacity: 0 !important;
            width: 0 !important;
            height: 0 !important;
            pointer-events: none !important;
        }

        /* Style the label as the visible radio button */
        [data-testid="stRadio"] label[data-baseweb="radio"] {
            background: var(--bg-card) !important;
            border: 3px solid #2D4A2D !important;
            border-radius: var(--radius-sm) !important;
            padding: 0.375rem 0.875rem !important;
            font-size: 0.82rem !important;
            font-weight: 700 !important;
            white-space: nowrap !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 0.375rem !important;
            margin: 0 !important;
            flex-shrink: 0 !important;
            min-width: 84px !important;
            min-height: 38px !important;
            transition: all 0.18s ease !important;
            cursor: pointer !important;
            color: var(--text-primary) !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
            position: relative !important;
        }

        /* Custom radio indicator (circle) */
        [data-testid="stRadio"] label[data-baseweb="radio"]::before {
            content: "" !important;
            width: 20px !important;
            height: 20px !important;
            border: 4px solid #2D4A2D !important;
            border-radius: 50% !important;
            background: var(--bg-card) !important;
            flex-shrink: 0 !important;
            transition: all 0.18s ease !important;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.05) !important;
        }

        /* Hover state */
        [data-testid="stRadio"] label[data-baseweb="radio"]:hover {
            border-color: var(--accent-green) !important;
            background: var(--bg-card-hover) !important;
        }

        [data-testid="stRadio"] label[data-baseweb="radio"]:hover::before {
            border-color: var(--accent-green) !important;
            box-shadow: 0 0 0 3px rgba(105, 171, 74, 0.15) !important;
        }

        /* Selected state - Present (value="Present") - GREEN #69ab4a */
        [data-testid="stRadio"] input[type="radio"][value="Present"]:checked + div label[data-baseweb="radio"],
        [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[type="radio"][value="Present"]:checked) {
            border-color: #69ab4a !important;
            background: linear-gradient(135deg, rgba(105,171,74,0.12), rgba(105,171,74,0.05)) !important;
            color: #5a963f !important;
        }

        [data-testid="stRadio"] input[type="radio"][value="Present"]:checked + div label[data-baseweb="radio"]::before,
        [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[type="radio"][value="Present"]:checked)::before {
            border-color: #69ab4a !important;
            background: #69ab4a !important;
            box-shadow: 0 0 0 3px rgba(105, 171, 74, 0.2) !important;
        }

        /* Selected state - Absent (value="Absent") - RED #ff0000 */
        [data-testid="stRadio"] input[type="radio"][value="Absent"]:checked + div label[data-baseweb="radio"],
        [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[type="radio"][value="Absent"]:checked) {
            border-color: #ff0000 !important;
            background: linear-gradient(135deg, rgba(255,0,0,0.12), rgba(255,0,0,0.05)) !important;
            color: #cc0000 !important;
        }

        [data-testid="stRadio"] input[type="radio"][value="Absent"]:checked + div label[data-baseweb="radio"]::before,
        [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[type="radio"][value="Absent"]:checked)::before {
            border-color: #ff0000 !important;
            background: #ff0000 !important;
            box-shadow: 0 0 0 3px rgba(255, 0, 0, 0.2) !important;
        }

        /* Selected state inner dot - Present (white dot) */
        [data-testid="stRadio"] input[type="radio"][value="Present"]:checked + div label[data-baseweb="radio"]::after,
        [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[type="radio"][value="Present"]:checked)::after {
            content: "" !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            width: 10px !important;
            height: 10px !important;
            border-radius: 50% !important;
            background: white !important;
            z-index: 1 !important;
        }

        /* Selected state inner dot - Absent (white dot) */
        [data-testid="stRadio"] input[type="radio"][value="Absent"]:checked + div label[data-baseweb="radio"]::after,
        [data-testid="stRadio"] label[data-baseweb="radio"]:has(input[type="radio"][value="Absent"]:checked)::after {
            content: "" !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            width: 10px !important;
            height: 10px !important;
            border-radius: 50% !important;
            background: white !important;
            z-index: 1 !important;
        }

        /* Focus visible for accessibility */
        [data-testid="stRadio"] input[type="radio"]:focus-visible + div label[data-baseweb="radio"],
        [data-testid="stRadio"] label[data-baseweb="radio"]:focus-within {
            outline: none !important;
            box-shadow: 0 0 0 3px rgba(105, 171, 74, 0.3) !important;
            border-color: var(--accent-green) !important;
        }

        /* Ensure label text is visible and doesn't wrap */
        [data-testid="stRadio"] label[data-baseweb="radio"] > div:last-child,
        [data-testid="stRadio"] label[data-baseweb="radio"] span {
            white-space: nowrap !important;
            overflow: visible !important;
        }

/* ============================================================
            SUMMARY STATS
            ============================================================ */
        .stats-row {
            display: flex;
            gap: 0.8rem;
            margin: 1rem 0 0.75rem 0;
        }

        /* ============================================================
            STICKY FOOTER (Section 2 - Attendance Page)
            ============================================================ */
        .sticky-footer {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 3rem);
            max-width: 800px;
            background: var(--bg-primary);
            padding: 1rem 0 1.5rem 0;
            z-index: 100;
            border-top: 1px solid var(--border-color);
            box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
        }

        .sticky-footer .stats-row {
            margin-bottom: 0.75rem;
            padding: 0 1.5rem;
        }

        .sticky-footer .stButton > button {
            width: 100% !important;
        }

        /* Button row inside footer - matches the two-column button layout */
        .sticky-footer [data-testid="stHorizontalBlock"] {
            gap: 1rem !important;
        }

        .sticky-footer [data-testid="column"] {
            flex: 1 !important;
            min-width: 0 !important;
        }

        /* Add bottom padding to block-container to prevent content hiding behind fixed footer */
        .block-container {
            padding-bottom: 12rem !important;
        }

        /* Tablet Landscape (1024px and below) - Sticky Footer */
        @media (max-width: 1024px) {
            .sticky-footer {
                width: calc(100% - 2rem);
                padding: 0.85rem 0 1.25rem 0;
            }
            .sticky-footer .stats-row {
                padding: 0 1rem;
            }
            .block-container {
                padding-bottom: 11rem !important;
            }
        }

        /* Tablet Portrait (768px and below) - Sticky Footer */
        @media (max-width: 768px) {
            .sticky-footer {
                width: calc(100% - 1.5rem);
                padding: 0.75rem 0 1rem 0;
            }
            .sticky-footer .stats-row {
                padding: 0 0.75rem;
            }
            .block-container {
                padding-bottom: 10rem !important;
            }
        }

        /* Mobile Landscape (480px and below) - Sticky Footer */
        @media (max-width: 480px) {
            .sticky-footer {
                width: calc(100% - 1rem);
                padding: 0.6rem 0 0.85rem 0;
            }
            .sticky-footer .stats-row {
                padding: 0 0.5rem;
            }
            .block-container {
                padding-bottom: 9rem !important;
            }
        }

        /* Error message inside sticky footer - full width with wrapping */
        .sticky-footer .stAlert {
            width: 100% !important;
            max-width: 100% !important;
            box-sizing: border-box !important;
        }

        .sticky-footer .stAlert > div {
            word-wrap: break-word !important;
            overflow-wrap: break-word !important;
            white-space: normal !important;
        }

        .stat-card {
            flex: 1;
            background: var(--bg-card);
            border: 3px solid var(--border-dark);
            border-radius: var(--radius-md);
            padding: 0.85rem 1rem;
            min-width: 120px;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .stat-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .stat-value {
            font-size: 1.5rem;
            font-weight: 800;
            line-height: 1.1;
        }

        .stat-label {
            font-size: 0.75rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 0.3rem;
            font-weight: 600;
        }

        .stat-present .stat-value { color: #27AE60; }
        .stat-absent .stat-value { color: #E74C3C; }
        .stat-total .stat-value { color: #000000; }
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
            color: #FFFFFF !important;
            box-shadow: 0 2px 8px rgba(105,171,74,0.3) !important;
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

            .attendance-header-row,
            .attendance-row {
                grid-template-columns: 50px minmax(200px, 1fr) minmax(250px, 1fr) 160px;
            }

            .form-card {
                padding: 1.2rem 1.2rem;
            }

            .stat-card {
                min-width: 100px;
                padding: 0.75rem 0.85rem;
            }

            .stat-value {
                font-size: 1.3rem;
            }

            .stat-label {
                font-size: 0.7rem;
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

            .stat-card {
                min-width: 85px;
                padding: 0.6rem 0.7rem;
            }

            .stat-value {
                font-size: 1.1rem;
            }

            .stat-label {
                font-size: 0.62rem;
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

            .attendance-header-row,
            .attendance-row {
                grid-template-columns: 45px minmax(180px, 1fr) minmax(200px, 1fr) 150px;
            }

            .attendance-col {
                padding: 0 0.35rem;
            }

            .attendance-col-name {
                font-size: 0.82rem;
            }

            .attendance-col-stream {
                font-size: 0.75rem;
            }

            .attendance-radio-label {
                padding: 0.25rem 0.4rem;
                font-size: 0.72rem;
                min-width: 55px;
            }

            .attendance-radio-input {
                width: 12px;
                height: 12px;
            }

            [data-testid="stSelectbox"] > div > div {
                min-height: 44px !important;
                font-size: 0.95rem !important;
            }

            [data-testid="stSelectbox"] label {
                font-size: 0.85rem !important;
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
            .col-stream {
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

            .stat-card {
                min-width: 75px;
                padding: 0.55rem 0.6rem;
                border-width: 2px;
            }

            .stat-value {
                font-size: 1rem;
            }

            .stat-label {
                font-size: 0.58rem;
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

            .attendance-header-row,
            .attendance-row {
                grid-template-columns: 40px minmax(150px, 1fr) minmax(180px, 1fr) 140px;
            }

            .attendance-col {
                padding: 0 0.25rem;
            }

            .attendance-col-name {
                font-size: 0.78rem;
            }

            .attendance-col-stream {
                font-size: 0.7rem;
            }

            .attendance-radio-label {
                padding: 0.2rem 0.3rem;
                font-size: 0.68rem;
                min-width: 50px;
            }

            .attendance-radio-input {
                width: 11px;
                height: 11px;
            }

            .attendance-radio-text {
                font-size: 0.68rem;
            }

            [data-testid="stSelectbox"] > div > div {
                min-height: 44px !important;
                font-size: 0.9rem !important;
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

            .attendance-header-row,
            .attendance-row {
                grid-template-columns: 35px minmax(120px, 1fr) minmax(150px, 1fr) 120px;
            }

            .attendance-col-name {
                font-size: 0.7rem;
            }

            .attendance-col-stream {
                font-size: 0.65rem;
            }

            .attendance-radio-label {
                padding: 0.15rem 0.25rem;
                font-size: 0.6rem;
                min-width: 45px;
            }

            .attendance-radio-input {
                width: 10px;
                height: 10px;
            }

            .attendance-radio-text {
                font-size: 0.6rem;
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

        /* ============================================================
           ADMIN LOGIN & DASHBOARD STYLES
           ============================================================ */

        /* Admin Login Container */
        .admin-login-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 60vh;
            padding: 2rem;
        }

        .admin-login-card {
            background: var(--bg-card);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-lg);
            padding: 2.5rem 3rem;
            max-width: 420px;
            width: 100%;
            box-shadow: var(--shadow-lg);
        }

        .admin-login-header {
            text-align: center;
            margin-bottom: 2rem;
        }

        .admin-login-header h2 {
            color: var(--text-primary);
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .admin-login-header p {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin: 0;
        }

        /* Admin Dashboard Header */
        .admin-dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid var(--border-color);
        }

        .admin-dashboard-title {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--text-primary);
            margin: 0;
        }

        .admin-dashboard-subtitle {
            font-size: 1rem;
            color: var(--text-secondary);
            margin: 0.25rem 0 0 0;
        }

        /* KPI Cards */
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .kpi-card {
            background: var(--bg-card);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-md);
            padding: 1.25rem 1.5rem;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .kpi-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .kpi-label {
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .kpi-value {
            font-size: 2rem;
            font-weight: 800;
            line-height: 1.1;
        }

        .kpi-value.present { color: #27AE60; }
        .kpi-value.absent { color: #E74C3C; }
        .kpi-value.total { color: var(--text-primary); }
        .kpi-value.percent { color: var(--accent-green); }
        .kpi-value.records { color: var(--accent-blue); }
        .kpi-value.days { color: var(--accent-yellow); }

        /* Metric Cards (new st.columns-based layout) */
        .metric-card {
            background: var(--bg-card);
            border: 2px solid var(--accent-green);
            border-radius: var(--radius-md);
            padding: 1.25rem 1.5rem;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 120px;
        }

        .metric-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(105, 171, 74, 0.2);
            border-color: var(--accent-green-dark);
        }

        .metric-icon {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            opacity: 0.7;
        }

        .metric-label {
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 600;
            margin-bottom: 0.35rem;
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 800;
            line-height: 1.1;
            color: var(--accent-green);
        }

        /* Filters Section */
        .filters-section {
            background: var(--bg-card);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .filters-title {
            font-size: 1rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 1rem;
        }

        .filters-row {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            align-items: flex-end;
        }

        .filter-group {
            flex: 1;
            min-width: 160px;
        }

        .filter-label {
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.35rem;
        }

        /* Make Streamlit columns in filters wrap responsively */
        .filters-section [data-testid="column"] {
            min-width: 180px;
            flex: 1 1 180px !important;
        }

        .filters-section .stSelectbox,
        .filters-section .stDateInput {
            width: 100% !important;
        }

        .filters-section .stSelectbox > div > div,
        .filters-section .stDateInput > div > div {
            width: 100% !important;
        }

        /* Ensure dropdown menus are fully visible */
        .filters-section .stSelectbox [data-baseweb="select"],
        .filters-section .stDateInput [data-baseweb="input"] {
            min-width: 100% !important;
        }

        /* On mobile: stack filters vertically */
        @media (max-width: 768px) {
            .filters-section [data-testid="column"] {
                min-width: 100% !important;
                flex: 1 1 100% !important;
            }
        }

        /* Chart Containers */
        .chart-container {
            background: var(--bg-card);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .chart-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 1rem;
        }

        /* Data Tables */
        .data-table-container {
            background: var(--bg-card);
            border: 2px solid var(--border-dark);
            border-radius: var(--radius-md);
            padding: 1rem;
            margin-bottom: 1.5rem;
            overflow-x: auto;
        }

        .data-table-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 1rem;
        }

        /* Refresh Button */
        .refresh-button {
            margin-bottom: 1.5rem;
        }

        /* Admin Dashboard specific responsive */
        @media (max-width: 768px) {
            .kpi-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .admin-login-card {
                padding: 2rem 1.5rem;
                margin: 1rem;
            }

            .filters-row {
                flex-direction: column;
            }

            .filter-group {
                width: 100%;
            }
        }

        @media (max-width: 480px) {
            .kpi-grid {
                grid-template-columns: 1fr;
            }

            .admin-dashboard-header {
                flex-direction: column;
                gap: 1rem;
                text-align: center;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )