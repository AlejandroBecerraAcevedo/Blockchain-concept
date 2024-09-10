import hashlib
import random

class RandomWords:
    def __init__(self):
        self.words = [
            "apple", "banana", "grape", "orange", "lemon", "cherry", "strawberry", "blueberry", 
            "watermelon", "peach", "pear", "plum", "pineapple", "mango", "kiwi", "papaya", 
            "coconut", "lime", "pomegranate", "raspberry", "blackberry", "fig", "date", 
            "apricot", "nectarine", "melon", "tangerine", "grapefruit", "avocado", "cucumber",
            "carrot", "broccoli", "cauliflower", "spinach", "lettuce", "cabbage", "onion",
            "garlic", "potato", "tomato", "pepper", "cucumber", "zucchini", "eggplant"
        ]        
        
        self.random_words = self.concatenate()
       

    def get_random_words(self):
        return random.sample(self.words, 3)

    def concatenate(self):
        self.random_words = self.get_random_words()
        return " ".join(self.random_words)

class Hashing:
    def __init__(self, dataIn):
        self.data = dataIn
        self.hash = self.hashing_code()      

    def hashing_code(self):
        # Datos de entrada
        data_encode = self.data.encode()  # Convertimos la cadena a bytes

        # Crear un objeto hash SHA-256
        sha256_hash = hashlib.sha256()

        # Actualizar el objeto hash con los datos
        sha256_hash.update(data_encode)

        # Obtener el valor hash en formato hexadecimal
        hash_final = sha256_hash.hexdigest()

        #print(f"El hash SHA-256 de {self.data} es: {hash_final} \n")

        return hash_final
    

