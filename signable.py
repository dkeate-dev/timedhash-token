'''
A module, signable.py

Classes
-------
Signable(Hashable)
'''

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

from hashable import Hashable, str_hash


class Signable(Hashable):
    '''
    A class, Signable extends Hashable, serves as the base for all Signable objects on the chain

    Attributes
    ----------
    signer : str
        base58 string representing the signer of the Signable object
    signature : str
        string that represents the signature of the Signable object

    Methods
    -------
    generate_unsigned
        generates the unsigned data of the Signable object
    generate_unsigned_hash
        generates the unsigned hash of the Signable object
    validate_signature
        validates the signature data of the Signable object against a RSA PublicKey object
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
        generates the unsigned data of the Signable object
        '''
        unsigned_data = self.generate_metadata()
        unsigned_data.pop("signer")
        unsigned_data.pop("signature")
        return unsigned_data

    def generate_unsigned_hash(self) -> SHA256:
        '''
        generates the unsigned hash of the Signable object
        '''
        return SHA256.new(str(self.generate_unsigned()).encode("utf-8"))

    def validate_signature(self, public_key : RSA.RsaKey) -> int:
        '''
        validates the signature data of the Signable object against a RSA PublicKey object
        '''
        signature = bytes.fromhex(self.signature)
        public_key = RSA.import_key(public_key)
        pkcs1_15.new(public_key).verify(
            str_hash(str(self.generate_unsigned())),
            signature
        )
        return 0
