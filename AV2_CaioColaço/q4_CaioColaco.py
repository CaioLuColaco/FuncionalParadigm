import mysql.connector
from dotenv import load_dotenv
import os
import inquirer
from inquirer.themes import GreenPassion

load_dotenv()

db_connection = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"),
    port=os.getenv("PORT"),
)
print("Database connected!")

cursor = db_connection.cursor()


createUser = lambda nome, console : cursor.execute("INSERT INTO usuarios (nome, console) VALUES (%s, %s)", (nome, console))

findUsers = lambda : cursor.execute("SELECT * FROM usuarios")

deleteUsers = lambda id : cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))

createJogo = lambda nome, data_lancamento : cursor.execute("INSERT INTO jogos (nome, data_lancamento) VALUES (%s, %s)", (nome, data_lancamento))

findJogos = lambda : cursor.execute("SELECT * FROM jogos")

deleteJogos = lambda id : cursor.execute("DELETE FROM jogos WHERE id = %s", (id,))


findUsers()
users = [(id, nome, console) for (id, nome, console) in cursor]

findJogos()
jogos = [(id, nome, console) for (id, nome, console) in cursor]

questions = [
    inquirer.List(
        'action',
        message="Oque você deseja fazer?",
        choices=['Cadatrar novo usuário', 'Buscar usuários', 'Apagar usuário', 'Cadatrar novo jogo', 'Buscar jogo', 'Apagar jogo' ],
    ),
]

answers = inquirer.prompt(questions, theme=GreenPassion())

input_user = lambda: (input("Qual o nome?\n"), input("Qual o console?\n"))
nomeUser, consoleUser = (lambda: input_user() if answers['action'] == "Cadatrar novo usuário" else (None, None))()
idUser = (lambda: int(input("Qual o id do usuário a ser deletado?\n")) if answers['action'] == "Apagar usuário" else None)()


input_jogo = lambda: (input("Qual o nome do jogo?\n"), input("Qual a data?\n"))
nomeJogo, lancamento = (lambda: input_jogo() if answers['action'] == "Cadatrar novo jogo" else (None, None))()
idJogo = (lambda: int(input("Qual o id do jogo a ser deletado?\n")) if answers['action'] == "Apagar jogo" else None)()

(lambda: createUser(nomeUser, consoleUser) if answers['action'] == "Cadatrar novo usuário" else None)()
(lambda: print(users) if answers['action'] == "Buscar usuários" else None)()
(lambda: deleteUsers(idUser) if answers['action'] == "Apagar usuário" else None)()

(lambda: createJogo(nomeJogo, lancamento) if answers['action'] == "Cadatrar novo jogo" else None)()
(lambda: print(jogos) if answers['action'] == "Buscar jogo" else None)()
(lambda: deleteJogos(idJogo) if answers['action'] == "Apagar jogo" else None)()

cursor.close()
db_connection.commit()
db_connection.close()