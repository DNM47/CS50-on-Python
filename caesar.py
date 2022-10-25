import sys                              # To be able to use command line argumtens

if len(sys.argv) != 2:                  # Check if there are less or more than 2 arguments
    print('Usage: ./caesar key\n')
    exit()
else:
    num = sys.argv[1]                   # Converting the 2nd argument into a int

    while True:                         # if there is negative number, string or empty string end code
        try:
            if int(num) < 0:            
                exit()  
            elif int(num) == ' ':
                exit()           
        except:
            print("Usage: ./caesar key\n") 
            exit()
        break

num = int(num)
plaintext = input('plaintext: ')
c_text = ''

for l in plaintext:                                 # Enchiper the plaintext
    new_l = int(ord(l))                             # Converting the letters into ASCII

    if new_l in range(65, 91):                      # Check the uppercase letters    
        char = (((new_l - 65) + num) % 26) + 65
        new_char = chr(char)                        # Converting the ASCII into letter
        c_text += new_char                          # Adding the letter into a empty string

    elif new_l in range(97, 123):                   # Check lowercase letters
        char = (((new_l - 97) + num) % 26) + 97
        new_char = chr(char)
        c_text += new_char
    
    else:
        new_char = chr(new_l)                       # Check all other symbols
        c_text += new_char

print(f'ciphertext: {c_text}')
