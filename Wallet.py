from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction



class Wallet():
    def __init__(self) -> None:
        self.keyPair = RSA.generate(2048)

    def sign(self, data: dict)-> hex:
        # this method hashes the data (json format) and signs the hashed data with the signatureSchemeObject, after it returns the signature in hex format
        
        dataHash = BlockchainUtils.hash(data) 
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)            # if provided both keys, this method can sign and validate
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

    @staticmethod
    def singatureValid(data: dict, signature: any, publicKeyString: str): 
        # this method validates if the hased data correspons to the publicKey and returns a validation status 

        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)           # if only provide public key, method can only validate data
        signatureValid = signatureSchemeObject.verify(dataHash, signature)
        return signatureValid

    def publicKeyString(self) -> bool:
        # generate a string representation of the public key through the Crypto library, exported as binary and decoded as a string 
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString

    def createTransaction(self, receiver, amount, type):
        transaction = Transaction(
            self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction