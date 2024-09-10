from utils import Hashing, RandomWords

class Wallet:
    def __init__(self, name, private_key):
        # Creates a wallet using the provided name and private key. The private key is hashed,
        # and a public key is derived by hashing the private key again. The initial balance is set to 0.
        self._private_key = Hashing(name + private_key).hash.__str__()  # Hashes the name and private key to generate the private key
        self.public_key = Hashing(self._private_key).hash.__str__()  # Generates a public key by hashing the private key
        self.balance = 0  # The wallet's starting balance is 0
        
        # A list to store all the transactions related to this wallet
        self.transactions = []

    def set_transaction(self, transaction):
        # Adds a transaction to the wallet's transaction list
        self.transactions.append(transaction)
    
    def get_public_key(self):
        # Updates the public key by hashing the private key again
        self.public_key = Hashing(self._private_key)
    
    def get_private_key(self):
        # Returns the private key of the wallet
        return self._private_key
        
    def get_balance(self):
        # Returns the balance of the wallet (length of the balance list, though this seems like an error)
        return len(self.balance)
    
    def deposit(self, amount):
        # Adds a specified amount to the wallet's balance and returns the updated balance
        self.balance += amount
        return self.balance
