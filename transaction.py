'''
A module, transaction.py
'''

from signable import Signable


class Transaction(Signable):
    '''
    A class, Transaction extends Signable

    Attributes
    ----------

    Methods
    -------
    '''

    def __init__(self) -> None:
        super().__init__()

    def generate_metadata(self) -> dict:
        '''
        A method, generate_metadata
        '''
        return super().generate_metadata()
