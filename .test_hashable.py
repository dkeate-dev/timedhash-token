from hashable import Hashable, file_hash, file_hash_hex, str_hash,\
    str_hash_hex, hex_to_base58, get_time_stamp

if __name__ == "__main__":
    my_hashable = Hashable()

    print(my_hashable.generate_hash().hexdigest())
    print(my_hashable.generate_hash_hex())
    print(my_hashable.generate_metadata())
    print(my_hashable)

    print(file_hash("./test-files/time.pdf").hexdigest())
    print(file_hash_hex("./test-files/time.pdf"))
    print(str_hash("Dustin Keate").hexdigest())
    print(str_hash_hex("Dustin Keate"))

    print(hex_to_base58("123456789abcdef"))
    print(get_time_stamp())
