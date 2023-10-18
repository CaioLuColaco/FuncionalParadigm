import inquirer
from inquirer.themes import GreenPassion
import os

pasta = "../storage"
arquivo = "dadosQ2.txt"
caminho_completo = os.path.join(pasta, arquivo)
newLogin = ""

read_data = lambda caminho_completo: dict(
    map(lambda linha: linha.strip().split(": "), open(caminho_completo, "r"))
) if os.path.exists(caminho_completo) else {}

create_directory = (lambda dir: os.makedirs(dir) if not os.path.exists(dir) else None)(pasta)

dados = read_data(caminho_completo)

questions = [
    inquirer.List(
        'cadastrado',
        message="Você já possui cadastro?",
        choices=['Sim', 'Não'],
    ),
]

answers = inquirer.prompt(questions, theme=GreenPassion())

register_user = (
    lambda: (
        (print("Vamos fazer o seu cadastro.\n"), dados.__contains__(newLogin) and print("Você já possui cadastro!"))
        if newLogin in dados
        else (
            (newPass := input("Qual será a sua senha?\n")),
            dados.update({newLogin: newPass}),
            (lambda file: file.writelines([f"{login}: {senha}\n" for login, senha in dados.items()]))(open(caminho_completo, "w"))
        )
    )
)

newLogin = (lambda: input("Qual será o seu login?\n") if answers['cadastrado'] == "Não" else None)()
(lambda: register_user() if answers['cadastrado'] == "Não" else None)()

print("\nLogin\n")
print("Preencha os seus dados:\n")
login = input("Login: ")
password = input("Senha: ")

(lambda: print("Login realizado com sucesso!") if login in dados and dados[login] == password else print("Login ou senha incorretos"))()