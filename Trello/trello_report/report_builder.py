def coletar_dados_membros(client, board, list_ids):
    """
    Coleta os dados dos membros e seus cards categorizados.
    Retorna:
        - lista de membros
        - dicionário com os cards por membro
        - totais por categoria
    """
    membros = board.all_members()
    dados_membros = {}
    totais = {
        "pendente": 0,
        "andamento": 0,
        "concluido": 0,
        "correcao": 0,
        "total": 0
    }

    for membro in membros:
        crd_pendente = _get_cards(client, membro.id, list_ids["pendente"])
        crd_andamento = _get_cards(client, membro.id, list_ids["andamento"])
        crd_concluido = _get_cards(client, membro.id, list_ids["concluido"])
        crd_correcao = _get_cards(client, membro.id, list_ids["correcao"])

        dados_membros[membro] = {
            "pendente": crd_pendente,
            "andamento": crd_andamento,
            "concluido": crd_concluido,
            "correcao": crd_correcao,
            "total": sum(len(lst) for lst in [crd_pendente, crd_andamento, crd_concluido, crd_correcao])
        }

        totais["pendente"] += len(crd_pendente)
        totais["andamento"] += len(crd_andamento)
        totais["concluido"] += len(crd_concluido)
        totais["correcao"] += len(crd_correcao)
        totais["total"] += dados_membros[membro]["total"]

    return membros, dados_membros, totais


def _get_cards(client, membro_id, list_id):
    """
    Busca os cards de uma lista atribuídos a um membro específico.
    """
    lista = client.get_list(list_id)
    cards = lista.list_cards()
    return [card for card in cards if membro_id in getattr(card, "member_id", [])]
