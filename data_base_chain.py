from wallet import Wallet
from utils import Hashing, RandomWords
from block import Block


class DataBase:
    def __init__(self):        
        self.wallets = []
        self.blocks = []
        self.transactions = []
    
    def add_transaction(self, transaction):
        print(f"\nTransaction added with block: {transaction.block}")
        print(f"Transaction added with sender: {transaction.sender}")
        print(f"Transaction added with recipient: {transaction.receiver}")
        print(f"Transaction added with amount: {transaction.amount} \n")
        self.transactions.append(transaction)
    
    def add_wallet(self, wallet):
        print(f"Your wallet has been created successfully!")
        self.wallets.append(wallet)
        
    
    def add_block(self, block):
        print(f"Block added with hash_block: {block.hash_block}")
        print(f"Block added with merkle root: {block.merkle_root}")
        
        for transaction in block.transactions:
            print("Block added with transactions: ")
            print(f"   Sender: {transaction.sender}")
            print(f"   Recipient: {transaction.receiver}")
            print(f"   Amount: {transaction.amount}")
            print("\n")
        print(f"Block added with index: {block.index}")
        print(f"Block added with previous hash: {block.previous_hash}")
        print(f"Block added with nonce: {block.nonce}")
        print(f"Block added with difficulty: {block.difficulty} \n")

        
        self.blocks.append(block)
        
    def get_wallet_by_public_key(self, public_key):
        for wallet in self.wallets:
            if wallet.public_key == public_key:
                return wallet
        return None
    def wallet_exists(self, public_key):
        for wallet in self.wallets:
            if wallet.public_key == public_key:
                return True
        return False
    def get_transactions(self):
        return self.transactions
    
    def check_balance(self, public_key):
        wallet = self.get_wallet_by_public_key(public_key)
        return wallet.balance
    def walletSenderBalance(self, public_key):
        wallet = self.get_wallet_by_public_key(public_key)
        return wallet.balance

    def get_wallets(self):
        return self.wallets
    
    def get_transaction_by_block(self, block):
        for transaction in self.transactions:
            if transaction.block == block:
                return transaction
        return None
    def get_block_by_hash(self, hash_block):
        for block in self.blocks:
            if block.hash_block == hash_block:
                return block
        return None
    def get_previous_block(self):
        return self.blocks[-1]
    def get_blocks(self):
        return self.blocks
    
    



# Example usage
'''
    db = DataBase()
    wallet1 = Wallet()
    wallet2 = Wallet()
    wallet3 = Wallet()
'''

