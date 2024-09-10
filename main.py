from wallet import Wallet
from block import Block
from transaction import Transaction
from data_base_chain import DataBase
from utils import Hashing, RandomWords


db = DataBase()

class main:
    def __init__(self):

        self.initial = False

        if self.initial:
            pass
        else:
            self.initialize()

    def initialize(self):
        
        block0 = Block(0, {}, "0"*64, 5)
        db.add_block(block0)
        self.initial = True
    
run_app = main()


while(True):
    print("\n1. Create Wallet")
    print("2. Deposit")
    print("3. Send Coin")
    print("4. mine block")
    print("5. Check BlockChain")
    print("6. My transactions")
    print("7. check balance")
    print("8. Exit")
    
    choice = str(input("Enter your choice: "))

    if choice == "1":        
        
        name = input("Enter your Username: ")
        randomWords = RandomWords().get_random_words()
        
        wallet = Wallet(name, "".join(randomWords))  

        db.add_wallet(wallet)
        


        print(f"\nPublic Key: {wallet.public_key}")            
        print(f"Balance: {wallet.balance}")        
        print("Your words are: ", " ".join(randomWords))
        print("save them somewhere safe \n")
    
    elif choice == "2":
        public_key = input("Enter your public key: ")
        amount = int(input("Enter amount: "))
        wallet = db.get_wallet_by_public_key(public_key)

        if wallet:
            wallet.deposit(amount)
            print(f"Deposited {amount} tokens to {public_key}")
            print(f"New balance: {wallet.balance}")
        else:
            print("Invalid Address")
        
        print("\n")

    elif choice == "3":
        sender = input("Enter sender's address: ")
        receiver = input("Enter receiver's address: ")
        amount = int(input("Enter amount: "))
        transaction = Transaction(sender, receiver, amount)

        if db.wallet_exists(sender) and db.wallet_exists(receiver):
            if db.check_balance(sender) >= amount:
                db.get_wallet_by_public_key(sender).deposit(-amount) 
                db.get_wallet_by_public_key(receiver).deposit(amount)               
                db.add_transaction(transaction)                
                print("Transaction Successful")
                db.get_wallet_by_public_key(sender).set_transaction(transaction)
                db.get_wallet_by_public_key(receiver).set_transaction(transaction)
                
            else:
                print("Insufficient tokens")
            print(f"balance result to sender: {db.walletSenderBalance(sender)}")
        else:
            print("Invalid Address")
        
        print("\n")
    elif choice == "4":
        difficulty = int(input("Enter difficulty: "))
        result = [transaction for transaction in db.get_transactions() if transaction.block == -1]
        if len(result) == 0:
            print("No pending transactions")
            print("\n")
            continue
        transactions = []
        
        for transaction in result:
            transaction.change_id_block(db.get_previous_block().index + 1)
            transactions.append(transaction)
            

        
        block = Block(db.get_previous_block().index + 1, transactions, db.get_previous_block().hash_block, difficulty)
        block.mine_block()
        db.add_block(block)
        
        print("\n")
    elif choice == "5":
        for block in db.get_blocks():
            print(f"Block: {block.index}")
            print(f"Hash: {block.hash_block}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Merkle Root: {block.merkle_root}")
            print(f"Nonce: {block.nonce}")
            print(f"Difficulty: {block.difficulty}")
            print(f"Transactions: {block.transactions}")
            print("\n")
        
    elif choice == "6":
        public_key = input("Enter your public key: ")
        wallet = db.get_wallet_by_public_key(public_key)
        if wallet:
            print("Transactions:")
            for transaction in wallet.transactions:
                print(f"Block: {transaction.block}")
                print(f"Sender: {transaction.sender}")
                print(f"Recipient: {transaction.receiver}")
                print(f"Amount: {transaction.amount}")
                print("\n")
        else:
            print("Invalid Address")
        
        print("\n")
    elif choice == "7":
        public_key = input("Enter your public key: ")
        wallet = db.get_wallet_by_public_key(public_key)
        if wallet:
            print(f"Balance: {wallet.balance}")
        else:
            print("Invalid Address")
        
        print("\n")
    elif choice == "8":
        break
        
    else:
        print("Invalid Choice")
        print("\n")




