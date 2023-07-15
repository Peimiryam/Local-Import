from ast import literal_eval

import os

def load_inventory(name_file):
    try:
        with open(name_file, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("I'm sorry, file not found. Creating a new file. . .")
        return {}
    
def save_inventory(name_file,inventory):
    with open(name_file, 'w') as file:
        file.write(str(inventory))

def save_history(history):
    path = os.path.join(os.getcwd(), "log.txt")
    with open(path, 'w') as fp:  
        fp.write((str(f"Log: {history}")))

def save_balance(balance_account):
    path = os.path.join(os.getcwd(), "balance.txt")
    with open(path, 'w') as fp:
        fp.write(str(f"Total Balance: {balance_account}"))
