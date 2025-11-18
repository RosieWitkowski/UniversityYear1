# Hackathon 12/11/2025   
Submission for the Edge Hill University 2025 Hackathon  
  
**Constraints**: 1 hour, no external libraries  
**Theme**: Text-based adventure game   
**Language**: Python  
  
**Placed**: 1st   
  
## Summary of submission:  
An escape room where the user must complete the wizard's 3 challenges to finish. At each junction, there is a small probability of running into a chest, which will freely provide the user with 50 gold. Otherwise, the user is met with one of the wizards puzzles - granting 100 gold per correct answer for the first 2, and a game-dependant value for the last. If the user completes enough turns without running into the wizard at least 3 times, the wizard takes pity on the user and gives them the remaining challenges without needing to find him. Each puzzle has clues throughout the game. The aim is to gain the most amount of gold, and there is replayability in the game-dependant variances of riddle 2 and 3.
  
## Reflection   
This was my first time coding a working project within such a constrained time limit, it was an enjoyable and informative experience. Part of this meant having to prioritise features, which I will be commenting on here. With more time, it would be best practice to add a try-except block in a validate_int() function, to ensure incorrect input will not give an error when attempting to typecast for puzzle 2 and 3. Additionally, considering the minimum and maximum amount of points possible to win is calculable, a 'ranking' could be added to the end with a custom message (e.g. < 50 points - F, 500-600 points- A, > 600 points - A*). Furthermore, the text_box printing was repeated twice, it would be better to make this a function and potentially use the sleep effect in more areas, with a list of different SLEEP_INTERVAL lengths to apply depending on the context of the text block. Finally, with enough time to do so, the answers() function could be more detailed/user-friendly. 









