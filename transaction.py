'''
A module, transaction.py
'''

from hashable import Hashable


class Transaction(Hashable):
    '''
    A class, Transaction extends Hashable

    Attributes
    ----------

    Methods
    -------
    '''

    def __init__(self) -> None:
        super().__init__()
        #signer             Wallet?
        #description        str

    def generate_metadata(self) -> dict:
        '''
        A method, generate_metadata
        '''
        return super().generate_metadata()
