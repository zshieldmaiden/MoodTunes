import streamlit as st

# Playlist verisini cache'le (st.cache_data ile)
@st.cache_data
def get_mood_playlists():
    return {
        "mutluyum": [
            ("Happy Hits", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Good Vibes", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Upbeat Pop", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
        ],
        "üzgünüm": [
            ("Sad Songs", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Melancholic Indie", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Emotional Ballads", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
        ],
        "enerjikim": [
            ("Workout Music", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("High Energy", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Pump Up Songs", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
        ],
        "sakinim": [
            ("Chill Out", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Ambient Relaxation", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Lo-Fi Beats", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
        ],
        "romantik hissediyorum": [
            ("Love Songs", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Romantic Hits", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
            ("Date Night", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"),
        ],
        "stresliyim": [
            ("Stress Relief", "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"),
            ("Calm Piano", "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO"),
            ("Peaceful Guitar", "https://open.spotify.com/playlist/37i9dQZF1DX4E3UdUs7fUx"),
        ],
        "heyecanlıyım": [
            ("Party Time", "https://open.spotify.com/playlist/37i9dQZF1DXaXB8fQg7xif"),
            ("Dance Hits", "https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO"),
            ("Feel Good Friday", "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"),
        ],
        "yorgunum": [
            ("Relax & Unwind", "https://open.spotify.com/playlist/37i9dQZF1DX3PIPIT6lEg5"),
            ("Evening Chill", "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6"),
            ("Sleep", "https://open.spotify.com/playlist/37i9dQZF1DWZd79rJ6a7lp"),
        ],
        "motivasyona ihtiyacım var": [
            ("Motivation Mix", "https://open.spotify.com/playlist/37i9dQZF1DXc5e2bJhV6pu"),
            ("Power Boost", "https://open.spotify.com/playlist/37i9dQZF1DX1OY2Lp0bIPp"),
            ("Rise & Shine", "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU"),
        ],
        "nostaljik hissediyorum": [
            ("80s Hits", "https://open.spotify.com/playlist/37i9dQZF1DX4UtSsGT1Sbe"),
            ("90s Pop", "https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l"),
            ("Retro Rock", "https://open.spotify.com/playlist/37i9dQZF1DX1spT6G94GFC"),
        ],
        "odaklanmam lazım": [
            ("Deep Focus", "https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ"),
            ("Coding Mode", "https://open.spotify.com/playlist/37i9dQZF1DX8Uebhn9wzrS"),
            ("Brain Food", "https://open.spotify.com/playlist/37i9dQZF1DX8NTLI2TtZa6"),
        ],
        "sürpriz yap": [
            ("Discover Weekly", "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"),
            ("Release Radar", "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"),
            ("Random Mix", "https://open.spotify.com/playlist/37i9dQZF1DX2sUQwD7tbmL"),
        ],
        "yalnızım": [
            ("Alone Again", "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634"),
            ("Solitude", "https://open.spotify.com/playlist/37i9dQZF1DX3Fzl4v4w9Zp"),
            ("Me, Myself & I", "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx"),
        ],
        "umutluyum": [
            ("Hopeful Vibes", "https://open.spotify.com/playlist/37i9dQZF1DX0SM0LYsmbMT"),
            ("Positive Energy", "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"),
            ("Sunshine", "https://open.spotify.com/playlist/37i9dQZF1DX1BzILRveYHb"),
        ],
    }

# Custom CSS for better look
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7fa;
    }
    .stTextArea textarea {
        background: #fffbe7;
        border-radius: 8px;
        font-size: 1.1em;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ffb347 0%, #ffcc33 100%);
        color: #222;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.5em 1.5em;
        margin-top: 10px;
    }
    .stAlert.success {
        background: #e0ffe0;
        border-left: 6px solid #4CAF50;
    }
    .playlist-link {
        font-size: 1.1em;
        color: #1db954 !important;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("MoodTunes Hakkında")
st.sidebar.info(
    """
    🎵 **MoodTunes Light**
    
    Ruh haline göre müzik öneren demo uygulama. 
    
    - 10'dan fazla mood
    - Tamamen mock veri
    - API anahtarı gerekmez
    """
)
st.sidebar.markdown("---")
st.sidebar.write("Geliştirici: upschool_project")

st.set_page_config(page_title="MoodTunes Light", page_icon="🎵")
st.title("🎵 MoodTunes Light")

st.write("Müzik ruhun gıdasıdır! Ruh halini yaz, sana uygun Spotify çalma listelerini önerelim.")

# Session state ile mood ve öneri kontrolü
def get_recommendations(mood, playlists):
    mood_key = mood.strip().lower()
    for key in playlists:
        if key in mood_key:
            return playlists[key]
    return None

if 'mood' not in st.session_state:
    st.session_state['mood'] = ''
if 'recommendations' not in st.session_state:
    st.session_state['recommendations'] = None
if 'last_submit' not in st.session_state:
    st.session_state['last_submit'] = False

mood = st.text_area("", value=st.session_state['mood'], placeholder="Bugün nasıl hissediyorsun?")

if st.button("Müzik Öner!"):
    st.session_state['mood'] = mood
    playlists = get_mood_playlists()
    recs = get_recommendations(mood, playlists)
    st.session_state['recommendations'] = recs
    st.session_state['last_submit'] = True

if st.session_state['last_submit']:
    if st.session_state['recommendations']:
        st.markdown(
            f"<div class='stAlert success'><b>Senin için önerilen çalma listeleri:</b></div>", unsafe_allow_html=True
        )
        for name, url in st.session_state['recommendations']:
            st.markdown(f"- <a class='playlist-link' href='{url}' target='_blank'>{name}</a>", unsafe_allow_html=True)
    else:
        st.warning("Üzgünüz, bu ruh hali için önerimiz yok. Lütfen farklı bir ruh hali deneyin!") 