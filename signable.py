'''
A module, signable.py
'''

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

from hashable import Hashable, str_hash


class Signable(Hashable):
    '''
    A class, Signable

    Attributes
    ----------

    Methods
    -------
    '''
    def __init__(
        self,
        signer_wallet : 'Wallet' = None,
        signer : str = None,
        signature : str = None,
        public_key : str = None
    ) -> None:
        super().__init__()

        self.signer = None
        self.signature = None

        if signer_wallet:
            self.signer = signer_wallet.wallet_address
            self.signature = signer_wallet.sign_signable(self)
        elif signer and signature:
            self.signer = signer
            self.signature = signature
            self.validate_signature(public_key)

    def generate_metadata(self) -> dict:
        metadata = super().generate_metadata()
        metadata["signer"] = self.signer
        metadata["signature"] = self.signature
        return metadata

    def generate_unsigned(self) -> dict:
        '''
        A method, generate_unsigned_data
        '''
        unsigned_data = self.generate_metadata()
        unsigned_data.pop("signer")
        unsigned_data.pop("signature")
        return unsigned_data

    def generate_unsigned_hash(self) -> SHA256:
        '''
        A method, generate_unsigned_hash
        '''
        return SHA256.new(str(self.generate_unsigned()).encode("utf-8"))

    def validate_signature(self, public_key : RSA.RsaKey) -> int:
        '''
        A method, validate_signature
        '''
        signature = bytes.fromhex(self.signature)
        public_key = RSA.import_key(public_key)
        pkcs1_15.new(public_key).verify(
            str_hash(str(self.generate_unsigned())),
            signature
        )
        return 0
