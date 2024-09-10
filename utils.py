import hashlib
import random

class RandomWords:
    def __init__(self):
        # A list of predefined words
        self.words = [
            "apple", "banana", "grape", "orange", "lemon", "cherry", "strawberry", "blueberry", 
            "watermelon", "peach", "pear", "plum", "pineapple", "mango", "kiwi", "papaya", 
            "coconut", "lime", "pomegranate", "raspberry", "blackberry", "fig", "date", 
            "apricot", "nectarine", "melon", "tangerine", "grapefruit", "avocado", "cucumber",
            "carrot", "broccoli", "cauliflower", "spinach", "lettuce", "cabbage", "onion",
            "garlic", "potato", "tomato", "pepper", "cucumber", "zucchini", "eggplant"
        ]        
        
        self.random_words = self.concatenate()
       
    # A string containing three randomly selected words concatenated together
    def get_random_words(self):
        return random.sample(self.words, 3)
    
    # concatenated words
    def concatenate(self):
        self.random_words = self.get_random_words()
        return " ".join(self.random_words)

# generating a SHA-256 hash from an input string.
class Hashing:
    def __init__(self, dataIn):
        self.data = dataIn
        self.hash = self.hashing_code() # Generates the hash during initialization

    def hashing_code(self):
        # Datos de entrada
        data_encode = self.data.encode()  # Convert string to bytes

        # Create SHA-256 hash object
        sha256_hash = hashlib.sha256()

        # Update hash with data
        sha256_hash.update(data_encode)

        # Generate final hash
        hash_final = sha256_hash.hexdigest()

        # Return hex hash

        return hash_final
    

