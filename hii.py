
import pyttsx3
question=pyttsx3.init()
numbersare=pyttsx3.init()
out=pyttsx3.init()
output=pyttsx3.init()
numbers=pyttsx3.init()
firstline=pyttsx3.init()
loop=pyttsx3.init()
oddd=pyttsx3.init()
variable=pyttsx3.init()
question.say("Five integers are passed as the input to the program. The program must print the count of odd integers as the output")
firstline.say("enter the numbers in mylist")
question.runAndWait()
firstline.runAndWait()
mylist=list(map(int,input().strip().split()))
numbers.say(mylist)
numbersare.say("these are numbers in the list")
numbersare.runAndWait()
numbers.runAndWait()
variable.say("initially odd count equal to zero")
variable.runAndWait
oddcount=0
loop.say("the loop start from here")
loop.runAndWait()
for i in mylist:
    if i%2!=0:
        oddcount+=1
oddd.say("printing the odd count")
loop.runAndWait()
print("the count",oddcount)
out.say("the oddcount in the list is ")
output.say(oddcount)
output.runAndWait()
out.runAndWait()

   





