'''
A module, wallet.py

Classes
-------
Wallet(Hashable)

Functions
---------
validate_signature
'''

# from base64 import b64encode
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

from hashable import Hashable, str_hash_hex, hex_to_base58


class Wallet(Hashable):
    '''
    A class, Wallet extends Hashable

    Attributes
    ----------
    private_key : RsaKey

    Methods
    -------
    generate_metadata
    sign_transaction
    '''

    def __init__(self, private_key=None) -> None:
        super().__init__()
        if not private_key:
            self.private_key = RSA.generate(2048)
        else:
            self.private_key = private_key
        self.private_key_str = self.private_key.public_key().export_key().decode("utf-8")
        self.wallet_address = hex_to_base58(str_hash_hex(self.private_key_str))

    def generate_metadata(self) -> dict:
        '''
        generates the metadata dict of the wallet object
        '''
        metadata = super().generate_metadata()
        metadata["public_key"] = self.private_key.public_key().export_key().decode("utf-8")
        metadata["wallet_address"] = self.wallet_address

        return metadata


    def sign_transaction(self, transaction) -> str:
        '''
        sign a transaction with the private key in the wallet

        TODO: SignError or similar.
        '''
        data_to_sign = transaction.generate_hash()
        return pkcs1_15.new(self.private_key).sign(data_to_sign).hex()

def validate_signature(public_key_str : str, signature_str : str, transaction) -> bool:
    '''
    validates a signature of a transaction using a public key
    '''
    signature = bytes.fromhex(signature_str)
    public_key = RSA.import_key(public_key_str)
    try:
        pkcs1_15.new(public_key).verify(transaction.generate_hash(), signature)
        return True
    except ValueError:
        return False
