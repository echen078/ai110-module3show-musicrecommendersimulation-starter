# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

This system has a few clear weaknesses. The dataset is small and skewed toward low-energy and lofi-style tracks, so the recommender can easily create a filter bubble by favoring those familiar sounds. The scoring logic also overweights energy proximity, which means users who want a specific mood like sad or romantic may still see high-energy songs ranked too high. Because genre and energy are treated as strong signals, the model can ignore more subtle user tastes and underrepresent users whose preferences do not fit the dominant catalog patterns.  

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

I tested several user profiles, including a high-energy pop listener, a chill lofi listener, a deep intense rock listener, and adversarial edge cases like a sad rock profile and a high-energy lofi profile. I looked for whether the top recommendations matched the requested genre, mood, and energy, and I compared the default score weights against a version where energy was given twice as much importance and genre was halved. What surprised me was that the recommender still ranked high-energy rock tracks first for a sad rock profile, showing that the model prioritized energy and genre much more than mood. I also found that the current dataset and scoring can underrepresent users with rare mood/genre combinations because it favors the dominant catalog patterns rather than subtle taste signals.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
