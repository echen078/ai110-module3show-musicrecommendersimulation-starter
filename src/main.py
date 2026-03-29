"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Taste profile: upbeat pop listener who wants high energy and a produced sound.
    # Four fields are required for the weighted scorer:
    #   genre       → categorical gate (weight 0.35) — strongest differentiator
    #   mood        → categorical gate (weight 0.25) — filters emotional context
    #   energy      → float 0-1 (weight 0.25) — proximity score; 0.8 targets
    #                 high-energy tracks and naturally penalizes chill/lofi
    #   acousticness → float 0-1 (weight 0.15) — 0.2 signals preference for
    #                 produced/electronic sound, which separates rock/pop/synthwave
    #                 from lofi/jazz/classical even when energy is similar
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "acousticness": 0.2,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
