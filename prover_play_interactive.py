import random

class TrisectionProtocol:
    def __init__(self, secret_angle):
        self.secret_angle = secret_angle
        self.trisection = round(secret_angle / 3, 2)

def prover_respond_interactively():
    print("Interactive BRS Protocol: You Are the Prover")
    secret_angle = random.randint(30, 150)
    prover = TrisectionProtocol(secret_angle)

    print("The verifier will challenge you for 5 rounds.")
    print("You must answer either the original angle or its trisection.")
    print("Don't reveal both values! You don't know which challenge is coming next.")
    print("Your goal: Pass all challenges to be authenticated.")

    for i in range(1, 6):
        print(f"--- Round {i} ---")
        challenge = random.choice(["angle", "trisection"])
        print(f"Verifier's challenge: Show {challenge}")

        user_input = input("Your response (in degrees): ").strip()

        try:
            user_value = float(user_input)
        except ValueError:
            print("Invalid input. Must be a number. Authentication failed.")
            return False

        correct_value = prover.secret_angle if challenge == "angle" else prover.trisection

        if abs(user_value - correct_value) < 0.01:
            print("Correct")
        else:
            print(f"Incorrect. Expected {correct_value}°, but got {user_value}°.")
            print("Authentication failed.")
            return False

    print("You were authenticated successfully!")
    return True

prover_respond_interactively()
