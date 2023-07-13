from ast import literal_eval

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
    with open(r'C:/Users/miria/OneDrive/Desktop/Importfile/log.txt', 'w') as fp:
        #fp.write("\n".join(str(history)))    
        fp.write((str(history)))

def save_balance(balance_account):
    with open(r'C:/Users/miria/OneDrive/Desktop/Importfile/balance.txt', 'w') as fp:
        fp.write(str(f"Total Balance: {balance_account}"))
