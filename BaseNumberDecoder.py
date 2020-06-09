import base64



print(r"""

______                _   _  ______                   _           
| ___ \              | \ | | |  _  \                 | |          
| |_/ / __ _ ___  ___|  \| | | | | |___  ___ ___   __| | ___ _ __ 
| ___ \/ _` / __|/ _ \ . ` | | | | / _ \/ __/ _ \ / _` |/ _ \ '__|
| |_/ / (_| \__ \  __/ |\  | | |/ /  __/ (_| (_) | (_| |  __/ |   
\____/ \__,_|___/\___\_| \_/ |___/ \___|\___\___/ \__,_|\___|_|

works with base16/32/64""")


base = int
n = int
selection = int

while True:

    while True: 
        try:
            base  = int(raw_input("\nWhat base are you decrypting: "))
        except:
            print("\nEnter an interger")
        else:
            break
    
    if base == 16 or base == 32 or base == 64:
        break
    else:
        print("\nIncorrect Input. Please input 16, 32, or 64 as shown.")

message = "\nHow many times was the base" + str(base) + " encrypted: "

while True:
    try:
        n = int(raw_input(message))
    except:
        print("\nEnter an interger")
    else:
        break


while True:
    try:
        selection = int(raw_input("\nEnter \"1\" for file input: \nEnter \"2\" for manual input:\n "))
    except:
        print("\nEnter an interger")
    else:
        if selection == 1 or selection == 2:
            break
if selection == 1:
    path = raw_input("\nEnter path to file: ")
    decodeThisFile = open(str(path), "r")
    encryption = decodeThisFile.read() 

elif selection == 2:
    encryption = raw_input("\nInput encryption to decode\n")

if base == 16:
    for i in range(n):
        encryption = base64.b16decode(encryption)
if base == 32:
    for i in range(n):
        encryption = base64.b32decode(encryption)
if base == 64:
    for i in range(n):
        encryption = base64.b64decode(encryption)

        
print("\n" + encryption + "\n") 

