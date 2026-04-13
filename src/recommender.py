from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    songs: List[Dict] = []
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if value is None:
                    song[key] = value
                    continue

                cleaned = value.strip()

                if key in int_fields:
                    song[key] = int(cleaned)
                elif key in float_fields:
                    song[key] = float(cleaned)
                else:
                    song[key] = cleaned

            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user's preferences."""
    score = 0.0
    reasons: List[str] = []

    # Support either starter keys (genre/mood/energy) or profile-style keys.
    preferred_genre = user_prefs.get("genre", user_prefs.get("favorite_genre", ""))
    preferred_mood = user_prefs.get("mood", user_prefs.get("favorite_mood", ""))
    target_energy = user_prefs.get("energy", user_prefs.get("target_energy"))

    song_genre = str(song.get("genre", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()

    preferred_genre_norm = str(preferred_genre).strip().lower()
    preferred_mood_norm = str(preferred_mood).strip().lower()

    if preferred_genre_norm and song_genre == preferred_genre_norm:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if preferred_mood_norm and song_mood == preferred_mood_norm:
        score += 1.0
        reasons.append("mood match (+1.0)")

    if target_energy is not None and song.get("energy") is not None:
        song_energy = float(song["energy"])
        energy_diff = abs(song_energy - float(target_energy))
        energy_similarity = max(0.0, 1.0 - energy_diff)
        score += energy_similarity
        reasons.append(f"energy close to target (+{energy_similarity:.2f})")

    if not reasons:
        reasons.append("no direct preference matches")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score, sort, and return the top k recommended songs."""
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
