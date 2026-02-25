# Quantum-Algorithms-
It contains the different types of the Quantum Algorithms and it's demonstration with the following python language.
# ⚛️ Quantum Algorithms

A collection of quantum computing algorithms and circuits implemented in Python using Qiskit. This repository documents my hands-on exploration of quantum computing, from fundamental entanglement to advanced quantum speedups. 

The code here is designed to be simulated locally using `qiskit_aer`, but is perfectly formatted to be deployed on real quantum hardware via the IBM Quantum Platform.

---

## 🗂️ Algorithms Included

### 🔹 The Deutsch-Jozsa Algorithm
**File:** `deutsch_jozsa.py`

The Deutsch-Jozsa algorithm demonstrates a clear, exponential separation between classical and quantum computing power. It determines whether a hidden boolean function (an "oracle") is **Constant** (returns all 0s or all 1s) or **Balanced** (returns half 0s, half 1s) in exactly **1 query**, taking advantage of quantum superposition and interference.
* **Key Concepts:** Quantum Oracles, Superposition, Quantum Interference.


*(More algorithms will be added here as the journey continues!)*

---

## 🚀 Getting Started

Today, I am exploring the **Deutsch-Jozsa algorithm**, a famous quantum algorithm that solves a specific problem exponentially faster than any classical computer.

## 🧠 The Problem: The Black Box

Imagine a hidden function (a "black box" or "oracle"):

$$f: \{0,1\}^n \rightarrow \{0,1\}$$

You are guaranteed this function is either:
* **Constant:** It returns the exact same value (all 0s or all 1s) for every input.
* **Balanced:** It returns $0$ for half of the inputs, and $1$ for the other half.

A classical computer has to check multiple inputs to figure out if it is constant or balanced. The Deutsch-Jozsa quantum algorithm figures it out in exactly **1 query**!

## 🛠️ The Quantum Circuit



1. Initialize $n$ query qubits to $|0\rangle$ and $1$ target qubit to $|1\rangle$.
2. Apply Hadamard gates to create superposition.
3. Apply the hidden Oracle.
4. Apply Hadamard gates again to create quantum interference.
5. Measure the query qubits.

## 🚀 How to Run the Code

**1. Install Dependencies**
First, install the required libraries using the provided requirements file:
`pip install -r requirements.txt`

**2. Run the Script**
Execute the Python file to simulate the algorithm:
`python deutsch_jozsa.py`

## 📊 Expected Output

If the function is **constant**, the result is always all zeros (e.g., `000`). 
If the function is **balanced**, the result is anything *except* all zeros (e.g., `111`).

Because the code in this repository builds a "balanced" oracle, your output will look like this:
```text
Measurement Results: {'111': 1000}
Conclusion: The function is BALANCED.


