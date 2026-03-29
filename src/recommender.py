import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """Represents a single song and its audio attributes loaded from songs.csv."""
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
    """Stores a listener's taste preferences used to score and rank songs."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

def score_song(song: Dict, user_prefs: Dict) -> float:
    """Returns a weighted match score (0–5.3) for one song against a user preference dict."""
    score = 0.0

    # Categorical gates
    if song["genre"] == user_prefs.get("genre", ""):
        score += 2.0
    if song["mood"] == user_prefs.get("mood", ""):
        score += 1.0

    # Energy proximity: rewards songs close to the user's target intensity
    energy_sim = max(0.0, 1.0 - abs(song["energy"] - user_prefs.get("energy", 0.5)))
    score += 1.5 * energy_sim

    # Acousticness proximity: differentiates organic vs. produced sound preference
    target_acousticness = user_prefs.get("acousticness", 0.75 if user_prefs.get("likes_acoustic") else 0.20)
    acoustic_sim = max(0.0, 1.0 - abs(song["acousticness"] - target_acousticness))
    score += 0.8 * acoustic_sim

    return round(score, 4)


def _explain(song: Dict, user_prefs: Dict) -> str:
    """Builds a human-readable explanation for why a song was recommended."""
    reasons = []

    if song["genre"] == user_prefs.get("genre", ""):
        reasons.append(f"matches your favorite genre ({song['genre']})")
    if song["mood"] == user_prefs.get("mood", ""):
        reasons.append(f"matches your preferred mood ({song['mood']})")

    energy_diff = abs(song["energy"] - user_prefs.get("energy", 0.5))
    if energy_diff <= 0.15:
        reasons.append(f"energy level is close to your target ({song['energy']} vs {user_prefs.get('energy', 0.5)})")

    target_acousticness = user_prefs.get("acousticness", 0.75 if user_prefs.get("likes_acoustic") else 0.20)
    acoustic_diff = abs(song["acousticness"] - target_acousticness)
    if acoustic_diff <= 0.20:
        reasons.append(f"sound texture fits your acoustic preference (acousticness {song['acousticness']})")

    if not reasons:
        reasons.append("partial match across energy and texture")

    return "This track was recommended because it " + ", and ".join(reasons) + "."


class Recommender:
    """Ranks a song catalog against a UserProfile and returns the top-k matches."""

    def __init__(self, songs: List[Song]):
        """Initializes the recommender with a list of Song objects."""
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        """Adapts UserProfile and Song dataclasses into dicts for score_song."""
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "acousticness": song.acousticness,
        }
        return score_song(song_dict, prefs)

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top-k Song objects sorted by descending match score."""
        scored = sorted(self.songs, key=lambda s: self._score(user, s), reverse=True)
        return scored[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable sentence explaining why a song was recommended."""
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "acousticness": song.acousticness,
            "title": song.title,
        }
        return _explain(song_dict, prefs)


def load_songs(csv_path: str) -> List[Dict]:
    """Parses songs.csv and returns a list of song dicts with typed numeric fields."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song, sorts by descending score, and returns the top-k as (song, score, explanation) tuples."""
    scored = [
        (song, score_song(song, user_prefs), _explain(song, user_prefs))
        for song in songs
    ]
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked[:k]
