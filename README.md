# Burmester-Rivest-Shamir Identification Protocol

## Goal

Simulate the Burmester-Rivest-Shamir (BRS) identification and authentication protocol using **angle trisection** as the Prover's secret. This is a conceptual demonstration of **zero-knowledge proof** where identity is verified without revealing the entire secret.

---

## Background

In classical geometry, **trisecting an arbitrary angle** using only a compass and straightedge is known to be **impossible in general**. This geometric limitation forms the basis for the BRS identification protocol: the Prover knows a trisectable angle and proves it without disclosing the method.

---

## Idea

- The **Prover** knows a secret angle θ.
- The **Verifier** can challenge them to:
  - Reveal θ (the full angle), or
  - Reveal θ/3 (a correct trisection).
- The Prover only responds to **one challenge per round**, never both.
- Repeating this interaction reduces the chance of cheating.

This setup simulates a **zero-knowledge identification scheme**.

---

## Protocol Steps

1. Prover selects a secret angle (e.g., 120°).
2. Prover computes its trisection (e.g., 40°).
3. Verifier challenges with either:
   - "Show me the angle"  
   - or "Show me the trisection"
4. Prover responds correctly.
5. Repeat the process over multiple rounds.

---

## Code Overview

The project includes **four Python programs**:

### 1. `brs_protocol.py`  
Simulates a basic 5-round identification protocol using automated random challenges and prover responses.

### 2. `brs_protocol_with_auth.py`  
Includes a full **authentication system**: runs 10 rounds of randomized challenge-response, and authenticates if all responses are correct.

### 3. `interactive_brs_protocol.py`  
**Interactive Verifier Mode**: You play the verifier. In each round, you type `angle` or `trisection`, and the prover responds automatically.

### 4. `prover_play_interactive.py`  
**Interactive Prover Mode**: The system plays the verifier. You act as the prover and must type the correct responses manually (based on your secret).

---


## Notes for Presentation

- BRS protocol is a **conceptual example** of a **zero-knowledge proof**.
- Emphasize the role of **geometric impossibility** in making this proof meaningful.
- Highlight how **interactive protocols** simulate real-world identity verification without secret leakage.
- In real-world systems, such ideas are implemented using **cryptographic primitives** (e.g., ZK-SNARKs, Fiat-Shamir).

---

## Files

- `brs_protocol_with_auth.py` – Full authentication with automated challenge-response  
- `interactive_brs_protocol.py` – Interactive verifier mode  
- `prover_play_interactive.py` – Interactive prover mode  
- `README.md` – The documentation

---

## Conclusion

This project demonstrates how a **zero-knowledge identification protocol** can be constructed from a purely geometric impossibility. It emphasizes the balance between proving knowledge and preserving secrecy — a concept widely used in modern cryptography.
