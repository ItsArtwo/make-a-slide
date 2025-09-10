from board_id import board_id, pendente_ID, andamento_ID, concluido_ID, correcao_ID

API_KEY = 'api key'
TOKEN = 'token'
BOARD_ID = board_id # ID do quadro do Trello
LIST_IDS = {
    "pendente": pendente_ID, # ID da lista "Pendente"
    "andamento": andamento_ID , # ID da lista "Em Andamento"
    "concluido": concluido_ID, # ID da lista "Concluído"
    "correcao": correcao_ID # ID da lista "Correção"
}

print(f'BOARD_ID: {BOARD_ID}')

for i in LIST_IDS:
    print(f'{i} ID: {LIST_IDS[i]}')
