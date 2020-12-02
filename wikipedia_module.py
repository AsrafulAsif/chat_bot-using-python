# importing the module 
import wikipedia  
import pyttsx3
n=input("Enter your text:")
# finding result for the search 
# sentences = 2 refers to numbers of line 
result = wikipedia.summary(n, sentences = 2)  
  
# printing the result 
print(result)  
friend=pyttsx3.init()
friend.say(result)
friend.runAndWait()