'''
A module, main.py
'''
import time

from block import Block
import transaction
import tree
from wallet import Wallet, validate_signature


if __name__ == "__main__":
    block_1 = Block(None)
    block_2 = Block(block_1)
    print(block_1.generate_metadata())
    print(block_2.generate_metadata())

    t1 = transaction.Transaction()
    time.sleep(1)
    t2 = transaction.Transaction()
    time.sleep(2)
    t3 = transaction.Transaction()

    node = tree.HeadNode([t1,t2,t3])
    print(node.transaction)
    print(node.left_node.transaction)
    print(node.right_node.transaction)

    my_wallet = Wallet()
    public_key = my_wallet.generate_metadata()["public_key"]
    signature = my_wallet.sign_transaction(node.transaction)
    print(signature)

    print(validate_signature(public_key, signature, node.transaction))
