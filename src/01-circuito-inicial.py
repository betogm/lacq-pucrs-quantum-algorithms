from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Criação do circuito quântico
qch = QuantumCircuit(1)

# Desenhando o circuito
fig_circuit = qch.draw(output='mpl')

# Visualização do estado quântico no diagrama de Bloch
stateh = Statevector.from_instruction(qch)
plot_bloch_multivector(stateh)

# Salva o diagrama do circuito
fig_circuit.savefig("images/circuit_diagram.png")

# Salva o diagrama do diagrama de Bloch
plt.savefig("images/circuit_bloch_diagram.png")

# Exibe os gráficos
plt.show()
