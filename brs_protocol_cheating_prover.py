import random

class BRSProtocol:
    def __init__(self,secret_angle, honest=True):
        self.secret_angle=secret_angle
        self.trisection=round(secret_angle/3,2)
        self.honest=honest

    def respond_to_challenge(self, challenge):
        if not self.honest and random.random() < 0.1:
            if challenge == "show_angle":
                return self.secret_angle+random.randint(1,5)
            elif challenge == "show_trisection":
                return self.trisection+ round(random.uniform(0.5,3),2)
        else:
            if challenge=="show_angle":
                return self.secret_angle
            elif challenge=="show_trisection":
                return self.trisection
            else:
                return None

def authenticate_prover(prover, rounds=10):
    print("Burmester-Rivest-Shamir Authentication Protocol\n")
    print(f"prover will tested in {rounds} rounds\n")

    for i in range(1, rounds + 1):
        print(f"--- Round {i} ---")
        challenge = random.choice(["show_angle","show_trisection"])
        print(f"verifier's chalenge: {challenge.replace('_', ' ').capitalize()}")



        expected=prover.secret_angle if challenge=="show_angle" else prover.trisection
        response=prover.respond_to_challenge(challenge)


        if abs(response-expected)>0.01:
            print(f"Auth failed: Incorrect response {response}°,expected {expected}°\n")
            return False
        else:
            print(f"correct response: {response}°\n")

    print("prover authenticeted successfully\n")
    return True

def simulate_authentication(honest=True):
    secret_angle = random.randint(30,150)


    prover = BRSProtocol(secret_angle,honest=honest)
    authenticated = authenticate_prover(prover,rounds=10)
    print("auth result:", "SUCCESS" if authenticated else "FAILURE")

simulate_authentication(honest=False)
