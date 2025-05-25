import random

class TrisectionProtocol:
    def __init__(self,secret_angle):
        self.secret_angle=secret_angle
        self.trisection=round(secret_angle/3,2)

def prover_respond_interactively():
    print("BRS Protocol:You Are a Prover")
    secret_angle=random.randint(30,150)
    prover=TrisectionProtocol(secret_angle)

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

        correct_value=prover.secret_angle if challenge=="angle" else prover.trisection

        if abs(user_value-correct_value)<0.01:
            print("Correct")
        else:
            print(f"Incorrect. Expected {correct_value}°,but got {user_value}°.")
            print("Auth failed.")
            return False

    print("You were authenticated successfully!")
    return True

prover_respond_interactively()
