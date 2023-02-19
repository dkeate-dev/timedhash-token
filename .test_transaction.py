from transaction import Transaction, TransactionInput, TransactionOutput
from wallet import Wallet


def main():
    my_wallet = Wallet()
    my_transaction = Transaction(
        [TransactionInput(1, "abc", 2)],
        [
            TransactionOutput("bcd", 1),
            TransactionOutput("abc", 1)
        ],
        my_wallet
    )

    print(my_transaction.generate_unsigned())
    print(my_transaction)


if __name__ == "__main__":
    main()
