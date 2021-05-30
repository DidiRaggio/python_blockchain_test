import hashlib

_h = hashlib.sha256()  # secure hashing algorithm of 256bits, developed by the NSA.
# soon replaced by sha512

_h.update('a'.encode('utf-8'))

print(_h.hexdigest())  # returns sha256 hash.

# the max size of a hash would be:
print(2**256)

# In our blockchain we can set the dificulty threshhold to:
print(2**(256-10))

# We can check if our hash passes this dificulty threshhold.
print(int(_h.hexdigest(), 16) < 2**(256-10))
print("\n")
# We set i as the counter, the "nonce" for acheiving the dificulty level.
i = 0
# _h2 = _h
_h2 = hashlib.sha256()

_h2.update(str(i).encode("utf-8"))
print(f"does i = {i} meet dificulty threshhold?")
print(int(_h2.hexdigest(), 16) > 2**(256-10))

print("\n")
while int(_h2.hexdigest(), 16) > 2**(256-10):
    i += 1
    _h2.update(str(i).encode("utf-8"))
    print(f"does i = {i} meet dificulty threshhold?")
    print(int(_h2.hexdigest(), 16) < 2**(256-10))
    print(f"hash: {_h2.hexdigest()}")
    print("\n")

# In python hash strings are cumulative, and do not reset therfore
_h3 = hashlib.sha256()
_h3.update(str(i).encode("utf-8"))
print(f"for a new python sha256 object does i = {i} meet the dificulty threshhold??")
print(int(_h3.hexdigest(), 16) < 2**(256-10))
print(f"hash _h3: {_h3.hexdigest()}")
print(f"hash _h2: {_h2.hexdigest()}")
print(f"is it the same ase in _h2? {_h2.hexdigest() == _h3.hexdigest()}")
print("\n")

# Try new while loop.
_h4 = hashlib.sha256()
i = 0
# _h2 = _h
_h4 = hashlib.sha256()

_h4.update(str(i).encode("utf-8"))
print(f"does _h4 i = {i} meet dificulty threshhold?")
print(int(_h4.hexdigest(), 16) > 2**(256-10))
print(f"hash: {_h4.hexdigest()}")
print("\n")
while int(_h4.hexdigest(), 16) > 2**(256-10):
    i += 1
    # We reset _h4
    _h4 = hashlib.sha256()
    _h4.update(str(i).encode("utf-8"))
    print(f"does _h4 i = {i} meet dificulty threshhold?")
    print(int(_h4.hexdigest(), 16) > 2**(256-10))
    print(f"hash: {_h4.hexdigest()}")
    print("\n")
