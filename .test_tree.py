from time import sleep

from transaction import Transaction
from tree import HeadNode

if __name__ == "__main__":
    t2 = Transaction()
    sleep(.1)
    t1 = Transaction()
    sleep(.1)
    t3 = Transaction()
    sleep(.1)
    t4 = Transaction()

    my_head_node = HeadNode([t1, t2, t3, t4])

    print(my_head_node)

    transaction_list = my_head_node.get_transaction_list()

    for t in transaction_list:
        print(t)
