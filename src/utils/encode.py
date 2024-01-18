from config import ENCODING_ERROR
from utils.constants import *


def encode(binary_code: str) -> None: 
    """
        @Author Massiles GHERNAOUT


        The encode function will take a binary sequence and generate the
        equivalent Hamming binary sequence to send over the wire. Of course,
        this will be done if possible. 

        Edge cases: 

        If the binary code given to the function does not have a canonical
        length according to the diffrent Hamming configuration, then in this
        case, the binary code will be extended with 0's in the beginning so as
        it reaches a standard Hamming sequence length.

    """

    # first get the length of the passed bianry code
    binary_code_len:int = len(binary_code)

    while binary_code_len % HAMMING_7_4_DATA_BITS_COUNT != 0: 
        binary_code = "0" + binary_code
        binary_code_len += 1

    # split the binary code into sub binary words of len 4
    sub_binary_codes = []
    index = 0
    for i in range(binary_code_len): 

        if i > 0 and i % HAMMING_7_4_DATA_BITS_COUNT == 0: 
            index+=1

        if index >= len(sub_binary_codes): 
            # add a sub list for the next sub word 
            sub_binary_codes.append([])



        sub_binary_codes[index].append(binary_code[i])


        

    # for each sub word, fill in the err detection bits
    words_to_transmit = []
    index = 0
    for sword in sub_binary_codes: 
        # sword is a list of bits i.e ['1','0','1','0']

        if index >= len(words_to_transmit):
            # fill the new sub word list with "x"
            words_to_transmit.append(["x" for _ in range(HAMMING_7_4_WORD_TO_SEND_BITS_COUNT)])



        for i in range(HAMMING_7_4_ERRDETCT_BITS_COUNT):
            # position the err detection bits
            words_to_transmit[index][ENCODING_ERROR_DETECTION_BITS_POSITIONS_7_4["C"+str(i)]-1] = int(sword[ENCODING_ERROR_DETECTION_BITS_CALC_7_4["C"+str(i)][0]-1])
            words_to_transmit[index][ENCODING_ERROR_DETECTION_BITS_POSITIONS_7_4["C"+str(i)]-1] ^= int(sword[ENCODING_ERROR_DETECTION_BITS_CALC_7_4["C"+str(i)][1]-1])
            words_to_transmit[index][ENCODING_ERROR_DETECTION_BITS_POSITIONS_7_4["C"+str(i)]-1] ^= int(sword[ENCODING_ERROR_DETECTION_BITS_CALC_7_4["C"+str(i)][2]-1])


        j = 0
        for i in range(HAMMING_7_4_WORD_TO_SEND_BITS_COUNT):
            # position the data bits
            if words_to_transmit[index][i] == "x": 
                words_to_transmit[index][i] = int(sword[j])
                j+=1

        if "x" in words_to_transmit[index]:
            print("Error on encoding. (ABORT)")
            exit(ENCODING_ERROR)


        index+=1


    print(words_to_transmit)

