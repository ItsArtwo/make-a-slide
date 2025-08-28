from trello import TrelloClient
from trello_report.config import API_KEY, TOKEN

def get_client():
    return TrelloClient(api_key=API_KEY, token=TOKEN)

def get_board_and_lists(client, board_id, list_ids):
    board = client.get_board(board_id)
    listas = {
        nome: client.get_list(list_id)
        for nome, list_id in list_ids.items()
    }
    return board, listas
