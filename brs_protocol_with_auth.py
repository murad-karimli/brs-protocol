import random

class BRSProtocol:
    def __init__(self, secret_angle):
        self.secret_angle = secret_angle
        self.trisection = round(secret_angle/3,2)


    def commit(self):
        return {
            "angle":self.secret_angle,
            "trisection":self.trisection
        }


    def respond_to_challenge(self,challenge):
        if challenge=="show_angle":
            return self.secret_angle
        elif challenge=="show_trisection":
            return self.trisection
        else:
            return None


def authenticate_prover(prover,rounds=10):
    print("Burmester-Rivest-Shamir Authentication Protocol\n")
    print(f"prover has secret angle and will tested {rounds} rounds\n")


    for i in range(1,rounds+1):
        print(f"--- Round {i} ---")
        challenge=random.choice(["show_angle","show_trisection"])
        print(f"verifier's chelenge:{challenge.replace('_', ' ').capitalize()}")



        expected=prover.secret_angle if challenge=="show_angle" else prover.trisection
        response=prover.respond_to_challenge(challenge)


        if response!=expected:
            print("auth failed:incorrect")
            return False
        else:
            print(f"correct response:{response}°\n")

    print("prover authenticated successful\n")
    return True

def simulate_authentication():
    secret_angle=random.randint(30,150)
    prover=BRSProtocol(secret_angle)
    authenticated=authenticate_prover(prover,rounds=10)
    print("Auth result:","SUCCESS" if authenticated else "FAILURE")

simulate_authentication()
