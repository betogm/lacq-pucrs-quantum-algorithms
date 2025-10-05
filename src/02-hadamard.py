from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Criação do circuito quântico
qch = QuantumCircuit(1)

# Aplicação da porta Hadamard 
qch.h(0)

# Desenhando o circuito
fig_circuit = qch.draw(output='mpl')

# Salva o diagrama do circuito
fig_circuit.savefig("images/hadamard_circuit_diagram.png")

# Visualização do estado quântico no diagrama de Bloch
stateh = Statevector.from_instruction(qch)
plot_bloch_multivector(stateh)

# Salva o diagrama do diagrama de Bloch
plt.savefig("images/hadamard_bloch_diagram.png")

# Exibe os gráficos
plt.show()
