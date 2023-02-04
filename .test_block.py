from block import Block

if __name__ == "__main__":
    block_1 = Block(None)
    block_2 = Block(block_1)
    print(block_1.generate_metadata())
    print(block_2.generate_metadata())

    print(block_2.generate_hash().hexdigest())
    print(block_2.generate_hash_hex())
    print(block_2)
