'''
A module, transaction.py

Classes
-------
Transaction(Signable)
TransactionOutput(Hashable)
TransactionInput(Hashable)
'''

from hashable import Hashable
from signable import Signable
from wallet import Wallet


class TokenTransaction(Signable):
    '''
    A class, TokenTransaction extends Signable, holds a set of transaction inputs and outputs

    Attributes
    ----------
    transaction_inputs : [TransactionInput]
        contains the list of TransactionInputs for the TokenTransaction
    transaction_outputs : [TransactionOutput]
        contains the list of TransactionOutputs for the TokenTransaction

    Methods
    -------
    None
    '''

    def __init__(
        self,
        transaction_inputs : ["TransactionInput"],
        transaction_outputs : ["TransactionOutput"],
        signer_wallet : Wallet = None,
        signer : str = None,
        signature : str = None,
        public_key : str = None
    ) -> None:
        self.transaction_inputs = transaction_inputs
        self.transaction_outputs = transaction_outputs
        super().__init__(signer_wallet, signer, signature, public_key)

    def generate_metadata(self) -> dict:
        metadata = super().generate_metadata()
        metadata["transaction_inputs"] = [i.generate_metadata() for i in self.transaction_inputs]
        metadata["transaction_outputs"] = [i.generate_metadata() for i in self.transaction_outputs]
        return metadata


class TokenTransactionOutput(Hashable):
    '''
    A class, TransactionOutput extends Hashable, represents an output from a TokenTransaction

    Attributes
    ----------
    wallet_address : str
        destination wallet address for the token amount
    amount : int
        token amount ouptput to destination wallet address

    Methods
    -------
    None
    '''

    def __init__(self, wallet_address : str, amount : int) -> None:
        super().__init__()
        self.wallet_address = wallet_address
        self.amount = amount

    def generate_metadata(self) -> dict:
        metadata = super().generate_metadata()
        metadata["wallet_address"] = self.wallet_address
        metadata["amount"] = self.amount
        return metadata


class TokenTransactionInput(Hashable):
    '''
    A class, TransactionInput extends Hashable, represents an input into a TokenTransaction

    Attributes
    ----------
    reference_output : (int,int)
        the reference transaction (block_id, transaction output index) for the current
        TokenTransactionInput
    wallet_address : str
        origination wallet for the token amount
    amount : int
        token amount input from the origination wallet address

    Methods
    -------
    None
    '''

    def __init__(self, reference_output : (int,int), wallet_address : str, amount : int) -> None:
        super().__init__()
        self.reference_output = reference_output
        self.wallet_address = wallet_address
        self.amount = amount

    def generate_metadata(self) -> dict:
        metadata = super().generate_metadata()
        metadata["reference_output"] = self.reference_output
        metadata["wallet_address"] = self.wallet_address
        metadata["amount"] = self.amount
        return metadata
