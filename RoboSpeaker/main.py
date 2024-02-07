import pyttsx3
if __name__ == '__main__':
        print("--RoboSpeaker--\n")
        x = input("Enter text to pronounce:")
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(x)
        engine.runAndWait()