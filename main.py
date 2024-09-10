from wallet import Wallet
from block import Block
from transaction import Transaction
from data_base_chain import DataBase
from utils import Hashing, RandomWords

# Initialize the blockchain database
db = DataBase()

class main:
    def __init__(self):
        # Initialize the main application class with a flag for the initial state
        self.initial = False

        # If the initial flag is False, call the initialize function to create the genesis block
        if self.initial:
            pass
        else:
            self.initialize()

    def initialize(self):
        # Create the genesis block (the first block in the blockchain) and add it to the database
        block0 = Block(0, {}, "0" * 64, 5)  # Block with index 0, empty transactions, and initial difficulty of 5
        db.add_block(block0)
        self.initial = True  # Set the initial flag to True after initialization

# Create an instance of the main class to start the application
run_app = main()

# Infinite loop to display the menu and handle user choices
while(True):
    print("\n1. Create Wallet")
    print("2. Deposit")
    print("3. Send Coin")
    print("4. Mine Block")
    print("5. Check Blockchain")
    print("6. My Transactions")
    print("7. Check Balance")
    print("8. Exit")
    
    choice = str(input("Enter your choice: "))

    if choice == "1":
        # Create a new wallet for the user
        name = input("Enter your Username: ")
        randomWords = RandomWords().get_random_words()  # Generate random words for wallet security
        wallet = Wallet(name, "".join(randomWords))  # Create a wallet with username and random words
        db.add_wallet(wallet)  # Add the new wallet to the database

        # Display the public key, balance, and generated words
        print(f"\nPublic Key: {wallet.public_key}")            
        print(f"Balance: {wallet.balance}")        
        print("Your words are: ", " ".join(randomWords))
        print("Save them somewhere safe \n")
    
    elif choice == "2":
        # Handle deposit transactions
        public_key = input("Enter your public key: ")
        amount = int(input("Enter amount: "))
        wallet = db.get_wallet_by_public_key(public_key)

        # Check if the wallet exists and deposit the amount
        if wallet:
            wallet.deposit(amount)
            print(f"Deposited {amount} tokens to {public_key}")
            print(f"New balance: {wallet.balance}")
        else:
            print("Invalid Address")
        
        print("\n")

    elif choice == "3":
        # Handle coin transfers between wallets
        sender = input("Enter sender's address: ")
        receiver = input("Enter receiver's address: ")
        amount = int(input("Enter amount: "))
        transaction = Transaction(sender, receiver, amount)  # Create a transaction

        # Check if both wallets exist and if the sender has enough balance
        if db.wallet_exists(sender) and db.wallet_exists(receiver):
            if db.check_balance(sender) >= amount:
                # Perform the transfer by updating balances and recording the transaction
                db.get_wallet_by_public_key(sender).deposit(-amount)
                db.get_wallet_by_public_key(receiver).deposit(amount)
                db.add_transaction(transaction)
                print("Transaction Successful")
                db.get_wallet_by_public_key(sender).set_transaction(transaction)
                db.get_wallet_by_public_key(receiver).set_transaction(transaction)
            else:
                print("Insufficient tokens")
            print(f"Balance remaining for sender: {db.walletSenderBalance(sender)}")
        else:
            print("Invalid Address")
        
        print("\n")
    
    elif choice == "4":
        # Mine a new block containing the pending transactions
        difficulty = int(input("Enter difficulty: "))
        result = [transaction for transaction in db.get_transactions() if transaction.block == -1]

        # Check if there are any pending transactions to mine
        if len(result) == 0:
            print("No pending transactions")
            print("\n")
            continue
        
        # Prepare the transactions for the new block
        transactions = []
        for transaction in result:
            transaction.change_id_block(db.get_previous_block().index + 1)
            transactions.append(transaction)
        
        # Create and mine the new block
        block = Block(db.get_previous_block().index + 1, transactions, db.get_previous_block().hash_block, difficulty)
        block.mine_block()
        db.add_block(block)
        
        print("\n")
    
    elif choice == "5":
        # Display the details of each block in the blockchain
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
        # Display the transactions associated with a specific wallet
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
        # Check the balance of a wallet by its public key
        public_key = input("Enter your public key: ")
        wallet = db.get_wallet_by_public_key(public_key)
        if wallet:
            print(f"Balance: {wallet.balance}")
        else:
            print("Invalid Address")
        
        print("\n")
    
    elif choice == "8":
        # Exit the application
        break
    
    else:
        print("Invalid Choice")
        print("\n")
