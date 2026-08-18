import pytest

from main import determine_winner


@pytest.mark.parametrize(
    ("player_choice", "computer_choice", "expected"),
    [
        ("rock", "scissors", "player"),
        ("paper", "rock", "player"),
        ("scissors", "paper", "player"),
        ("lizard", "spock", "player"),
        ("spock", "scissors", "player"),
        ("rock", "paper", "computer"),
        ("scissors", "rock", "computer"),
        ("lizard", "paper", "player"),
        ("spock", "lizard", "computer"),
        ("rock", "rock", "tie"),
    ],
)
def test_determine_winner(player_choice, computer_choice, expected):
    assert determine_winner(player_choice, computer_choice) == expected
