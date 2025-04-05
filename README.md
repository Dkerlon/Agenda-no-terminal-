# 📒 Agenda no Terminal

Uma agenda de contatos feita em Python com SQLite, executada diretamente no terminal. Permite **inserir**, **consultar**, **editar** e **deletar** contatos com nome, telefone e e-mail, utilizando um banco de dados local.

---

## 🚀 Funcionalidades

- Inserir novo contato com validação de nome e e-mail
- Deletar contatos por ID
- Atualizar nome, telefone ou e-mail
- Consultar todos os registros, por nome ou por ID
- Banco de dados local com SQLite

---

## 🧩 Estrutura

- `main.py`: interface de menu interativa com o usuário
- `cBanco.py`: contém todas as funções de manipulação do banco de dados (`insert`, `delete`, `update`, `select`, etc.)
- Banco de dados: `agenda.db`

---

## 🛠️ Requisitos

- Python 3.x
- Biblioteca `sqlite3` (inclusa no Python)

---

## ⚙️ Como usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Dkerlon/Agenda-no-terminal-.git
   cd Agenda-no-terminal-
