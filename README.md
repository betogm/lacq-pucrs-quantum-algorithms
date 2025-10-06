# lacq-pucrs-quantum-algorithms

Studies of quantum logic gates and algorithms using Qiskit

Este é um projeto de exemplo para demonstrar o uso do [Qiskit](https://qiskit.org/), um SDK de código aberto para trabalhar com computadores quânticos.

---

## 📋 Pré-requisitos

- Python **3.8** ou superior  
- [pip](https://pip.pypa.io/en/stable/) (geralmente vem instalado com o Python)

---

## ⚙️ Configuração do Ambiente

Para garantir que as dependências deste projeto não entrem em conflito com outros projetos em sua máquina, utilizamos um **ambiente virtual (venv)**.  
Siga os passos abaixo para configurar o ambiente.

### 1. Clone o Repositório

```bash
git clone git@github.com:betogm/lacq-pucrs-quantum-algorithms.git
cd lacq-pucrs-quantum-algorithms
```

### 2. Crie o Ambiente Virtual

```bash
python3 -m venv venv
. ./venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Teste os scripts

```bash
python src/01-circuito-inicial.py
python src/02-hadamard.py
python src/03-pauli-x.py
python src/04-pauli-y.py
python src/04-pauli-y-x.py
python src/05-pauli-z.py
python src/06-pauli-z-x.py
```

## Contribua com esse projeto no GitHub!

- 1. Crie um Fork desse repositório
- 2. Faça alterações, adições ou correções no código
- 3. Crie um commit (ainda em seu fork) descritivo
- 4. Abra um Pull Request para este projeto

