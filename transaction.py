from data_base_chain import DataBase


class Transaction:
    def __init__(self, sender, recipient, amount, block = -1):
        self.block = block
        self.sender = sender
        self.receiver = recipient
        self.amount = amount
   
    def change_id_block(self, block):
        self.block = block

    def to_string(self):
        return f"Transaction: {self.sender} sends {self.amount} to {self.receiver}"    
    
    
