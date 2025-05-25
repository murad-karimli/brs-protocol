# Burmester-Rivest-Shamir Identification Protocol

## Goal

Simulate the Burmester-Rivest-Shamir (BRS) identification and authentication protocol using **angle trisection** as the Prover's secret. This is a conceptual demonstration of **zero-knowledge proof** where identity is verified without revealing the entire secret.

---

## Background

In classical geometry, **trisecting an arbitrary angle** using only a compass and straightedge is known to be **impossible in general**. This limitation forms the base for the BRS identification protocol: the Prover knows a trisectable angle and proves it without disclosing the method.

---

## Idea

- The **Prover** knows a secret angle θ.
- The **Verifier** can challenge them to:
  - Reveal θ (the full angle), or
  - Reveal θ/3 (the trisection).
- The Prover only answers **one of the questions** each round, not both.
- After many rounds, the verifier can be sure (or like almost sure) the Prover knows the secret.

It shows a basic **zero-knowledge proof** logic where nothing secret is revealed but still convinces the other person.

---

## Protocol Steps

1. Prover picks a secret angle (like 120°).
2. Prover calculates the trisection (like 40°).
3. Verifier asks one of:
   - "Show me the angle"  
   - OR "Show me the trisection"
4. Prover answers only the one asked.
5. Repeat multiple rounds so cheating is unlikely.

---

## Code Overview

I wrote a few Python programs for this.

### 1. `brs_protocol_with_auth.py`  
Does the whole thing: identification plus 10 rounds of authentication. Random challenges each time, fails if one response is wrong.

### 2. `interactive_brs_protocol.py`  
You become the **Verifier**. You type either `angle` or `trisection`, and the Prover (the code) answers you. It's like playing with it.

### 3. `prover_play_interactive.py`  
You are the **Prover** now. The program asks you questions and you have to type the correct response. If you're wrong, it says you failed.

### 4. `brs_protocol_cheating_prover.py`  
This one is special. I added a version where the Prover is *not honest*. They guess sometimes (10% chance of giving a wrong answer).  
It shows how someone who doesn't actually know the secret will eventually be caught if you repeat the protocol enough times.

---

## Notes

- This BRS thing is like a simple idea to show **zero-knowledge proof**.
- It’s based on geometry stuff, not really used in real-life crypto but it’s still cool.
- You can explain that you never give both values (angle + trisection) in one round, so the Verifier never learns the full secret.
- If someone cheats, over time their answers won’t match and they fail.

---

## Files

- `brs_protocol_with_auth.py` – Full protocol with authentication
- `interactive_brs_protocol.py` – You act as the Verifier
- `prover_play_interactive.py` – You act as the Prover
- `brs_protocol_cheating_prover.py` – Fake Prover that sometimes lies
- `README.md` – This document 

---

## Conclusion

This whole project is about how someone can prove they know something **without revealing it**.  
We used angle trisection to simulate that.  
It was actually fun to make, and helped me understand how zero-knowledge proofs kinda work.  
