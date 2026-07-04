from . import candy_neon

def stylesheet():

    c = candy_neon.COLORS

    return f"""

QWidget{{
background:{c["background"]};
color:{c["text"]};
font-family:Segoe UI;
}}

QMainWindow{{
background:{c["background"]};
}}

QToolBar{{
background:{c["surface"]};
border:none;
}}

QStatusBar{{
background:{c["surface"]};
}}

QListWidget{{
background:{c["surface"]};
border:2px solid {c["primary"]};
border-radius:12px;
padding:10px;
}}

QPushButton{{
background:{c["primary"]};
padding:10px;
border-radius:10px;
}}

QPushButton:hover{{
background:{c["secondary"]};
}}

QComboBox{{
background:{c["surface"]};
padding:8px;
}}

QLabel{{
font-size:22px;
font-weight:bold;
}}

"""
