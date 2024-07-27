import speech_recognition as sr
import pyttsx3
from gtts import gTTS

# Initialize the recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice {i}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    # print(f" - Languages: {voice.languages}")
    # print(f" - Gender: {voice.gender}")
    # print(f" - Age: {voice.age}")

def maleVoice():
    # Set properties
    engine.setProperty('voice', voices[0].id)  # Choose voice by index
    engine.setProperty('rate', 150)  # Speed of speech (default is usually 200)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

def femaleVoice():
    # Set properties
    engine.setProperty('voice', voices[1].id)  # Choose voice by index
    engine.setProperty('rate', 150)  # Speed of speech (default is usually 200)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Function to convert text to speech using pyttsx3
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

def convertor():
    print("Whose voice you want to listen ?")
    number = int(input("Enter no.: 1 for Male and 2 for Female: "))
    if number == 1:
        maleVoice()
    elif number == 2:
        femaleVoice()

    # Loop infinitely for user to speak
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                SpeakText("Listening... Please give me the command.")

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say: ", MyText)
                SpeakText(MyText)

                if "exit" in MyText:
                    SpeakText("Exiting the Program...")
                    print("Exiting the Program...")
                    break

        except sr.RequestError as e:
            SpeakText("Could not request results; {0}".format(e))
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            SpeakText("Sorry, I did not understand that.")
            print("Sorry, I did not understand that.")

        except KeyboardInterrupt:
            SpeakText("Exiting the Program...")
            print("\nExiting program.")
            break

convertor()
