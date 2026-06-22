# FIX: Refactor the logic_utils.py to include a function that returns the range for a given difficulty level.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100

# FIX: Refactor the parse_guess function to handle float inputs and round them to the nearest integer.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = round(float(raw))  # round 3.9 -> 4 instead of chopping to 3
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: Refactor High/Low hint logic.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

# FIX: Refactor the update_score function to include a scoring system based on the number of attempts and whether the guess was correct or not.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    attempt_number is 1-based (1 on the first guess).
    """
    if outcome == "Win":
        # Win faster -> more points. A first-guess win earns the full 100.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # A wrong guess always costs 5 points, whether it was too high or too low.
    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
