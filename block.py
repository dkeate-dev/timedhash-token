'''
A module, block.py

Classes
-------
Block(Hashable)
'''

from hashable import Hashable
from transaction import TokenTransaction
from tree import HeadNode


class Block(Hashable):
    '''
    A class, Block extends Hashable, is used to represent a block of information stored to the
    chain

    Attributes
    ----------
    block_id : int
        sequential id for the current Block starting with 0
    previous_block_hash_str : str
        hash of previous_block if there is one, else a string of 64 0s
    transactions : [TokenTransaction]
        list of transactions to be stored in the Block

    Methods
    -------
    generate_metadata
        generates the metadata dict of the Block
    '''

    def __init__(self, previous_block : "Block", transactions : [TokenTransaction]) -> None:
        super().__init__()
        self.transaction_tree = HeadNode(transactions)

        if previous_block:
            self.previous_block_hash_str = previous_block.generate_hash_hex()
            self.block_id = previous_block.block_id + 1
        else:
            self.previous_block_hash_str = "0" * 64
            self.block_id = 0

    def generate_metadata(self) -> dict:
        '''
        generates the metadata dict of the Block
        '''
        metadata = super().generate_metadata()
        metadata["block_id"] = self.block_id
        metadata["previous_block_hash_str"] = self.previous_block_hash_str
        metadata["transactions"] = [
            i.generate_metadata() for i in self.transaction_tree.get_transaction_list()
        ]

        return metadata
