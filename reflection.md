# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? When I first ran the game, it appeared to load normally, but several core features were broken. After finishing a round, clicking the "New Game" button with the same Difficulty did nothing. I had to manually refresh the page to reset the game. Secondly, the hint system was reversed: when my guess was too low, it told me to "GO LOWER", and when it was too high, it said "GO HIGHER". Lastly, the attempt counter was off by one: the game was set to 8 attempts, but it ended and showed the result when there was still 1 attempt remaining. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Click "New Game" button after a round ends (using the same difficulty)|Game resets immediately| Nothing happens. Page must manually refresh| No error. Event listener likely unbound after game end|
|Submit a guess lower than the secret number| "GO HIGHER" message displayed|"GO LOWER" message displayed| No error. Comparison operator likely flipped|
|Play 8-attempt game and exhaust all guesses| Game ends after the 8th guess| Game ends with 1 attempt still showing| No error. Termination condittion likely uses < instead of <=|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I verified by running pytest with 11 tests passing. The key tests were test_too_high_tells_player_to_go_lower and test_too_low_tells_player_to_go_higher which confirmed that guessing above the secret correctly returns "Too High" with a "Go LOWER" message, and guessing below returns "Too Low" with a "Go HIGHER" message.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When fixing the New Game button, the AI suggested adding 
status = "playing" and history = [] to the reset block. However, after manually testing the game, I noticed the score was not resetting to 0 when starting a new game. The AI missed that line, so I added score = 0 myself after catching it through manual testing.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
I used both pytest and manual browser testing together. pytest confirmed the logic was correct, and manual testing confirmed the UI behaved correctly in the real game.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
AI generated a parametrized test called test_high_low_outcome_direction that tested 6 different guess/secret combinations (like guess=60 secret=50 expecting "Too High", and guess=40 secret=50 expecting "Too Low"). Running pytest showed all 11 tests passing, which confirmed the high/low hint bug was fully fixed.

- Did AI help you design or understand any tests? How?
Yes. Claude helped me understand why the 3 starter tests needed to be updated from assert result == "Win" to outcome, _ = check_guess(...) because check_guess returns a tuple, not a single string. Claude also guided me to write the new test myself rather than just giving me the answer.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
If I had to explain it to a friend, I'd say: every time you click a button or change an input in Streamlit, the entire script runs again from top to bottom — that's a "rerun." Normally this would mean all your variables reset back to their starting values, like the page forgot everything that happened. That's where `session_state` comes in. It's like a notebook that survives the rerun. Anything you want Streamlit to "remember" between clicks (like the secret number, score, or guess history) has to be stored in `st.session_state`, otherwise it gets wiped every time the app reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One habit I definitely want to reuse is always asking the AI why it's recommending a change, and asking it to explain it in detail as if I'm a complete beginner, until I actually understand why the change is needed and what it's being changed to. This habit didn't just help me fix the code, it also taught me how to actually learn from AI instead of just copying its output. Another thing I want to keep using is my prompting strategy being specific by structuring prompts around ROLE, TASK, CONTEXT, CONSTRAINTS, and QUALITY CHECK.

- What is one thing you would do differently next time you work with AI on a coding task? 
Next time, I'll write down each bug and its fix immediately after I find and resolve it. This time, I sometimes forgot the exact part I had changed manually after fixing it, which made it harder to go back and document everything accurately later.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project taught me that AI-generated code is most valuable as a learning tool, not just a quick fix. Using AI efficiently doesn't mean letting it fix the code for me right away. It means letting it ask me questions first, so I have to think through the answer myself before learning the solution.