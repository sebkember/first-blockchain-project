from blockchain import Blockchain
from block import Block

# Create a new blockchain
blockchain = Blockchain()

while True:
    data_input = input("Add data to the blockchain: ")

    print("Mining...")
    blockchain.mine_block(data_input)

    print("Mining complete!")
    print("New state of chain: ")
    print(blockchain.__repr__())
    print(f"Chain valid: {blockchain.is_valid()}")