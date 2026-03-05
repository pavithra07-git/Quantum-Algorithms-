from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Define the secret string we want the quantum computer to find
secret_string = "1011"
n = len(secret_string)

# Create a Quantum Circuit with n query qubits and 1 target qubit
bv_circuit = QuantumCircuit(n + 1, n)

# 2. Initialization
# Put the target qubit (the last one) into the |1> state
bv_circuit.x(n)

# Apply Hadamard gates to all qubits to create superposition
bv_circuit.h(range(n + 1))
bv_circuit.barrier() # Visual separator

# 3. Apply the Oracle (The Black Box)
# Qiskit orders qubits from right-to-left, so we reverse the string for the loop
for i, bit in enumerate(reversed(secret_string)):
    if bit == '1':
        # Apply a CNOT gate from the query qubit to the target qubit
        bv_circuit.cx(i, n)
        
bv_circuit.barrier() # Visual separator

# 4. Apply Hadamard gates to the query qubits again
bv_circuit.h(range(n))

# 5. Measure the query qubits
bv_circuit.measure(range(n), range(n))

# Optional: Draw the circuit to the console
print("Bernstein-Vazirani Circuit:")
print(bv_circuit.draw())

# 6. Simulate the circuit
simulator = AerSimulator()
result = simulator.run(bv_circuit, shots=1000).result()
counts = result.get_counts(bv_circuit)

print("\nMeasurement Results:")
print(counts)
print(f"The quantum computer found the secret string: {list(counts.keys())[0]}")
