from utils import Hashing, RandomWords

class Wallet:
    def __init__(self, name, private_key):
        self._private_key = Hashing(name + private_key).hash.__str__()
        self.public_key = Hashing(self._private_key).hash.__str__()   
        self.balance = 0       
        
        self.transactions = []

    def set_transaction(self, transaction):
        self.transactions.append(transaction)
    def get_public_key(self):
        self.public_key = Hashing(self._private_key)
        
    
    def get_private_key(self):
        return self._private_key
        
    def get_balance(self):
        return len(self.balance)
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

