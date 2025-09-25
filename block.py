import hashlib

class Block:
    # Initialises the block with a timestamp, data, previous hash and proof of work
    def __init__(self, timestamp, data, previous_hash, proof_of_work):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.proof_of_work = proof_of_work
    
    # Returns the Block as a JSON string
    def __repr__(self):
        return f'{{"timestamp": "{self.timestamp}", "data": "{self.data}", "previous_hash": "{self.previous_hash}", "proof_of_work": {self.proof_of_work}}}'
        
    
    # Gets the SHA-256 hash of the block
    def get_hash(self):
        encoded_block_string = self.__repr__().encode("utf-8")
        return hashlib.sha256(encoded_block_string).hexdigest()
    
    

