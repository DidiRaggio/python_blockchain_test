# Cryptographic hash
import hashlib  # One way cypher, scrambles data (seemingly randomly).


class Block(object):
    """docstring for Block"""
    def __init__(self, data, previous_hash):
        super(Block, self).__init__()
        self.hash = hashlib.sha256()
        self.nonce = 0
        self.data = data
        # Security in a blockchain is acheived by linking blocks
        self.previous_hash = previous_hash

    # The __str__ is run whenever you are passing the class to a parameter that is treated like a string.
    # for example "print(instance_of_block)".
    def __str__(self):
        # This is a work around for using python. By passing in the previous_hash this affects the hash of the current block, therefor ensuring that the chain has not been tampered with.
        return f"{self.previous_hash.hexdigest()}{self.data}{self.nonce}"

    # We don't know the difficulty of the chain we need to mine.
    def mine(self, difficulty):
        encoded_string_representation = str(self).encode("utf-8")  # passing the instance of Block, applies the __str__ funciton.
        self.hash.update(encoded_string_representation)

        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty):
            # we increment the nonce.
            self.nonce += 1
            # reset hash, because in python hashing is a cumulative process.
            self.hash = hashlib.sha256()
            # encode string representation fo block.
            encoded_string_representation = str(self).encode("utf-8")
            # update hash value.
            self.hash.update(encoded_string_representation)
