import time
from trello_report import (
    get_client,
    get_board_and_lists,
    coletar_dados_membros,
    gerar_apresentacao,
    BOARD_ID,
    LIST_IDS
)

def main():
    start_time = time.time()

    client = get_client()
    board, listas = get_board_and_lists(client, BOARD_ID, LIST_IDS)
    membros, dados_membros, totais = coletar_dados_membros(client, board, LIST_IDS)
    gerar_apresentacao(membros, dados_membros, totais)

    end_time = time.time()
    print(f"Relatório gerado com sucesso em {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    main()
