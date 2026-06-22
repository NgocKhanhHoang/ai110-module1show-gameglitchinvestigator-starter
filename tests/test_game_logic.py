import pytest

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- High/Low bug fix ---------------------------------------------------------
# The glitch: the "Too High"/"Too Low" hints were swapped, so guessing ABOVE the
# secret told the player to go HIGHER (and vice versa). These tests pin the
# direction of both the outcome label and the user-facing arrow message so the
# swap cannot silently come back.

@pytest.mark.parametrize(
    "guess, secret, expected_outcome",
    [
        (60, 50, "Too High"),   # guess above secret -> Too High
        (51, 50, "Too High"),   # just above the boundary
        (100, 1, "Too High"),   # far above
        (40, 50, "Too Low"),    # guess below secret -> Too Low
        (49, 50, "Too Low"),    # just below the boundary
        (1, 100, "Too Low"),    # far below
    ],
)
def test_high_low_outcome_direction(guess, secret, expected_outcome):
    outcome, _ = check_guess(guess, secret)
    assert outcome == expected_outcome


def test_too_high_tells_player_to_go_lower():
    # A guess above the secret must steer the player DOWN, not up.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_tells_player_to_go_higher():
    # A guess below the secret must steer the player UP, not down.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()
