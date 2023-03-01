from block import Block
from transaction import TokenTransaction, TokenTransactionInput, TokenTransactionOutput
from wallet import Wallet

if __name__ == "__main__":
    my_wallet = Wallet()
    my_transaction = TokenTransaction(
        [TokenTransactionInput((1,0), "abc", 2)],
        [
            TokenTransactionOutput("bcd", 1),
            TokenTransactionOutput("abc", 1)
        ],
        my_wallet
    )

    block_1 = Block(None,[])
    block_2 = Block(block_1,[my_transaction])
    print(block_1.generate_metadata())
    print(block_2)

    print(block_2.generate_hash().hexdigest())
    print(block_2.generate_hash_hex())
