from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Criação do circuito quântico
qcx = QuantumCircuit(1)

# Aplicação da porta Pauli-X
qcx.x(0)

# Desenhando o circuito
fig_circuit = qcx.draw(output='mpl')

# Salva o diagrama do circuito
fig_circuit.savefig("images/pauli_x_circuit_diagram.png")

# Visualização do estado quântico no diagrama de Bloch
stateh = Statevector.from_instruction(qcx)
plot_bloch_multivector(stateh)

# Salva o diagrama do diagrama de Bloch
plt.savefig("images/pauli_x_bloch_diagram.png")

# Exibe os gráficos
plt.show()
