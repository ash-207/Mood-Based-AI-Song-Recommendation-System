import streamlit as st
from transformers import pipeline

# Load emotion detection model
emotion_classifier = pipeline("text-classification",
                               model="j-hartmann/emotion-english-distilroberta-base",
                               return_all_scores=True,
                               top_k=None)

# Mood-to-song mapping
mood_songs = {
    "joy": [
        "Happy – Pharrell Williams",
        "On Top of the World – Imagine Dragons",
        "Uptown Funk – Bruno Mars"
    ],
    "sadness": [
        "Let Her Go – Passenger",
        "Someone Like You – Adele",
        "Channa Mereya – Arijit Singh"
    ],
    "anger": [
        "Believer – Imagine Dragons",
        "Lose Yourself – Eminem",
        "Numb – Linkin Park"
    ],
    "fear": [
        "Demons – Imagine Dragons",
        "Boulevard of Broken Dreams – Green Day",
        "Everybody Hurts – R.E.M."
    ],
    "surprise": [
        "Viva La Vida – Coldplay",
        "Counting Stars – OneRepublic",
        "Paradise – Coldplay"
    ],
    "disgust": [
        "Breaking the Habit – Linkin Park",
        "I Hate Everything About You – Three Days Grace"
    ],
    "neutral": [
        "Perfect – Ed Sheeran",
        "Photograph – Ed Sheeran",
        "Let Me Down Slowly – Alec Benjamin"
    ]
}

mood_playlists = {
    "joy": {
        "YouTube": ("Feel Good Vibes – YouTube", "https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"),
        "Spotify": ("Happy Hits – Spotify", "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC")
    },
    "sadness": {
        "YouTube": ("Sad Songs – YouTube", "https://www.youtube.com/playlist?list=PLSdoVPM9B0rHbNQZ4k9MCkPmsX5ZDU_5W"),
        "Spotify": ("Life Sucks – Spotify", "https://open.spotify.com/playlist/37i9dQZF1DWSqBruwoIXkA")
    },
    "anger": {
        "YouTube": ("Rage Mode – YouTube", "https://www.youtube.com/playlist?list=PLVO0-xIDR0_1ljSDOqdcS6zA7rO5JOLkj"),
        "Spotify": ("Beast Mode – Spotify", "https://open.spotify.com/playlist/37i9dQZF1DWUVpAXiEPK8P")
    },
    "fear": {
        "YouTube": ("Calm Down Anxiety – YouTube", "https://www.youtube.com/playlist?list=PL2d2Mbyb9FhIlybMRAIyk84ojyqdI-hLy"),
        "Spotify": ("Calm Vibes – Spotify", "https://open.spotify.com/playlist/37i9dQZF1DX4E3UdUs7fUx")
    },
    "surprise": {
        "YouTube": ("Unexpected Bops – YouTube", "https://www.youtube.com/playlist?list=PLDcnymzs18LWRd5Z3fKkzYkiMZY3h84eH"),
        "Spotify": ("Fresh Finds – Spotify", "https://open.spotify.com/playlist/37i9dQZF1DX4WgZiuR77Ef")
    },
    "disgust": {
        "YouTube": ("Dark Vibes – YouTube", "https://www.youtube.com/playlist?list=PL_Y1ZcC9Y_yUPrU7rChmR3xLMWg1VqOej"),
        "Spotify": ("Angsty Alt – Spotify", "https://open.spotify.com/playlist/37i9dQZF1DX59NCqCqJtoH")
    },
    "neutral": {
        "YouTube": ("Chill Mix – YouTube", "https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI"),
        "Spotify": ("Lo-Fi Beats – Spotify", "https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy")
    }
}

mood_themes = {
    "joy": {
        "bg": "linear-gradient(135deg, #FFF9C4, #FFD54F)",   # sunshine yellow
        "text": "#1B1B1B",
        "accent": "#FF8F00"
    },
    "sadness": {
        "bg": "linear-gradient(135deg, #C6DBF0, #7EA6E0)",   # cool calm blue
        "text": "#101F33",
        "accent": "#2B65EC"
    },
    "anger": {
        "bg": "linear-gradient(135deg, #FFB3B3, #FF4C4C)",   # heated red
        "text": "#330000",
        "accent": "#D50000"
    },
    "fear": {
        "bg": "linear-gradient(135deg, #E1C7F3, #7B1FA2)",   # mystic purple
        "text": "#1C0D1A",
        "accent": "#AB47BC"
    },
    "surprise": {
        "bg": "linear-gradient(135deg, #FFE9B1, #FFA726)",   # orange energy
        "text": "#3C2F00",
        "accent": "#FB8C00"
    },
    "disgust": {
        "bg": "linear-gradient(135deg, #C8E6C9, #558B2F)",   # mossy green
        "text": "#1B2B1B",
        "accent": "#66BB6A"
    },
    "neutral": {
        "bg": "linear-gradient(135deg, #ECECEC, #DADADA)",   # soft steel
        "text": "#222222",
        "accent": "#4F4F4F"
    }
}




mood_emojis = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😠",
    "fear": "😨",
    "surprise": "😲",
    "disgust": "🤢",
    "neutral": "😐"
}
song_links = {
    "YouTube": {
        "Happy – Pharrell Williams": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "On Top of the World – Imagine Dragons": "https://www.youtube.com/watch?v=w5tWYmIOWGk",
        "Uptown Funk – Bruno Mars": "https://www.youtube.com/watch?v=OPf0YbXqDm0",
        "Let Her Go – Passenger": "https://www.youtube.com/watch?v=RBumgq5yVrA",
        "Someone Like You – Adele": "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
        "Channa Mereya – Arijit Singh": "https://www.youtube.com/watch?v=284Ov7ysmfA",
        "Believer – Imagine Dragons": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
        "Lose Yourself – Eminem": "https://www.youtube.com/watch?v=_Yhyp-_hX2s",
        "Numb – Linkin Park": "https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Demons – Imagine Dragons": "https://www.youtube.com/watch?v=mWRsgZuwf_8",
        "Boulevard of Broken Dreams – Green Day": "https://www.youtube.com/watch?v=Soa3gO7tL-c",
        "Everybody Hurts – R.E.M.": "https://www.youtube.com/watch?v=ijZRCIrTgQc",
        "Viva La Vida – Coldplay": "https://www.youtube.com/watch?v=dvgZkm1xWPE",
        "Counting Stars – OneRepublic": "https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Paradise – Coldplay": "https://www.youtube.com/watch?v=1G4isv_Fylg",
        "Breaking the Habit – Linkin Park": "https://www.youtube.com/watch?v=v2H4l9RpkwM",
        "I Hate Everything About You – Three Days Grace": "https://www.youtube.com/watch?v=d8ekz_CSBVg",
        "Perfect – Ed Sheeran": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
        "Photograph – Ed Sheeran": "https://www.youtube.com/watch?v=nSDgHBxUbVQ",
        "Let Me Down Slowly – Alec Benjamin": "https://www.youtube.com/watch?v=50VNCymT-Cs"
    },

    "Spotify": {
        "Happy – Pharrell Williams": "https://open.spotify.com/track/60nZcImufyMA1MKQY3dcCH",
        "On Top of the World – Imagine Dragons": "https://open.spotify.com/track/4xjlfD0kTWZQdlFjXgy2Wk",
        "Uptown Funk – Bruno Mars": "https://open.spotify.com/track/32OlwWuMpZ6b0aN2RZOeMS",
        "Let Her Go – Passenger": "https://open.spotify.com/track/2jyjhRf6DVbMPU5zxagN2h",
        "Someone Like You – Adele": "https://open.spotify.com/track/4kflIGfjdZJW4ot2ioixTB",
        "Channa Mereya – Arijit Singh": "https://open.spotify.com/track/1mw0RgNXIP1wiyg4D12pSy",
        "Believer – Imagine Dragons": "https://open.spotify.com/track/0pqnGHJpmpxLKifKRmU6WP",
        "Lose Yourself – Eminem": "https://open.spotify.com/track/1bDbXMyjaUIooNwFE9wn0N",
        "Numb – Linkin Park": "https://open.spotify.com/track/2nLtzopw4rPReszdYBJU6h",
        "Demons – Imagine Dragons": "https://open.spotify.com/track/3LlAyCYU26dvFZBDUIMb7a",
        "Boulevard of Broken Dreams – Green Day": "https://open.spotify.com/track/5GorCbAP4aL0EJ16frG2hd",
        "Everybody Hurts – R.E.M.": "https://open.spotify.com/track/3XVBdLihbNbxUwZosxcGuJ",
        "Viva La Vida – Coldplay": "https://open.spotify.com/track/1mea3bSkSGXuIRvnydlB5b",
        "Counting Stars – OneRepublic": "https://open.spotify.com/track/6sy3LkhNFjJWlaeSMNwQ62",
        "Paradise – Coldplay": "https://open.spotify.com/track/6nek1Nin9q48AVZcWs9e9D",
        "Breaking the Habit – Linkin Park": "https://open.spotify.com/track/5jE48hhRu8E6zBDPRSkEq7",
        "I Hate Everything About You – Three Days Grace": "https://open.spotify.com/track/0jNcIjegG2nwsL10fNkxjP",
        "Perfect – Ed Sheeran": "https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v",
        "Photograph – Ed Sheeran": "https://open.spotify.com/track/6gk5mD9A8NRYz0P6R6UEnD",
        "Let Me Down Slowly – Alec Benjamin": "https://open.spotify.com/track/2nGFzvICaeEWjIrBrL2RAx"
    }
}




# Streamlit UI
st.title("🎧 AI Mood-Based Song Recommender")
st.write("Describe how you're feeling right now, and get some song suggestions based on your mood!")

platform = st.selectbox(
    "🎵 Where would you like to listen?",
    ["YouTube", "Spotify"]
)

user_input = st.text_input("💬 Your mood (type a sentence):")

if user_input:
    with st.spinner("Analyzing your mood..."):
        result = emotion_classifier(user_input)
        sorted_result = sorted(result[0], key=lambda x: x['score'], reverse=True)
        
        mood = sorted_result[0]['label'].lower()
        confidence = round(sorted_result[0]['score'] * 100, 2)

        st.markdown(f"### Detected Mood: {mood_emojis.get(mood, '')} **{mood.upper()}** ({confidence}% confidence)")

        import time
        time.sleep(0.05)  # Small pause for smooth transition

        # Apply mood-based theme
        theme = mood_themes.get(mood, mood_themes["neutral"])
        bg = theme["bg"]
        text = theme["text"]
        accent = theme["accent"]

        # Inject styling
        st.markdown(
            f"""
            <style>
                html, body, .stApp {{
                    background: {bg};
                    font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
                    color: {text};
                    animation: fadeSlideIn 0.6s ease-in-out;
                    transition: background 0.5s ease-in-out, color 0.5s ease-in-out;
                }}
                @keyframes fadeSlideIn {{
                    from {{
                        opacity: 0;
                        transform: translateY(-10px);
                    }}
                    to {{
                        opacity: 1;
                        transform: translateY(0);
                    }}
                }}
                p, label, h1, h2, h3, h4, h5, h6 {{
                    color: {text};
                    opacity: 0.92;
                    letter-spacing: 0.3px;
                }}
                a {{
                    color: {accent};
                    text-decoration: none;
                    font-weight: 600;
                    transition: 0.2s ease-in-out;
                }}
                a:hover {{
                    opacity: 0.85;
                    text-decoration: underline;
                }}
                h4 {{
                    text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1);
                }}
                .css-1cpxqw2, .css-1aumxhk {{
                    color: {text} !important;
                    opacity: 0.9;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )



        theme = mood_themes.get(mood, mood_themes["neutral"])
        bg = theme["bg"]
        text = theme["text"]
        accent = theme["accent"]

        st.markdown(
    f"""
    <style>
        html, body, .stApp {{
            background: {bg};
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
            color: {text};
            transition: all 0.5s ease-in-out;
        }}

        /* Matte text style */
        p, label, h1, h2, h3, h4, h5, h6 {{
            color: {text};
            opacity: 0.92;
            letter-spacing: 0.3px;
        }}

        /* Link style with accent */
        a {{
            color: {accent};
            text-decoration: none;
            font-weight: 600;
        }}

        a:hover {{
            opacity: 0.85;
            text-decoration: underline;
        }}

        /* Subheader style */
        h4 {{
            text-shadow: 0px 1px 2px rgba(0,0,0,0.15);
        }}

        /* Widget labels (optional fix) */
        .css-1cpxqw2, .css-1aumxhk {{
            color: {text} !important;
            opacity: 0.9;
        }}
    </style>
    """,
    unsafe_allow_html=True
)




        
        st.markdown(
    f"""
    <style>
        /* Main background and font */
        html, body, .stApp {{
            background: {bg};
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
            color: {text};
            animation: fadeSlideIn 0.6s ease-in-out;
            transition: background 0.5s ease-in-out, color 0.5s ease-in-out;
        }}

        /* Smooth fade & slide-in animation */
        @keyframes fadeSlideIn {{
            from {{
                opacity: 0;
                transform: translateY(-10px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        /* Matte text styles */
        p, label, h1, h2, h3, h4, h5, h6 {{
            color: {text};
            opacity: 0.92;
            letter-spacing: 0.3px;
        }}

        /* Playlist/song links */
        a {{
            color: {accent};
            text-decoration: none;
            font-weight: 600;
            transition: 0.2s ease-in-out;
        }}

        a:hover {{
            opacity: 0.85;
            text-decoration: underline;
        }}

        /* Header shadows */
        h4 {{
            text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1);
        }}

        /* Streamlit widget label overrides */
        .css-1cpxqw2, .css-1aumxhk {{
            color: {text} !important;
            opacity: 0.9;
        }}
    </style>
    """,
    unsafe_allow_html=True
)




        if mood in mood_playlists:
            playlist_name, playlist_link = mood_playlists[mood].get(platform, ("No playlist", ""))
        st.subheader("🎧 Playlist Recommendation:")
        st.write(f"**{playlist_name}**  [Open]({playlist_link})")

        st.subheader("🎵 Top Song Picks:")
        for song in mood_songs[mood]:
            link = song_links.get(platform, {}).get(song, "")
            if link:
                st.write(f"**{song}**  [▶️]({link})")
            else:
                st.write(f"- {song}")






