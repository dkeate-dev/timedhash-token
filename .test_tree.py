from time import sleep

from transaction import TokenTransaction
from tree import HeadNode
from wallet import Wallet

if __name__ == "__main__":
    my_wallet = Wallet()
    t2 = TokenTransaction([],[], signer_wallet = my_wallet)
    sleep(.1)
    t1 = TokenTransaction([],[], signer_wallet = my_wallet)
    sleep(.1)
    t3 = TokenTransaction([],[], signer_wallet = my_wallet)
    sleep(.1)
    t4 = TokenTransaction([],[], signer_wallet = my_wallet)

    my_head_node = HeadNode([t1, t2, t3, t4])

    print(my_head_node)

    transaction_list = my_head_node.get_transaction_list()

    for t in transaction_list:
        print(t)
