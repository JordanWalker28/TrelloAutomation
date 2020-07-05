
from tkinter import *
from tkinter import ttk
from trello import TrelloClient
import requests


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
    
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
    
def clickMe():
    boardName = name.get()
    create_board(boardName)

#last_board = all_boards[-1]
#print(last_board.name)

#print(all_boards[0].name)

#lists = all_boards[0].all_lists()
#print(lists)

#all_boards[1].add_label("concept", "blue")

#create_board("randomTest")

root = Tk()
root.title("Tk dropdown example")
root.geometry('300x400')
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 2)
mainframe.rowconfigure(0, weight = 2)
mainframe.pack(padx = 0, pady = 0)


# Create a Tkinter variable
tkvar = StringVar(root)

all_boards = client.list_boards()
boardList = []

for i in all_boards:
    boardList.append(i)
print(list)

boardList = list(dict.fromkeys(boardList))
print(boardList)
# Dictionary with options
choices = boardList
tkvar.set(choices[-1]) # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
tkvar.trace('w', change_dropdown)
Label(mainframe, text="Choose a Board:").grid(row = 0, column = 1)
popupMenu.grid(row = 1, column =1)

# link function to change dropdown
tkvar.trace('w', change_dropdown)

label = ttk.Label(mainframe, text = "Create Board:").grid(column = 0, row = 2)

name = StringVar()
nameEntered = ttk.Entry(mainframe, width = 15, textvariable = name)
nameEntered.grid(column = 1, row = 2)

button = ttk.Button(mainframe, text = "Click Me", command = clickMe).grid(column= 2, row = 2)


root.mainloop()

del boardList, tkvar, root
