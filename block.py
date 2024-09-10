from root_hash import Get_tree_root_hash
from utils import Hashing
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, difficulty=3):
        # Initializes a block with an index, a list of transactions, the previous block's hash,
        # a nonce (set to 0 initially), and the difficulty of mining.
        self.index = index  # Block index in the blockchain
        self.transactions = transactions  # List of transactions included in the block
        self.previous_hash = previous_hash  # Hash of the previous block in the chain
        self.nonce = 0  # Counter used for mining the block
        self.merkle_root = self.update_merkle_root()  # Generate the Merkle root from the transactions
        self.hash_block = self.calculate_hash()  # Calculate the block's hash
        self.difficulty = difficulty  # The mining difficulty (number of leading zeros in the hash)
        

    def calculate_hash(self):
        # Concatenate the block's attributes into a string format to prepare for hashing
        block_content = (
            str(self.index) + 
            str(self.previous_hash) + str(self.merkle_root) +
            str(self.nonce)
        )
        # Apply the SHA-256 hashing algorithm to the concatenated string and return the result as a hexadecimal hash
        return Hashing(block_content).hash.__str__()
    
    def update_merkle_root(self):
        # Generate the Merkle root from the transactions using the Get_tree_root_hash class
        root_hash = Get_tree_root_hash(self.transactions)
        root_hash.transactions = self.transactions  # Assign the transactions to the Merkle tree
        root_hash.get_MerkleRoot()  # Calculate the Merkle root of the transaction set
        self.merkle_root = root_hash.merkle_root  # Update the block's Merkle root with the calculated value
        return self.merkle_root
    

    def mine_block(self):
        # Create a target string representing the mining difficulty (e.g., 3 leading zeros for difficulty=3)
        target = '0' * self.difficulty  # Target hash with a number of leading zeros equal to difficulty
        
        print(f"Mining block... with difficulty {self.difficulty}")
        start_time = time.time()  # Record the start time of the mining process
        
        # Increment the nonce and recalculate the block's hash until it meets the target difficulty
        while self.hash_block[:self.difficulty] != target:
            self.nonce += 1
            self.hash_block = self.calculate_hash()  # Update the block's hash
        
        end_time = time.time()  # Record the end time when the block is successfully mined
        
        # Print the mining results: the block's final hash, nonce, and total mining time
        print(f"Block successfully mined!\nHash: {self.hash_block}\nNonce: {self.nonce}\nTime: {end_time - start_time:.2f} seconds\n")

