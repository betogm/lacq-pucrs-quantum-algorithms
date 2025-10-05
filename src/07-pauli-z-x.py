from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Criação do circuito quântico
qcz = QuantumCircuit(1)

# Visualização do estado quântico no diagrama de Bloch
stateh = Statevector.from_instruction(qcz)
plot_bloch_multivector(stateh)

# Todos os estados no Qiskit iniciam em ∣0⟩, por isso aplicamos X
# Inverte o estado 
qcz.x(0)

# Aplicação da porta Pauli-Z
qcz.z(0)

# Desenhando o circuito
fig_circuit = qcz.draw(output='mpl')

# Salva o diagrama do circuito
fig_circuit.savefig("images/pauli_z-x_circuit_diagram.png")

# Visualização do estado quântico no diagrama de Bloch
stateh = Statevector.from_instruction(qcz)
plot_bloch_multivector(stateh)

# Salva o diagrama do diagrama de Bloch
plt.savefig("images/pauli_z-x_bloch_diagram.png")

# Exibe os gráficos
plt.show()
