from transaction import TokenTransaction, TokenTransactionInput, TokenTransactionOutput
from wallet import Wallet


def main():
    my_wallet = Wallet()
    my_transaction = TokenTransaction(
        [TokenTransactionInput(1, "abc", 2)],
        [
            TokenTransactionOutput("bcd", 1),
            TokenTransactionOutput("abc", 1)
        ],
        my_wallet
    )

    print(my_transaction.generate_unsigned())
    print(my_transaction)


if __name__ == "__main__":
    main()
