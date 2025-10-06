from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Criação do circuito quântico com 1 qubit e 1 bit clássico para medição
qcx = QuantumCircuit(1, 1)

# Inicializa o qubit no estado |0> (padrão)
print("Matriz de entrada (vetor de estado |0>):", Statevector.from_label('0').data)

# Aplica a porta Pauli-X para inverter o qubit para |1>
qcx.x(0)

# Adiciona a medição do qubit no bit clássico
qcx.measure(0, 0)

# Desenha o circuito, indicando entrada |0> e saída |1> com medição
fig_circuit = qcx.draw(output='mpl')
fig_circuit.savefig("images/pauli_x_circuit_diagram.png")

# Simula o circuito para obter o vetor de estado após a porta X (antes da medição)
stateh = Statevector.from_instruction(qcx.remove_final_measurements(inplace=False))
print("Matriz de saída (vetor de estado após Pauli-X):", stateh.data)

# Visualiza o estado quântico no diagrama de Bloch
plot_bloch_multivector(stateh)
plt.savefig("images/pauli_x_bloch_diagram.png")

# Exibe os gráficos
plt.show()
