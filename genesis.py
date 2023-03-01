'''
A module, genesis.py

Classes
-------
Genesis(Block)
'''

from block import Block
from transaction import TokenTransaction, TokenTransactionOutput


class Genesis(Block):
    '''
    A class, Genesis

    Attributes
    ----------

    Methods
    -------
    '''

    def __init__(self):
        genesis_transactions = [TokenTransaction([],
            [TokenTransactionOutput("4n8fEJNjM8XXitqQpmYhYKpgHLLjKMYmXUHFj1GKSHPJ", 333),
            TokenTransactionOutput("5REV5gGgc1rTUPEyQaBgLm4Sn8LCuVHcgSuybhYbYmq4", 333),
            TokenTransactionOutput("E31ZBLQRKNenRLLY5ufgHfpQJ1sPNPt7sjjefGNSvD94", 333)])]
        
        for i in range(len(genesis_transactions[0].transaction_outputs)):
            genesis_transactions[0].transaction_outputs[i].timestamp = "2023-01-01 00:00:00.000000"

        super().__init__(None, genesis_transactions)
