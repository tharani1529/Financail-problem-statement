
import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
        #create the genesis Blockchain
        self.new_block(previous_hash='1', proof=100)
       
    def new_block(self,proof,previous_hash=None):
            block = {
          'index': len(self.chain) + 1,
          'timestamp': time(),
          'transactions': self.current_transactions,
          'proof': proof,
          'previous_hash': previous_hash or self.hash(self.chain[-1])
      }
            self.current_transactions = []
            self.chain.append(block)
            return block
      
    def new_transactions(self,sender,recipient,amount):
      # add a new transaction to the list of transactions
      self.current_transactions.append({
          'sender':sender,
          'recipient':recipient,
          'amount': amount
      })
      
      return self.last_block['index'] + 1
      
      
      @staticmethod
      def hash(block):
     # we must maku sure that the dictionary is ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block,sort_keys=True.encode())
        return hashlib,sha256(block_string).hexdigest()
      
      @property
      def last_block(self):
         return self.chain[-1]
          
      def proof_of_work(self,last_proof):
           proof=0
           while self.valid_proof(last_proof,proof) is false:
                proof+=1
                return proof
          
    @staticmethod
    def valid_proof(last_proof,proof):
           guess = f'{last_proof}{proof}'.encode()
           guess_hash = hashlib.sha256(guess).hexdigest()
           return guess_hash[:4] =="0000"
           
           #Instantiate our Blockchain
           blockchain = Blockchain()
           
           #create a transaction
           blockchain.new_transaction("john Doe","Jane Doe",100)
           
           #Mine the new block
           last_block = blockchain.last_block
           last_proof = last_block['proof']
           proof = blockchain.new_block(proof,previous_hash)
           
           
           print("new block added to the chain.")
           print