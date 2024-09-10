from transaction import Transaction

transaction = Transaction("sender", "receiver", 100)

print(transaction.to_string())