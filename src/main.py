from config import *
from utils.decode import decode
from utils.encode import encode



# get user input, the bit sequence
binary_code:str = input("Please insert the binary sequence: ")
# get user wanted action
action:str = input("Please insert the wanted action " + str(SUPPORTED_ACTIONS)+" : ")



if len(binary_code) == 0:
    print("Binary sequence can not be blank. (ABORT)")
    exit(BINARY_CODE_EMPTY)
elif action not in SUPPORTED_ACTIONS: 
    print("Non supported action. (ABORT)")
    exit(NON_SUPPORTED_ACTION)

accumulator = ""
if action == SUPPORTED_ACTIONS[0]:
    encode(binary_code)
elif action == SUPPORTED_ACTIONS[1]:
    decode(binary_code)
    


