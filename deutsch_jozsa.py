from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random

def get_balanced_oracle(n):
    """
    Creates a balanced oracle.
    Returns 0 for half the inputs and 1 for the other half.
    """
    oracle_qc = QuantumCircuit(n + 1)
    # Apply CNOT gates to entangle the input qubits with the target qubit
    for qubit in range(n):
        oracle_qc.cx(qubit, n)
    return oracle_qc

def get_constant_oracle(n):
    """
    Creates a constant oracle.
    Returns either all 0s or all 1s for every input.
    """
    oracle_qc = QuantumCircuit(n + 1)
    # Randomly decide if the constant output should be 0 or 1
    output = random.choice(['0', '1'])
    if output == '1':
        # If output is 1, apply an X-gate to the target qubit
        oracle_qc.x(n)
    # If output is 0, we do nothing (Identity)
    return oracle_qc

# 1. Setup variables (using 3 input qubits)
n = 3 
dj_circuit = QuantumCircuit(n + 1, n)

# 2. Initialization
# Put the target qubit into the |1> state using an X-gate
dj_circuit.x(n)

# Apply Hadamard (H) gates to all qubits to create a massive superposition
for qubit in range(n + 1):
    dj_circuit.h(qubit)

# 3. Apply the Oracle (Choose ONE to test)
# oracle = get_balanced_oracle(n)
oracle = get_constant_oracle(n) # We are testing the constant oracle here

dj_circuit.compose(oracle, inplace=True)

# 4. Apply H-gates to the input qubits again to create interference
for qubit in range(n):
    dj_circuit.h(qubit)

# 5. Measure the input qubits
for i in range(n):
    dj_circuit.measure(i, i)

# 6. Simulate the circuit
simulator = AerSimulator()
result = simulator.run(dj_circuit, shots=1000).result()
counts = result.get_counts(dj_circuit)



# Print the results
print("Measurement Results:", counts)
if '0' * n in counts and counts['0' * n] == 1000:
    print("Conclusion: The function is CONSTANT.")
else:
    print("Conclusion: The function is BALANCED.")
