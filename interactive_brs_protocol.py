import random

class TrisectionProtocol:
    def __init__(self, secret_angle):
        self.secret_angle=secret_angle
        self.trisection=round(secret_angle/3,2)

    def respond_to_challenge(self, challenge):
        if challenge=="angle":
            return self.secret_angle
        elif challenge=="trisection":
            return self.trisection
        else:
            return None


def interactive_authentication(rounds=5):
    secret_angle=random.randint(30,150)
    prover=TrisectionProtocol(secret_angle)



    for i in range(1,rounds+1):
        print(f"--- Round {i} ---")

        challenge=input("type your chelenge (angle/trisection): ").strip().lower()


        if challenge not in ["angle", "trisection"]:
            print("invalid chalenge.Try again.")
            return False

        correct_answer=prover.secret_angle if challenge=="angle" else prover.trisection
        response=prover.respond_to_challenge(challenge)

        print(f"prover response: {response}°")

        if response != correct_answer:
            print("incorrect response. Auth failed.")
            return False
        else:
            print("correct")

    print("auth succeeded,prover is verified.")
    return True

interactive_authentication()
