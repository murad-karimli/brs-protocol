import random

class TrisectionProtocol:
    def __init__(self, secret_angle):
        self.secret_angle = secret_angle
        self.trisection = round(secret_angle / 3, 2)

    def respond_to_challenge(self, challenge):
        if challenge == "angle":
            return self.secret_angle
        elif challenge == "trisection":
            return self.trisection
        else:
            return None

def interactive_authentication(rounds=5):
    secret_angle = random.randint(30, 150)
    prover = TrisectionProtocol(secret_angle)

    print(f"Prover has chosen a secret angle. You will now verify them by asking {rounds} questions.")

    for i in range(1, rounds + 1):
        print(f"--- Round {i} ---")
        challenge = input("Type your challenge (angle/trisection): ").strip().lower()

        if challenge not in ["angle", "trisection"]:
            print("Invalid challenge. Try again.")
            return False

        correct_answer = prover.secret_angle if challenge == "angle" else prover.trisection
        response = prover.respond_to_challenge(challenge)

        print(f"Prover's response: {response}°")

        if response != correct_answer:
            print("Incorrect response. Auth failed.")
            return False
        else:
            print("Correct response.")

    print("Auth succeeded,Prover is verified.")
    return True

interactive_authentication()
