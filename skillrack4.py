# An alphabet CH from 'A' to 'V' is passed as the input to the program. The program must print five alphabets from CH as the output.
#  Note: The characters can be represented as integers using ASCII values.

ch=input()
ch=ord(ch)
for i in  range (5):
    print(chr(i),end="")
    ch+=1
