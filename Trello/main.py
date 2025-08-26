#Chave de API: a2ffb6570256b8afa8d0262596294e36
#Token: ATTA71a7e45fb51ca2bd4c24dd8d44a032c98a778e0ff331eb6f70130e3ec24e8a31AAFA42DF
#Segredo: 26d688ac575f0f8fd0d52ad54f4958b82966b8c8ce8f6e2ba2256f75574bd594



#Classe usuário se pá? guardar as infos

from trello import TrelloClient

client = TrelloClient(
    api_key='a2ffb6570256b8afa8d0262596294e36',
    token='ATTA71a7e45fb51ca2bd4c24dd8d44a032c98a778e0ff331eb6f70130e3ec24e8a31AAFA42DF'
)

#----------Criar listas-------------
board_ID_list = []
list_ID_list = []
card_ID_list = []

#------Escolher um board---------------------

boards = client.list_boards() #faz um json?
for i, board in enumerate(boards, start=0):
    board_ID_list.append(board.id)
    print(f"Board {i}: {board.name} | ID: {board.id}")
board_ID = int(input("Choose a board "))
board = client.get_board(board_ID_list[board_ID])


#------Mostrar e escolher uma lista---------------------

#lists = board.list_lists()
lists = board.list_lists()
for i, lst in enumerate(lists, start=0):
    list_ID_list.append(lst.id)
    print(f"Lista {i}: {lst.name} | ID: {lst.id}")
escolha_Listas = int(input("Choose a list "))
list = board.get_list(list_ID_list[escolha_Listas])


#----------------------Mostrar e escolher uma cards-------------------------

cards = list.list_cards()
for i, card in enumerate(cards, start=0):
    card_ID_list.append(card)
    for member_id in card.member_id:
        member = client.get_member(member_id)
        print(f"Card {i}: {card.name} | ID: {card.id} | Member: {member.full_name} - {card.member_id}" )
escolha_Cards = int(input("Choose a card "))
card = card_ID_list[escolha_Cards]


# Pegue a lista de destino
target_list = board.get_list('66ddcdc0176ed00c5c401bbe')

# Mova o card para a nova lista
card.change_list(target_list.id)

print(f"Card '{card.name}' movido para a lista '{target_list.name}' com sucesso.")