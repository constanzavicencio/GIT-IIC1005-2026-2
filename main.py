import random

RULES = {
    "rock": {"scissors", "lizard"},
    "paper": {"rock", "spock"},
    "scissors": {"paper", "lizard"},
    "lizard": {"paper", "spock"},
    "spock": {"rock", "scissors"},
}

ALIASES = {
    "rock": {"rock", "piedra"},
    "paper": {"paper", "papel"},
    "scissors": {"scissors", "tijeras"},
    "lizard": {"lizard", "lagarto"},
    "spock": {"spock"},
}


def normalize_choice(choice):
    if not isinstance(choice, str):
        return None

    normalized = choice.strip().lower()
    for canonical, aliases in ALIASES.items():
        if normalized in aliases:
            return canonical
    return None


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    if computer_choice in RULES.get(player_choice, set()):
        return "player"

    return "computer"


def get_computer_choice():
    return random.choice(list(RULES.keys()))


def get_user_choice():
    while True:
        option = input(
            "Elige una opción: rock / paper / scissors / lizard / spock: "
        ).strip()
        normalized = normalize_choice(option)

        if normalized is not None:
            return normalized

        print("Opción inválida. Inténtalo de nuevo.")


def play_round():
    player_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    print(f"Tu elección: {player_choice}")
    print(f"Elección de la computadora: {computer_choice}")

    if result == "tie":
        print("Empate.")
    elif result == "player":
        print("¡Ganaste esta ronda!")
    else:
        print("La computadora ganó esta ronda.")

    return result


def juego():
    print("Bienvenido a Rock, Paper, Scissors, Lizard, Spock")
    print("Reglas:")
    print("- rock gana a scissors y lizard")
    print("- paper gana a rock y spock")
    print("- scissors gana a paper y lizard")
    print("- lizard gana a paper y spock")
    print("- spock gana a rock y scissors")

    rounds_to_play = 0
    while rounds_to_play <= 0:
        try:
            rounds_to_play = int(
                input("¿Cuántas rondas quieres jugar? Ingresa un número positivo: ")
            )
        except ValueError:
            print("Debes ingresar un número válido.")

    player_score = 0
    computer_score = 0

    for _ in range(rounds_to_play):
        result = play_round()
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

    print("\nResultado final:")
    print(f"Tu puntaje: {player_score}")
    print(f"Puntaje de la computadora: {computer_score}")

    if player_score > computer_score:
        print("¡Felicidades! Ganaste el juego.")
    elif computer_score > player_score:
        print("La computadora ganó. ¡Suerte para la próxima!")
    else:
        print("El juego terminó en empate.")


if __name__ == "__main__":
    juego()