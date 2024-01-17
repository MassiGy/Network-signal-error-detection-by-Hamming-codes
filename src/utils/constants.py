"""
        @Author Massiles GHERNAOUT
        @Source https://en.wikipedia.org/wiki/Hamming_code

        This contains all the canonical Hamming Codes. Nevertheless, only the
        first one will be used in our program, in the encoding phase.

        Our program is designed to break down the given word to encode into sub
        words of length 4. Thus, the first Hamming code setup is the only one
        required for this demo. The goal is to simplify the error detection
        bits calculation and possibly cache it for the futur incomming words.
        Besides, this helps us make Hamming error detection mechanism more
        reliable since the probability of having multiple errors in a 4 bit
        wide word is smalled then in the context of a 120 (or more) bit wide
        word.
"""
HAMMING_CODES_PER_LENGTH: dict[int, int]= {
    # Total bits count          # Data bits count
    7:                          4,
    15:                         11,
    31:                         26,
    63:                         57,
    127:                        120,
    255:                        247,
    511:                        502
}

HAMMING_7_4_DATA_BITS_COUNT = 4
HAMMING_7_4_ERRDETCT_BITS_COUNT = 3
HAMMING_7_4_WORD_TO_SEND_BITS_COUNT = 7

ENCODING_ERROR_DETECTION_BITS_POSITIONS_7_4 = {
    #Error Detection Bit        # Position of the given Err Detection bit i.e (2**i) for Ci
    "C0":                       1,
    "C1":                       2,
    "C2":                       4,
}



ENCODING_ERROR_DETECTION_BITS_CALC_7_4 = {
    #Error Detection Bit        # Positions of The In-Word Bits to Sum up. (Not Indecies!)
    "C0":                       [1,2,4],    # positions before adding the err detec bits
    "C1":                       [1,3,4],
    "C2":                       [2,3,4],
}





