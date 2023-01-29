'''
A module, block.py

Classes
-------
Block(Hashable)

'''

from hashable import Hashable


class Block(Hashable):
    '''
    A class, block, is used to represent a block of transactions stored to the
    chain

    Attributes
    ----------
    version : int
        an integer that represents the version the block was created under
    block_id : int
        sequential id for the current block.starting with 0
    timestamp : str
        current date and time in format yyyy-mm-dd hh:mm:ss.ssssss
    previous_block_hash_str : str
        hash of previous_block if there is one, else a string of 64 0s
    previous_block : Block
        the block that immediately precedes this block on the chain

    Methods
    -------
    generate_metadata
        generates the metadata dict of the block
    '''

    def __init__(self, previous_block) -> None:
        super().__init__()
        self.previous_block = previous_block
        #transactions_list      [Transactions]

        #transaction_tree_head  TransactionTreeNode and create_tree_from_list

        #if this is the first block, set the previous_block_hash to 0
        if self.previous_block:
            self.previous_block_hash_str = previous_block.generate_hash_hex()
            self.block_id = previous_block.block_id + 1
        else:
            self.previous_block_hash_str = "0" * 64
            self.block_id = 0

    def generate_metadata(self) -> dict:
        '''
        A method, generate_metadata
        '''
        metadata = super().generate_metadata()
        metadata["block_id"] = self.block_id
        metadata["previous_block_hash_str"] = self.previous_block_hash_str

        return metadata
