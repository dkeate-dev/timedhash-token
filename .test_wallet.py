from Crypto.PublicKey import RSA

from signable import Signable
from wallet import Wallet, validate_signature


if __name__ == "__main__":
    my_wallet = Wallet()
    print(my_wallet)

    my_signable = Signable(signer_wallet = my_wallet)
    print(my_signable)

    public_key = my_wallet.generate_metadata()["public_key"]
    signature = my_wallet.sign_signable(my_signable)
    print(signature)
    print(validate_signature(public_key, signature, my_signable))
    print(my_signable.validate_signature(public_key))

    my_signable2 = Signable()
    my_signable2.timestamp = my_signable.timestamp
    my_signable2.signer = my_signable.signer
    my_signable2.signature = my_signable.signature
    print(my_signable2.validate_signature(public_key))

    print(my_signable2)

    w1 = Wallet()

    print(w1.private_key.export_key())
    print(w1)

    with open("secrets/gw_pk.txt", "wb") as file:
        file.write(w1.private_key.export_key())

    with open("secrets/gw.json", "w") as file:
        file.write(str(w1))

    with open("secrets/gw_pk.txt", "rb") as file:
        new_pk = RSA.import_key(file.read())

    print(new_pk.export_key())
