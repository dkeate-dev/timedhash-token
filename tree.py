'''
A module, tree.py

Classes
-------
Node(Hashable)
HeadNode(Node)
'''

from hashable import Hashable


class Node(Hashable):
    '''
    A class, Node extends Hashable, contains a single transaction on a single Node in a tree

    Attributes
    ----------
    transaction : Transaction
        the Transaction being stored on this Node
    left_node : Node
        Node downstream and to the left on the tree
    right_node : Node
        Node downstream and to the right on the tree

    Methods
    -------
    append_transactions
        extracts the transaction from the Node and appends it to the passed list
    '''

    def __init__(self, transaction, left_node = None, right_node = None) -> None:
        super().__init__()
        self.transaction = transaction
        self.left_node = left_node
        self.right_node = right_node

    def generate_metadata(self) -> dict:
        metadata = super().generate_metadata()
        metadata["transaction_hash"] = self.transaction.generate_hash_hex()
        if self.left_node:
            metadata["left_node_hash"] = self.left_node.generate_hash_hex()
        if self.right_node:
            metadata["right_node_hash"] = self.right_node.generate_hash_hex()

        return metadata

    def append_transactions(self, result_list) -> None:
        '''
        extracts the transaction from the Node and appends it to the passed list
        '''
        if self.left_node:
            self.left_node.append_transactions(result_list)

        result_list.append(self.transaction)

        if self.right_node:
            self.right_node.append_transactions(result_list)


class HeadNode(Node):
    '''
    A class, HeadNode extends Node, is the top middle Node in the transaction tree

    Methods
    -------
    transaction_tree_insert
        adds the transaction list to the HeadNode and cascades it down the tree
    get_transaction_list
        extracts the transactions from the HeadNode as a list
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
        adds the transaction list to the HeadNode and cascades it down the tree
        '''
        if not remaining_transactions:
            return None

        midpoint = len(remaining_transactions) // 2

        return Node(
            remaining_transactions[midpoint],
            self.transaction_tree_insert(remaining_transactions[:midpoint]),
            self.transaction_tree_insert(remaining_transactions[midpoint+1:])
        )

    def get_transaction_list(self):
        '''
        extracts the transactions from the HeadNode as a list
        '''
        result = []

        if self.left_node:
            self.left_node.append_transactions(result)
        if self.transaction:
            result.append(self.transaction)
        if self.right_node:
            self.right_node.append_transactions(result)

        return result
