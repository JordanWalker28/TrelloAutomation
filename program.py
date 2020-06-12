from trello import TrelloClient
import requests

api_key=''
token=''

client = TrelloClient(
    api_key='',
    token=''
)

def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": api_key, "token": token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id
    
def create_card(list_id, card_name):
    url = "https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

all_boards = client.list_boards()
last_board = all_boards[-1]
print(last_board.name)

print(all_boards[0].name)

lists = all_boards[0].all_lists()
print(lists)

all_boards[1].add_label("concept", "blue")

create_board("test")
