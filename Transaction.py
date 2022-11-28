
import uuid             #randomness
import time             #generate unique timestamp
import copy

class Transaction():
    def __init__(self, senderPublicKey: str, reciverPublicKey: str, amountOfToken: float, typeOfTransaction ) -> None:
        self.senderPublicKey = senderPublicKey
        self.reciverPublicKey = reciverPublicKey
        self.amount = amountOfToken
        self.type = typeOfTransaction
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self) -> dict:
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self) -> dict:
        # use copy method to alter the json repr. so the hash when validating the singature is the same , drop signature , to empty string
        jsonRepresentation = copy.deepcopy(self.toJson())         
        jsonRepresentation['signature'] = ""
        return jsonRepresentation

    def equals(self, transaction):
        if self.id == transaction.id:
            return True
        else:
            return False
