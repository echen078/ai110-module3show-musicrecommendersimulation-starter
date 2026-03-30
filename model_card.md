# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Intended Use

This recommender suggests songs from a small catalog based on a listener's favorite genre, mood, energy level, and acoustic preference. It is designed for classroom exploration and understanding how simple playlist scoring works. It is not meant to replace a full music streaming service for real listeners.

---

## 3. How the Model Works

The model checks four things for each song. It gives a boost when the song matches the requested genre and mood. It then prefers songs whose energy is close to the user's target energy. Finally, it rewards songs with acousticness near the listener's preference for organic or produced sound. The final ranking is a weighted score of these matches.

---

## 4. Data

The catalog has 18 songs from `data/songs.csv`. It includes genres like lofi, pop, indie pop, hip-hop, rock, ambient, jazz, synthwave, r&b, classical, electronic, country, and funk. Moods include chill, intense, happy, relaxed, melancholic, uplifting, moody, focused, romantic, and sad. The dataset is small and does not cover all musical styles or very niche tastes.

---

## 5. Strengths

The system works well for clear taste profiles like happy pop or chill lofi. It captures obvious genre and mood matches and often ranks songs with the right energy level higher. For example, a high-energy pop profile normally gets upbeat pop songs ahead of slower tracks.

---

## 6. Limitations and Bias

The model does not use tempo, valence, danceability, artist, or lyrics. It favors energy and genre too strongly, so songs with the right intensity can appear above better mood matches. The dataset is also small and has more lofi and chill examples than some other styles, so rare or mixed tastes may be underrepresented.

---

## 7. Evaluation

I tested with preset profiles in `src/main.py` and with simple unit tests in `tests/test_recommender.py`. Profiles included high-energy pop, chill lofi, and deep intense rock. I checked whether the top songs matched the requested genre, mood, and energy and whether the recommendation order made sense compared to those preferences.

---

## 8. Ideas for Improvement

- Add more songs and more genres to make the catalog less limited.
- Include tempo, valence, and danceability so the model can better distinguish mood.
- Balance the score weights so mood and acoustic preference have more influence.

---

## 9. Personal Reflection

My biggest learning moment was seeing how a basic score function can still create recommendations that feel meaningful when the inputs line up. I also learned that using AI tools helped me phrase the model behavior clearly, but I had to double-check the code and dataset details myself to avoid mistakes about how the scoring actually works.

I was surprised that simple genre, mood, and energy rules can still feel like real recommendations for obvious profiles. The project showed me that a small catalog and a few weights can still capture the idea of matching a listener's taste, even though it is far from a complete system.

If I extended this project, I would add more songs, more audio features like tempo and valence, and more varied user profiles so the model can handle subtle or mixed preferences better.
