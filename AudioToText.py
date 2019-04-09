import speech_recognition as sr 
  
AUDIO_FILE = (input("Enter the Files Name: ")+".wav") 
  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 

  audio = r.record(source)  #Reads the audio file
  
try: 
  print("The audio file contains: " + r.recognize_google(audio)) 
  
except sr.UnknownValueError: 
  print("Google Speech Recognition could not understand the audio") 
  
except sr.RequestError as e: 
  print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
