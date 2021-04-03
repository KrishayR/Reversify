import pyttsx3

engine = pyttsx3.init()


def ReverseText(text):
    if not type(text) is str:
        raise TypeError('Only strings are allowed. Please enter a string.')
    text = str(text[::-1])
    print(text)

def ReverseVoice(text):
    global engine
    print('Reverse Audio text:',str(text[::-1]))
    engine.say(str(text[::-1]))
    engine.runAndWait()
    
