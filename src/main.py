"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    # Allows running as a script: python src/main.py
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    sample_profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.92},
    }

    for profile_name, user_prefs in sample_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nUsing profile: {profile_name}")
        print("Top recommendations:\n")

        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

            print(f"{index}. {song['title']}")
            print(f"   Score  : {score:.2f}")
            print("   Reasons:")
            for reason in reasons:
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()
