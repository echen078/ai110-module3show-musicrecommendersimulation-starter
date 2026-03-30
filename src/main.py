"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Preset taste profiles for different listeners.
    # Four fields are required for the weighted scorer:
    #   genre       → categorical gate (weight 0.35) — strongest differentiator
    #   mood        → categorical gate (weight 0.25) — filters emotional context
    #   energy      → float 0-1 (weight 0.25) — proximity score; 0.8 targets
    #                 high-energy tracks and naturally penalizes chill/lofi
    #   acousticness → float 0-1 (weight 0.15) — 0.2 signals preference for
    #                 produced/electronic sound, which separates rock/pop/synthwave
    #                 from lofi/jazz/classical even when energy is similar
    high_energy_pop = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "acousticness": 0.2,
    }

    chill_lofi = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.4,
        "acousticness": 0.8,
    }

    deep_intense_rock = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "acousticness": 0.15,
    }

    user_prefs = high_energy_pop

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print()
    print("=" * 52)
    print("  Music Recommender — Top 5 for Your Taste Profile")
    print("=" * 52)
    print(f"  Genre: {user_prefs['genre']}  |  Mood: {user_prefs['mood']}  |  Energy: {user_prefs['energy']}")
    print("=" * 52)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  #{rank}  {song['title']}  —  {song['artist']}")
        print(f"       Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"       Score: {score:.2f}")
        print(f"       Why:   {explanation}")

    print()\



if __name__ == "__main__":
    main()
