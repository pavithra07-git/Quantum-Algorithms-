from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Initialize a 2-qubit circuit
n = 2
grover_circuit = QuantumCircuit(n, n)

# 2. Initialization
# Apply Hadamard gates to create a uniform superposition of all possible states (00, 01, 10, 11)
grover_circuit.h([0, 1])
grover_circuit.barrier()

# 3. The Oracle (Marking the target state)
# We want to find the state |11>. 
# A Controlled-Z (CZ) gate flips the phase of the |11> state (makes it negative).
grover_circuit.cz(0, 1)
grover_circuit.barrier()

# 4. The Diffuser (Amplitude Amplification)
# This amplifies the probability of the marked state and shrinks the others.
# Step A: Apply H gates
grover_circuit.h([0, 1])
# Step B: Apply X gates
grover_circuit.x([0, 1])
# Step C: Apply a CZ gate
grover_circuit.cz(0, 1)
# Step D: Apply X gates again
grover_circuit.x([0, 1])
# Step E: Apply H gates again
grover_circuit.h([0, 1])
grover_circuit.barrier()

# 5. Measure the qubits
grover_circuit.measure([0, 1], [0, 1])

# Optional: Draw the circuit
print("Grover's Algorithm Circuit:")
print(grover_circuit.draw())

# 6. Simulate the circuit
simulator = AerSimulator()
result = simulator.run(grover_circuit, shots=1000).result()
counts = result.get_counts(grover_circuit)

print("\nMeasurement Results:")
print(counts)
print("The quantum computer found the target state: 11")
