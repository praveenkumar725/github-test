# The program must accept the time in 24-hour format. The program must print the time in 12-hour format as the output.


  

def convert12(str): 
    h1 = ord(str[0]) - ord('0') 
    h2 = ord(str[1]) - ord('0') 
    hh = h1 * 10 + h2 
    Meridien="" 
    if (hh < 12): 
        Meridien = "AM" 
    else: 
        Meridien = "PM" 
    hh %= 12 
    if (hh == 0): 
        print("12", end = "") 
        for i in range(2, 8): 
            print(str[i], end = "") 
    else: 
        print(hh,end="") 
        for i in range(2, 8): 
            print(str[i], end = "") 
    print(" " + Meridien) 
if __name__ == '__main__': 
    str =input("enter the time") 
    convert12(str) 


