import random
from typing import Dict, List

import streamlit as st


# Page config
st.set_page_config(page_title="AI 영화 추천봇", page_icon="🎬", layout="centered")

# Minimal inline CSS for centered layout and gradient background + simple cards
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 50%, #e0f2fe 100%);
    }

    /* Center the main container and limit width */
    .main-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 1rem 0 2rem 0;
        text-align: center;
    }

    .subtitle {
        color: #475569;
        font-size: 1.05rem;
        margin-top: 0.25rem;
        margin-bottom: 1.5rem;
    }

    .help-text {
        color: #334155;
        font-weight: 600;
        background: rgba(255,255,255,0.6);
        border: 1px solid rgba(148,163,184,0.25);
        padding: 0.85rem 1rem;
        border-radius: 12px;
        display: inline-block;
        margin-top: 0.5rem;
    }

    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
        gap: 16px;
        margin-top: 12px;
    }

    .card {
        background: rgba(255,255,255,0.85);
        border: 1px solid rgba(148,163,184,0.25);
        border-radius: 14px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        overflow: hidden;
        transition: transform 120ms ease;
    }

    .card:hover { transform: translateY(-2px); }

    .poster {
        width: 100%;
        height: 300px;
        object-fit: cover;
        background: #e2e8f0;
        display: block;
    }

    .card-title {
        padding: 10px 12px 12px 12px;
        font-weight: 700;
        color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session state for selected genre
if "selected_genre" not in st.session_state:
    st.session_state.selected_genre = None

# Simple dataset: genre -> list of movies with optional poster URL
MOVIES: Dict[str, List[Dict[str, str]]] = {
    "액션": [
        {"title": "어벤져스", "poster": "https://picsum.photos/seed/avengers/500/750"},
        {"title": "다크 나이트", "poster": "https://picsum.photos/seed/dark-knight/500/750"},
        {"title": "매드맥스: 분노의 도로", "poster": "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg"},
        {"title": "존 윅", "poster": "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg"},
        {"title": "미션 임파서블: 폴아웃", "poster": "https://picsum.photos/seed/mission-impossible/500/750"},
    ],
    "코미디": [
        {"title": "슈퍼배드", "poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png"},
        {"title": "행오버", "poster": "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg"},
        {"title": "나홀로 집에", "poster": "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg"},
        {"title": "브루스 올마이티", "poster": "https://picsum.photos/seed/bruce-almighty/500/750"},
        {"title": "주먹왕 랄프", "poster": "https://picsum.photos/seed/wreck-it-ralph/500/750"},
    ],
    "로맨스": [
        {"title": "노트북", "poster": "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg"},
        {"title": "라라랜드", "poster": "https://picsum.photos/seed/la-la-land/500/750"},
        {"title": "어바웃 타임", "poster": "https://picsum.photos/seed/about-time/500/750"},
        {"title": "비포 선라이즈", "poster": "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg"},
        {"title": "그 여자 작사 그 남자 작곡", "poster": "https://picsum.photos/seed/music-and-lyrics/500/750"},
    ],
    "호러": [
        {"title": "컨저링", "poster": "https://picsum.photos/seed/the-conjuring/500/750"},
        {"title": "그것", "poster": "https://picsum.photos/seed/it-2017/500/750"},
        {"title": "겟 아웃", "poster": "https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png"},
        {"title": "애나벨: 인형의 주인", "poster": "https://picsum.photos/seed/annabelle-creation/500/750"},
        {"title": "할로윈", "poster": "https://picsum.photos/seed/halloween-2018/500/750"},
    ],
}


def render_header() -> None:
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.markdown("## 🎬 AI 영화 추천봇")
        st.markdown(
            '<div class="subtitle">좋아하는 장르를 선택하면 맞춤 영화를 추천해드려요!</div>',
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)


def render_genre_selector() -> None:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    # 2x2 grid using two rows of two columns
    row1 = st.columns(2, gap="large")
    row2 = st.columns(2, gap="large")

    if row1[0].button("🔥 액션", use_container_width=True):
        st.session_state.selected_genre = "액션"
    if row1[1].button("😂 코미디", use_container_width=True):
        st.session_state.selected_genre = "코미디"
    if row2[0].button("💕 로맨스", use_container_width=True):
        st.session_state.selected_genre = "로맨스"
    if row2[1].button("👻 호러", use_container_width=True):
        st.session_state.selected_genre = "호러"

    st.markdown('</div>', unsafe_allow_html=True)


def recommend_movies(genre: str) -> List[Dict[str, str]]:
    movies = MOVIES.get(genre, [])
    if not movies:
        return []
    k = min(len(movies), random.randint(3, 5))
    return random.sample(movies, k)


def render_results() -> None:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    if not st.session_state.selected_genre:
        st.markdown('<div class="help-text">영화 추천을 시작해보세요!</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        return

    genre = st.session_state.selected_genre
    recs = recommend_movies(genre)

    st.markdown(f"#### '{genre}' 장르 추천 작품")

    # Card grid
    fallback_poster = "https://via.placeholder.com/500x750.png?text=No+Image"
    cards_html = [
        (
            "<div class='card'>"
            f"<img class='poster' src='{item.get('poster') or fallback_poster}' alt='{item['title']} 포스터' referrerpolicy='no-referrer' "
            f"onerror=\"this.onerror=null;this.src='{fallback_poster}';\" />"
            f"<div class='card-title'>{item['title']}</div>"
            "</div>"
        )
        for item in recs
    ]

    st.markdown("<div class='card-grid'>" + "".join(cards_html) + "</div>", unsafe_allow_html=True)

    # Option to reset selection
    st.write("")
    if st.button("장르 다시 선택", help="선택한 장르를 초기화합니다"):
        st.session_state.selected_genre = None

    st.markdown('</div>', unsafe_allow_html=True)


def main() -> None:
    render_header()
    render_genre_selector()
    render_results()


if __name__ == "__main__":
    main()
