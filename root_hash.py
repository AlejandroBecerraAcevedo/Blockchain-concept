from utils import Hashing
import json

class Get_tree_root_hash():

    def __init__(self, transactions):
        self.tree = []
        self.transactions = transactions    # Datos de entrada   
        self.merkle_root = ""     
    

    def build_tree(self):
        level_tree = []
        for transaction in self.transactions:
            level_tree.append(Hashing(transaction.to_string()).hash.__str__())                       
        self.tree.append(level_tree)
        print(level_tree)
        

        n_level_tree = int(len(level_tree)/2)

        if (len(level_tree)%2 != 0):
            n_level_tree = n_level_tree +1
        
        for e in range(0, n_level_tree):
            
            level_tree = []
            long = len(self.tree[e])

            if (len(self.tree[e])%2 != 0):
                level_tree.append(self.tree[0][-1])
                long = len(self.tree[e])-1
                
            
            for i in range(0, long, 2):            
                level_tree.append(Hashing(self.tree[e][i] + self.tree[e][i+1]).hash.__str__())           
            self.tree.append(level_tree)
            print(level_tree)
           
            

            if (len(level_tree) == 1):
                self.merkle_root = level_tree[0]
                print("Merkle root: ", self.merkle_root, "\n")
                break 

    def get_MerkleRoot(self):
        self.build_tree()
        
    

# Example usage
'''
    root_hash = Get_tree_root_hash( {"1": "User1 sends 2 BTC to User2", "2": "User2 sends 2 BTC to User3", "3": "User3 sends 2 BTC to User4", "4": "User4 sends 2 BTC to User5"})
    root_hash.build_tree()


    for i in range(len(root_hash.tree)):
        print(root_hash.tree[i], "\n")
'''