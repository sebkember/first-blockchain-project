from block import Block
import datetime

class Blockchain:
    # For the proof of work, the hash of the block must start with 4 leading zeros
    MINING_DIFFICULTY = "0000"

    # Initialises the blockchain with a genesis block
    def __init__(self):
        # The list which stores a chain of block objects
        self.chain = []

        # Create the genesis block
        genesis_block = Block(timestamp=datetime.datetime.now(),
                               data="Genesis Block",
                               previous_hash="0",
                               proof_of_work=0)
        
        # Add the genesis block to the chain
        self.chain.append(genesis_block)
    
    def __repr__(self):
        block_str = ""
        for block in self.chain:
            block_str += block.__repr__() + "\n-->\n"
        
        return block_str

    # Adds a new block to the chain
    def add_block(self, block):
        # Add a block to the chain
        self.chain.append(block)
    
    # Gets the last block in the blockchain
    def get_last_block(self):
        return self.chain[-1]
    
    # Checks if the blockchain is valid
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
        
            # Check if the hash matches
            if (previous_block.get_hash() != current_block.previous_hash):
                return False
        
            # Check if proof of work is valid
            if (current_block.get_hash()[:len(self.MINING_DIFFICULTY)] != self.MINING_DIFFICULTY):
                return False
        
        # If all checks passed, the blockchain is valid
        return True
    
    # Mines a new block with given data and adds to the chain
    def mine_block(self, data):
        # Initialise a flag to check if a valid proof of work has been found
        proof_found = False

        # The proof of work, which will be incremented until a valid number is found
        proof_of_work = 0

        while not proof_found:
            previous_hash = self.get_last_block().get_hash()

            # Initialise the new block
            new_block = Block(timestamp=datetime.datetime.now(), data=data, previous_hash=previous_hash, proof_of_work=proof_of_work)

            # Get the hash of the new block
            new_block_hash = new_block.get_hash()

            if (new_block_hash[:len(self.MINING_DIFFICULTY)] == self.MINING_DIFFICULTY):
                # Valid proof of work has been found
                proof_found = True
                
                # Add the newly-mined block to the blockchain
                self.add_block(new_block)

                # Print the new block
                print("New block")
                print(new_block.__repr__())
            
            else:
                # Increment the proof of work
                proof_of_work += 1
            




    
