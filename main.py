from Wallet import Wallet
from TransactionPool import TransactionPool


if __name__ == '__main__':
    
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    typeOfTransaction= 'TRANSACTION'
    
    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(receiver, amount, typeOfTransaction)
 
    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    print(pool.transactions)