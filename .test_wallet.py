from hashable import Hashable
from wallet import Wallet, validate_signature

if __name__ == "__main__":
    my_hashable = Hashable()
    print(my_hashable)

    my_wallet = Wallet()
    print(my_wallet)

    public_key = my_wallet.generate_metadata()["public_key"]
    signature = my_wallet.sign_transaction(my_hashable)
    print(signature)
    print(validate_signature(public_key, signature, my_hashable))
