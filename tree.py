'''
A module, tree.py

Classes
-------
Node

HeadNode

'''

from hashable import Hashable
from transaction import Transaction


class Node(Hashable):
    '''
    A class, Node

    Attributes
    ----------

    Methods
    -------
    '''

    def __init__(self, transaction, left_node = None, right_node = None) -> None:
        super().__init__()
        self.transaction = transaction
        self.left_node = left_node
        self.right_node = right_node

    def generate_metadata(self) -> dict:
        '''
        A method, generate_data
        '''
        return super().generate_metadata()


class HeadNode (Node):
    '''
    A class, HeadNode extends Node
    '''

    def __init__(self, list_of_transactions) -> None:
        list_of_transactions.sort(key=lambda x: x.timestamp)

        super().__init__(None)

        if list_of_transactions:
            midpoint = len(list_of_transactions) // 2
            self.left_node = self.transaction_tree_insert(list_of_transactions[:midpoint])
            self.right_node = self.transaction_tree_insert(list_of_transactions[midpoint+1:])
            self.transaction = list_of_transactions[midpoint]

    def transaction_tree_insert(self, remaining_transactions) -> Node:
        '''
        A method, transaction_tree__insert
        '''
        if not remaining_transactions:
            return None

        midpoint = len(remaining_transactions) // 2

        return Node(
            remaining_transactions[midpoint],
            self.transaction_tree_insert(remaining_transactions[:midpoint]),
            self.transaction_tree_insert(remaining_transactions[midpoint+1:])
        )
    
    def get_transactions(self) -> Transaction:
        '''
        A method, get_transactions
        '''

