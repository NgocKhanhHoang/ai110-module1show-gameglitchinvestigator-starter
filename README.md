# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

1. Game Purpose
This game challenges the player to guess a secret number within a limited number of attempts, using "higher/lower" hints to narrow down their guess.

2. Bugs Found
- **"New Game" button unresponsive:** Clicking "New Game" with the same difficulty did nothing. The game state never reset, forcing a manual page refresh.
- **High/Low hints:** The hint logic was inverted. A guess that was too low returned "GO HIGHER" instead of "GO LOWER", and vice versa.
- **Off-by-one attempt counter:** With attempts set to 8, the game ended and displayed results while 1 attempt still remained.
- **Unimplemented core functions:** `get_range_for_difficulty`, `parse_guess`, and `update_score` in `logic_utils.py` were placeholder stubs raising `NotImplementedError`.

3. Fixes Applied
- **High/Low hint bug:** Removed the even/odd branch in `app.py` that was converting the secret number to a string on even attempts, causing wrong comparisons. Fixed by passing `st.session_state.secret` directly to `check_guess`.
- **New Game bug:** The reset block was missing `score`, `status`, and `history` resets. Added `score = 0`, `status = "playing"`, and `history = []` so the game fully restarts.
- **Unimplemented functions:** Filled in the three placeholder functions — `get_range_for_difficulty`, `parse_guess`, and `update_score` — which were raising `NotImplementedError` in the starter code.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 50
2. Game returns "📈 Go HIGHER!"
3. User enters a guess of 80
4. Game returns "📉 Go LOWER!"
5. Score updates correctly after each guess
6. Game ends after the correct guess or when the player runs out of 8 attempts.

<img width="725" height="639" alt="image" src="https://github.com/user-attachments/assets/83a006a8-a2b3-485f-9841-16d89554a574" />
