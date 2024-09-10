from root_hash import Get_tree_root_hash
from utils import Hashing
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, difficulty=3):
        self.index = index
        self.transactions = transactions        
        self.previous_hash = previous_hash        
        self.nonce = 0
        self.merkle_root = self.update_merkle_root()
        self.hash_block = self.calculate_hash()
        self.difficulty = difficulty
        

       
    def calculate_hash(self):
        # Concatenate the block's attributes into a string
        block_content = (
                            str(self.index) + 
                            str(self.previous_hash) + str(self.merkle_root) +
                            str(self.nonce)
                         )
        # Apply the SHA-256 algorithm to the string and return the hexadecimal hash
        
        return Hashing(block_content).hash.__str__()
    
    def update_merkle_root(self):
        root_hash = Get_tree_root_hash(self.transactions)
        root_hash.transactions = self.transactions
        root_hash.get_MerkleRoot()
        self.merkle_root = root_hash.merkle_root
        return self.merkle_root
    

    def mine_block(self):
        # Create a target string that represents the difficulty
        target = '0' * self.difficulty #000 difficulty =  3
        
        print(f"Mining block... with difficulty {self.difficulty}")
        start_time = time.time()
        
        # Keep incrementing the nonce until the hash meets the difficulty
        while self.hash_block[:self.difficulty] != target:
            self.nonce += 1
            self.hash_block = self.calculate_hash()
        
        end_time = time.time()        
        
        print(f"Block successfully mined!\nHash: {self.hash_block}\nNonce: {self.nonce}\nTime: {end_time - start_time:.2f} seconds\n")

# Example usage

'''
    transactions = {"send": "67 coin"}
    block = Block(index=1, transactions=transactions, timestamp=time.time(), previous_hash="0000000000000000000", difficulty=3)

    # Mine the block with a difficulty of 3 leading zeros
    block.mine_block()

'''
