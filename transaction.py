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
    A class, Transaction extends Signable

    Attributes
    ----------

    Methods
    -------
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
    A class, TransactionOutput extends Hashable

    Attributes
    ----------

    Methods
    -------
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
    A class, TransactionInput extends Hashable

    Attributes
    ----------

    Methods
    -------
    '''

    def __init__(self, reference_output : (int,int), wallet_address, amount) -> None:
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
