from config import DECODING_ERROR
from utils.constants import HAMMING_CODES_PER_LENGTH
from utils.helpers import isPowerOfTwo, reverse


def decode(binary_code: str) -> None: 
    """
        @Author Massiles GHERNAOUT

        This function will receive a binary code that follows one of the 
        canonical Hamming codes setup i.e 7-4,15-11...

        Thereafter, the function will extract the error detection bits, see
        if the thier values is diffrent then 0, if so, then there is an err
        and we can correct it since we can derrive its position. After that,
        we will extract the data bit and output them to the user.

        Besides, we assume that if the binary sequence contain an error, this
        one will be unique. Since Hamming error tracking is only good when 
        the error count do not exceed 1 per sequence.

    """

    # reverse to get the natural number reading while type = str
    # binary_code = reverse(binary_code)

    binary_code_len = len(binary_code)

    # we will assume that all the binary_code won't exceed the 
    # biggest Hamming standard code saved in our constants
    if binary_code_len not in HAMMING_CODES_PER_LENGTH.keys():
        print("Error on decoding, non supported binary_code length/format. (ABORT)")
        exit(DECODING_ERROR)

    # save the count of data bits
    data_bits_count = HAMMING_CODES_PER_LENGTH[binary_code_len]
    err_detection_bits_count = binary_code_len - data_bits_count


    # calculer les bit d'erreur
    err_detection_bits = [] 

    for i in range(err_detection_bits_count): 
        c_prime_i = 0

        copy = False
        for j in range(len(binary_code)):
            if j % (2**i) == 0:
                copy = not(copy)

            if copy: 
                # print("@i:", i, " ^bit:", binary_code[j])
                c_prime_i ^= int(binary_code[j])

        err_detection_bits.append(c_prime_i)


    # check if there is an error
    err_detection_bits_sum = 0
    for i in range(err_detection_bits_count):
        err_detection_bits_sum += err_detection_bits[i] * 2**i


    # print("err @pos: ", err_detection_bits_sum)

    # print("err bit equal to: ", binary_code[-err_detection_bits_sum])

    binary_code = reverse(binary_code)
    if err_detection_bits_sum != 0: 
        # there is an err at pos: err_detection_bits_sum ,
        # (note: a number in a str is reversed)
        # flip that bit, just xor it with 1
        flipped_err_bit = int(binary_code[err_detection_bits_sum-1]) ^ 1
        # print("flipped_bit: ", flipped_err_bit)

        # print("binary_code[:err_detection_bits_sum-2]: ", binary_code[:err_detection_bits_sum-1])
        # print("binary_code[err_detection_bits_sum:]: ", binary_code[err_detection_bits_sum:])
        binary_code =  binary_code[:err_detection_bits_sum-1]+ str(flipped_err_bit) + binary_code[err_detection_bits_sum:]


    binary_code =  reverse(binary_code)


    print("corrected: ", binary_code)

    # extract the data bits
    data_bits = ""
    for i in range(binary_code_len):
        if isPowerOfTwo(i+1) and i <= err_detection_bits_count:
            continue
        else: 
            data_bits += binary_code[i]

    print("data bits: ", data_bits)








        





