from .block import Block

class Blockchain:
    # Manages the chain of blocks and ensures integrity
    difficulty = 3

    def __init__(self):
        self.chain = [self.create_genesis_block]
    
    def create_genesis_block(self):
        # First block in the chain (no previous hash)
        return Block(0, "Genesis Certificate", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def mine_block(self, new_block):
        # Proof of work: Find a hash that meets difficulty
        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


