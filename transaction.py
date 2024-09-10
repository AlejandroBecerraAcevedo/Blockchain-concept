from data_base_chain import DataBase

class Transaction:
    def __init__(self, sender, recipient, amount, block=-1):
        # Initializes a transaction with a sender, recipient, amount, and an optional block number.
        # If no block is specified, it defaults to -1.
        self.block = block  # The block ID where the transaction is stored
        self.sender = sender  # The public key or identifier of the sender
        self.receiver = recipient  # The public key or identifier of the recipient
        self.amount = amount  # The amount of the transaction
   
    def change_id_block(self, block):
        # Changes the block ID to which the transaction is associated
        self.block = block

    def to_string(self):
        # Returns a string representation of the transaction, summarizing the sender, recipient, and amount
        return f"Transaction: {self.sender} sends {self.amount} to {self.receiver}"    
