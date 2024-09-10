from utils import Hashing
import json

class Get_tree_root_hash():

    def __init__(self, transactions):
        # Initialize the class with a list to store the tree structure and input transactions
        self.tree = []
        self.transactions = transactions    # Input transactions data
        self.merkle_root = ""   # Store the Merkle root (root hash) of the tree
    

    def build_tree(self):
        # Create the first level of the tree by hashing each transaction
        level_tree = []
        
        for transaction in self.transactions:
            # Hash each transaction and convert it to a string, then add to the first level of the tree
            level_tree.append(Hashing(transaction.to_string()).hash.__str__())                       
        self.tree.append(level_tree)  # Add the first level (transaction hashes) to the tree
        print(level_tree)  # Print the first level of the Merkle tree
        

        # Calculate the number of pairs of hashes for the next level
        n_level_tree = int(len(level_tree) / 2)

        # If the number of transactions is odd, add one more level
        if (len(level_tree) % 2 != 0):
            n_level_tree += 1
        
        # Build subsequent levels of the Merkle tree
        for e in range(0, n_level_tree):
            
            level_tree = []  # Create a new level in the tree
            long = len(self.tree[e])  # Get the length of the current level

            # If the current level has an odd number of elements, duplicate the last element
            if (len(self.tree[e]) % 2 != 0):
                level_tree.append(self.tree[0][-1])
                long = len(self.tree[e]) - 1
                
            # Iterate through pairs of hashes and combine them to create the next level
            for i in range(0, long, 2):            
                level_tree.append(Hashing(self.tree[e][i] + self.tree[e][i+1]).hash.__str__())           
            self.tree.append(level_tree)  # Add the new level to the tree
            print(level_tree)  # Print the newly created level of the tree
           
            # If the new level contains only one element, it is the Merkle root
            if (len(level_tree) == 1):
                self.merkle_root = level_tree[0]  # Set the Merkle root
                print("Merkle root: ", self.merkle_root, "\n")
                break  # Stop once the Merkle root is found

    def get_MerkleRoot(self):
        # Public method to build the Merkle tree and retrieve the Merkle root
        self.build_tree()
