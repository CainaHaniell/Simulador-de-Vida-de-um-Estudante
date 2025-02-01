import time

print("+" + "-" * 53 + "+")
print("|  Bem vindo ao simulator school" + " " * 22 + "|")
print("|  Aqui vamos simular uma vida de um jovem estudante." + " " * 1 + "|")
nomealuno = input("|  Digite Seu nome:")
print("|  Você virou o aluno " + nomealuno + " " * (32 - len(nomealuno)) + "|")
print("+" + "-" * 53 + "+\n")

time.sleep(2.5)
print(f"{nomealuno} está saindo de casa e acenou para o seu joão")
time.sleep(2.5)
print("Seu joão acenou devolta!")
time.sleep(1.5)
print(f"{nomealuno} Chegou na escola")
time.sleep(2)
print("Bem vindo ao IFSERTAO-PE")
time.sleep(1.5)

while True:
    print("--- Ações ---")
    time.sleep(1)
    print("1 - Assistir a aula\n2 - Faltar a aula\n3 - Sair do simulador")
    opcao = int(input("Digite a opção desejada: "))
    print("")

    if opcao == 1:
        print("Que bom que você decidiu assistir à aula! Aguarde um pouco, pois a professora teve um imprevisto.")
        time.sleep(2)
        print("A professora entrou na sala.")
        time.sleep(1)
        print("A professora disse: Bom dia alunos")
        bomdia = input("Diga Bom Dia para a professora: ")
        print(f"{nomealuno} disse {bomdia}\n")
        print("Olá, pessoal! Sou a Carol Silva, a nova professora de vocês. Vou dar aulas de Redes.")
        print("E aí, pessoal! Vamos nos conhecer? Formem um círculo pra gente começar!\n")
        time.sleep(2)
        print("Carol conheçe cada um dos seus novos alunos.")
        print("Pessoal, peguem seus caderno pois que vou começar a dar aula.")
        time.sleep(1)
        print("")

        while True:
            print("\nO que você vai fazer?")
            print("1 - Pegar o caderno")
            print("2 - Fingir que pegou o caderno")
            print("3 - Dizer que esqueceu em casa")
            acao = int(input(""))

            if acao == 1:
                print(
                    "Excelente! Sua atitude proativa te diferencia. Você é um exemplo a ser seguido!")
                break
            elif acao == 2:
                print("A consciência do aluno: As anotações são como um mapa do tesouro do conhecimento.\nSem elas, vou me perder no caminho")
                break
            elif acao == 3:
                print("A mente do aluno: 'Por que eu menti? Eu nem precisava disso! Agora a professora vai achar que eu sou desonesto.'")
                break
            else:
                print("Opcao incorreta.")
    elif opcao == 2:
        print("Você decidiu faltar a aula. E está passeando nos corredores")
        time.sleep(2)
        print("O diretor te viu e perguntou o que você está fazendo fora da sala de aula.")
        time.sleep(1.5)
        print("Você mentiu e disse que estava indo ao banheiro.")
        time.sleep(1.5)
        print("O diretor viu que era mentira e te mandou para a sala de aula.")
        time.sleep(1.5)
        print("Você foi para a sala de aula e a professora te perguntou o motivo de ter faltado a aula.")
        time.sleep(1.5)
        print("Você ficou sem saber o que dizer e a professora te mandou para a diretoria.")
        print("Você foi para a diretoria e o diretor te deu uma advertência.")
        print("")
    else:
        print("Saindo do simulador...")
        break
