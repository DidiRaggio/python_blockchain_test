import hashlib
from block import Block


class Chain(object):
    """docstring for Chain"""
    def __init__(self, difficulty):
        super(Chain, self).__init__()
        self.difficulty = difficulty
        self.blocks = []  # will be created by the data that comes into the pool.
        self.pool = []  # waiting area for data to be mined into the blockchain, contains incoming data.
        self.create_origin_block()

        # Nodes will be checking the pool to see if there is data in it.
        # if so they will grab that data and use the mining operation on that
        # block. The chain will then test the result and make sure it complies
        # with the difficulty requirement and add it to the blocks.

    # Receives block and tests it.
    def proof_of_work(self, block):
        _hash = hashlib.sha256()
        _hash.update(str(block).encode("utf-8"))
        proof_of_consitency = block.hash.hexdigest() == _hash.hexdigest()
        proof_of_difficulty = int(_hash.hexdigest(), 16) < 2**(256 - self.difficulty)
        proof_of_continuity = block.previous_hash == self.blocks[-1].hash  # This makes a tamperer need to update every block further forward.
        return proof_of_consitency and proof_of_difficulty and proof_of_continuity

    def add_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    # The security of a blockchain is done by linking the blocks together.
    def add_to_pool(self, data):
        self.pool.append(data)

    # Creates empty block to start chain.
    def create_origin_block(self):
        _h = hashlib.sha256()
        _h.update("".encode("utf-8"))
        origin = Block(
            data="Origin",
            previous_hash=_h
        )
        origin.mine(self.difficulty)
        self.blocks.append(origin)

    def mine(self):
        # Test if anything in the poool.
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(
                data=data,
                previous_hash=self.blocks[-1].hash
            )
            block.mine(self.difficulty)
            self.add_to_chain(block)
            print("\n\n=======================")
            print(f"Hash:\t\t {block.hash.hexdigest()}")
            print(f"Previous Hash:\t\t {block.previous_hash.hexdigest()}")
            print(f"Nonce:\t\t {block.nonce}")
            print(f"Data:\t\t {block.data}")
            print("\n\n=======================")