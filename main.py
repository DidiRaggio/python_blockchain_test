# from block import Block

# # Create the blockchain that functions like a LinkedList.
# class Node():
#     def __init__(self):
#         self.data = 5
#         self._next = None
#         # In a linked list each node is linked to each other by the _next attribute, so they are nested one within the other.


# # In a blockchain, we embed one block within the other using the hash. The hash garantees the chain has not been manipulated.

# block = Block("Hello World!")
# block.mine(20)
# print(f"Block's hash: {block.hash.hexdigest()}\nBlock's nonce: {block.nonce}\nBlock's data: {block.data}\n\n")

# block = Block("Hello WorlD!")
# block.mine(20)
# print(f"Block's hash: {block.hash.hexdigest()}\nBlock's nonce: {block.nonce}\nBlock's data: {block.data}\n\n")

from chain import Chain

chain = Chain(difficulty=20)

# i = 0

# while(True):
#     data = input("Add something to the chain: ")
#     chain.add_to_pool(data)
#     chain.mine()
#     if i % 5 == 0:
#         print(chain.blocks[i])
#     i += 1

for i in range(5):
    chain.add_to_pool(f" Block #{i} ")
    chain.mine()
