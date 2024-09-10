from wallet import Wallet
from utils import Hashing, RandomWords
from block import Block

class DataBase:
    def __init__(self):        
        # Initializes the database with empty lists to store wallets, blocks, and transactions
        self.wallets = []
        self.blocks = []
        self.transactions = []
    
    def add_transaction(self, transaction):
        # Adds a transaction to the transaction list and prints its details
        print(f"\nTransaction added with block: {transaction.block}")
        print(f"Transaction added with sender: {transaction.sender}")
        print(f"Transaction added with recipient: {transaction.receiver}")
        print(f"Transaction added with amount: {transaction.amount} \n")
        self.transactions.append(transaction)
    
    def add_wallet(self, wallet):
        # Adds a wallet to the wallet list and prints a success message
        print(f"Your wallet has been created successfully!")
        self.wallets.append(wallet)
        
    def add_block(self, block):
        # Adds a block to the block list and prints its details, including all transactions in the block
        print(f"Block added with hash_block: {block.hash_block}")
        print(f"Block added with merkle root: {block.merkle_root}")
        
        for transaction in block.transactions:
            # Prints details of each transaction in the block
            print("Block added with transactions: ")
            print(f"   Sender: {transaction.sender}")
            print(f"   Recipient: {transaction.receiver}")
            print(f"   Amount: {transaction.amount}")
            print("\n")
        # Prints additional block details such as index, previous hash, nonce, and difficulty
        print(f"Block added with index: {block.index}")
        print(f"Block added with previous hash: {block.previous_hash}")
        print(f"Block added with nonce: {block.nonce}")
        print(f"Block added with difficulty: {block.difficulty} \n")

        self.blocks.append(block)  # Adds the block to the block list
        
    def get_wallet_by_public_key(self, public_key):
        # Searches for and returns a wallet by its public key, or None if not found
        for wallet in self.wallets:
            if wallet.public_key == public_key:
                return wallet
        return None
    
    def wallet_exists(self, public_key):
        # Checks if a wallet with the given public key exists
        for wallet in self.wallets:
            if wallet.public_key == public_key:
                return True
        return False
    
    def get_transactions(self):
        # Returns the list of all transactions
        return self.transactions
    
    def check_balance(self, public_key):
        # Returns the balance of a wallet identified by its public key
        wallet = self.get_wallet_by_public_key(public_key)
        return wallet.balance
    
    def walletSenderBalance(self, public_key):
        # Alias for checking the balance of a sender's wallet by its public key
        wallet = self.get_wallet_by_public_key(public_key)
        return wallet.balance

    def get_wallets(self):
        # Returns the list of all wallets
        return self.wallets
    
    def get_transaction_by_block(self, block):
        # Searches for and returns a transaction by the block it belongs to
        for transaction in self.transactions:
            if transaction.block == block:
                return transaction
        return None
    
    def get_block_by_hash(self, hash_block):
        # Searches for and returns a block by its hash value
        for block in self.blocks:
            if block.hash_block == hash_block:
                return block
        return None
    
    def get_previous_block(self):
        # Returns the last block in the block list (the most recent one)
        return self.blocks[-1]
    
    def get_blocks(self):
        # Returns the list of all blocks
        return self.blocks
