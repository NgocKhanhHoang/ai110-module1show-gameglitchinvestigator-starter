# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? When I first ran the game, it appeared to load normally, but several core features were broken. After finishing a round, clicking the "New Game" button with the same Difficulty did nothing. I had to manually refresh the page to reset the game. Secondly, the hint system was reversed: when my guess was too low, it told me to "GO LOWER", and when it was too high, it said "GO HIGHER". Lastly, the attempt counter was off by one: the game was set to 8 attempts, but it ended and showed the result when there was still 1 attempt remaining. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Click "New Game" button after a round ends (using the same difficulty)|Game resets immediately| Nothing happens. Page must manually refresh| No error. Event listener likely unbound after game end|
|Submit a guess lower than the secret number| "GO HIGHER" message displayed| "GO LOWER" message displayed| No error. Comparison operator likely flipped|
|Play 8-attempt game and exhaust all guesses| Game ends after the 8th guess| Game ends with 1 attempt still showing| No error. Termination condittion likely uses < instead of <=|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Gemini
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
