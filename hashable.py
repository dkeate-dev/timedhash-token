'''
A module, hashable.py

Classes
-------
Hashable


Functions
---------
file_hash
file_hash_hex
string_hash
string_hash_hex
hex_to_base58
get_time_stamp
'''

from datetime import datetime

from Crypto.Hash import SHA256
import base58


class Hashable:
    '''
    A class, Hashable

    Attributes
    ----------
    version
        the specification version the Hashable object was created under
    timestamp
        time when the Hashable object was created (according to who?)


    Methods
    -------
    generate_hash
        generates a SHA256 Crypto.Hash object of the block based on the
        metadata
    generate_hash_hex
        generates the sha256 hash of the block based on the metadata
    generate_metadata
        generates the metadata dict of the block
    '''

    def __init__(self):
        self.version = 1
        self.timestamp = get_time_stamp()

    def __str__(self) -> str:
        return str(self.generate_metadata())

    def generate_hash(self) -> SHA256:
        '''
        generates a SHA256 Crypto.Hash object of the Hashable object using the
        metadata of the object
        '''
        return SHA256.new(str(self).encode("utf-8"))

    def generate_hash_hex(self) -> str:
        '''
        generates the sha256 hash string of the Hashable object using the
        metadata of the object
        '''
        return str_hash_hex(str(self))

    def generate_metadata(self) -> dict:
        '''
        generates the metadata dict of the block
        '''
        return {
            "version": self.version,
            "timestamp": self.timestamp,
        }


def file_hash (filename : str) -> SHA256:
    '''
    returns the SHA256 Crypto.Hash object of the file passed
    '''
    with open(filename, "rb") as file:
        filename_hash = SHA256.new(file.read())

    return filename_hash


def file_hash_hex (filename : str) -> str:
    '''
    returns the sha256 hash str of the file passed
    '''
    return file_hash(filename).hexdigest()


def str_hash (data_str : str) -> SHA256:
    '''
    returns the SHA256 Crypto.Hash object of the str passed
    '''
    return SHA256.new(data_str.encode("utf-8"))


def str_hash_hex (data_str : str) -> str:
    '''
    returns the sha256 hash str of the str passed
    '''
    return str_hash(data_str).hexdigest()


def hex_to_base58 (hex_str : str) -> str:
    '''
    converts a hex_str to base58
    '''
    return base58.b58encode_int(int(hex_str,16)).decode("utf-8")


def get_time_stamp() -> str:
    '''
    returns a simple datetime time stamp for the current UTC system time

    TODO: Call ntplib and set an offset. Make it better. Maybe it's own class
    '''
    return str(datetime.utcnow())
