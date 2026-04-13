# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---
    Model name: MoodSense

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  


        This model helps people find songs that match the vibe they want—whether that’s happy pop, chill lofi, or high‑energy workout tracks.
        It looks at things like genre, mood, and energy to pick out the best matches.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.


    For each song, it gives out points when something matches well; like  a mood match, or an energy level that’s close to what the user asked for. 
    It also subtracts or reduces points when things don’t line up then it adds up all those points into a final score and sorts the songs from 
    highest to lowest. Then the top‑scoring songs become the recommendations. descrIt’s basically a vibe matching system. It looks at what the user 
    wants, checks how close each song is to that vibe, and ranks the songs by best fit.


## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

        The dataset contains a small catalog of songs; usually around a few dozen entries. It includes  genres like pop, rock, EDM, and lofi, along
        with moods such as happy, and energetic. I didn’t add or remove any major data, so the set stays small and a bit uneven. Because of that some
        parts of musical taste are missing, like jazz, classical, metal, and so on . This means the recommender can only work within the limited styles
        represented in the CSV

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

        The recommender works best for users who have clear, consistent preferences like people. It does a good job matching energy levels and tends to
        pick songs that fit the  vibe the user is asking for. I also noticed patterns that made sense, high‑energy profiles consistently pulled  pop tracks,
        while low‑energy profiles shifted toward  lofi songs. In many tests, the top recommendations matched my expectations.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

        The system ignores some musical features that real listeners care about, like tempo, or instrumentation.
        The model tends to repeat the same types of songs and overlook others.

Right now, the recommender leans too heavily on energy, so songs with similar energy can rank high even if the mood or genre doesn’t really fit. It also treats labels like ‘pop’ and ‘indie pop’ as totally different, which can unfairly push similar songs down the list. Since the dataset is small and uneven, some genres and moods show up more often and dominate the results. This can create a bit of a recommendation bubble instead of giving users a wider mix of music.

## 7. Evaluation  

    I tested three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I looked at the top 5 songs for each profile and 
    checked whether genre, mood, and energy reasons made sense.  The system did a good job picking clear matches like Sunrise City 
    for High-Energy Pop, Library Rain for Chill Lofi, and Storm Runner for Deep Intense Rock. The surprising part was how often Gym 
    Hero stayed near the top, even when the profile was not mainly about pop. That happened because energy now has a strong weight, 
    so high-energy songs can rise quickly even with partial category matches. This quick profile comparison helped me confirm both the 
    strengths and the filter-bubble risk of the current scoring recipe.


## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

        The model could be improved by adding more features, like 1. Tempo,  or instrumentation, so it understands more of what makes a song
        feel a certain way.     2. Explain recommendations more clearly.    3. Increase diversity in the top results, so the system doesn’t keep
        repeating the same genre or artist.    4. Handle more complex or mixed user tastes like someone who wants ‘sad but high‑energy’ would make
        recommendations feel more realistic and flexible.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

        This project taught me a lot about how recommender systems  work behind the scenes. I learned that a model can be very sensitive  to small
        changes like shifting one weight or removing one feature that will in consequence affect the recommendations. It was also interesting to see
        where the system behaved in ways I didn’t expect. This changed the way I think about apps like Spotify or YouTube. I learned that music
        recommendation can be very tricky
