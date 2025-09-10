#GET https://api.trello.com/1/boards/BOARD_ID/lists?key=SEU_API_KEY&token=SEU_TOKEN
import requests
from trello_report.config import API_KEY, TOKEN

url = "https://api.trello.com/1/members/me/boards"

params = {
    "key": API_KEY,
    "token": TOKEN
}

response = requests.get(url, params=params)

if response.status_code == 200:
    boards = response.json()
    print("Seleciona um dos boards abaixo. ")
    for i, board in enumerate(boards, start=1):
        print(f"Nome: {board['name']} | ID: {board['id']} | {i}")
        print("--" * len(boards[i-1]))

    while True:         # Loop até o usuário fornecer uma entrada válida
        escolha_id = int(input("Digite o número do board escolhido: "))

        if escolha_id < 1 or escolha_id > len(boards): #conferir se o número é válido
            print("Número inválido. Tente novamente.")
            print("-"*37)
            continue
        
        confirmar = input(f"ID do board selecionado: {boards[escolha_id-1]['id']}. Confirmar? (s/n): ").strip().lower() #confirmação da escolha_id

        if confirmar == 's':
            #---------------------------------------
            board_id = boards[escolha_id - 1]['id'] #Define a escolha e ajusta o número da escolha_id ao indice correto
            print("+-" * 37 + "+")
            print(f"Board ID confirmado: {board_id}")
            #---------------------------------------

            #Definir list_id's
            pendente_ID = boards[escolha_id - 1]['lists'][0]['id']
            andamento_ID = boards[escolha_id - 1]['lists'][1]['id']
            concluido_ID = boards[escolha_id - 1]['lists'][2]['id']
            correcao_ID = boards[escolha_id - 1]['lists'][3]['id']

        else:
            print("-"*37)


else:
    print("Erro ao buscar boards:", response.status_code) 