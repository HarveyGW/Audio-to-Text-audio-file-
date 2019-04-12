import speech_recognition as sr 
import colorama
from colorama import Fore as f
  
AUDIO_FILE = (input("Enter the Files Name: ")+".wav") 
  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 

  audio = r.record(source)  #Reads the audio file
  
try: 
	print(f.LIGHTGREEN_EX + "Success")
	print(f.LIGHTYELLOW_EX + "The audio file contains: " + f.LIGHTBLUE_EX + r.recognize_google(audio)) 
  
except sr.UnknownValueError: 
  print(f.LIGHTRED_EX + "Google Speech Recognition could not understand the audio") 
  
except sr.RequestError as e: 
  print(f.LIGHTRED_EX + "Could not request results from Google Speech Recognition service; {0}".format(e)) 
