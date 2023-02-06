from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from transaction import Transaction

my_transaction = Transaction()

print(my_transaction.generate_hash_hex())

print()

private_key = RSA.generate(2048)
public_key = RSA.import_key(private_key.public_key().export_key().decode("utf-8"))

print()

print(private_key.public_key().export_key().decode("utf-8"))

print()

h = SHA256.new(b"1234567890")
print(h.hexdigest())

print()

signature = pkcs1_15.new(private_key).sign(my_transaction.generate_hash())
print(bytes.fromhex(signature.hex()))
print(signature)
print(pkcs1_15.new(public_key).verify(my_transaction.generate_hash(), signature))
