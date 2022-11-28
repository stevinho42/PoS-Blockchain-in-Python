


class TransactionPool():
    def __init__(self) -> None:
        self.transactions = []

    def addTransaction(self, transaction) -> None:
        self.transactions.append(transaction)

    def transactionExists(self, transaction):
        # check if this transaction already exists
        for poolTransaction in self.transactions:
            if poolTransaction.equals(transaction):
                return True
            else:
                False