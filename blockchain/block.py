import hashlib
import time
import json

class Block:
    # Represents a single block in the blockchain
    def __init__(self, index, certificate_hash, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.certificate_hash = certificate_hash
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Generates a SHA-256 has from block data
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "certificate_hash": self.certificate_hash,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        return
    hashlib.sha256(block_string).hexdigest()
