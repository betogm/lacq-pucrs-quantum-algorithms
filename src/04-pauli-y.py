from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Criação do circuito quântico
qcy = QuantumCircuit(1)

# Aplicação da porta Pauli-Y
qcy.y(0)

# Desenhando o circuito
fig_circuit = qcy.draw(output='mpl')

# Salva o diagrama do circuito
fig_circuit.savefig("images/pauli_y_circuit_diagram.png")

# Visualização do estado quântico no diagrama de Bloch
stateh = Statevector.from_instruction(qcy)
plot_bloch_multivector(stateh)

# Salva o diagrama do diagrama de Bloch
plt.savefig("images/pauli_y_bloch_diagram.png")

# Exibe os gráficos
plt.show()
