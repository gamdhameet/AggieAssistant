import win32com.client as sp
import speech_recognition as sr
import webbrowser
from formation import AppBuilder
speaker = sp.Dispatch("SAPI.spVoice")

choice = -1
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak......")
        r.pause_threshold = 1
        print("Listening.......")
        audio = r.listen(source)
        print("Recognizing the Input.....")
        queryJunk = r.recognize_google(audio, language="en-us")
        return queryJunk


def openWebsite(st):
    queryLocal = st
    url = f"www.{queryLocal}.com"
    speaker.Speak(f"Opening {queryLocal}")
    webbrowser.open_new(url)
    return 0


def getAnswer(st):
    queryLocal = st
    url = f"https://www.google.com/search?q={queryLocal}"
    speaker.Speak(f"Searching in Google about your query {queryLocal}")
    webbrowser.open_new(url)
    return 0


def repeatInput(st):
    queryLocal = st
    speaker.Speak(queryLocal)
    return 0
def choices():
    global choice
    # print("Commands to execute\n1:Open Website\n2:Get Answer for your question\n3:Get Computer "
    #       "audio of what you speak\n0:To Quit Program")
    # choice = int(input("Enter 1 , 2 , 3 , 0 : "))
    if choice == 1:
        query = takeCommand()
        a = openWebsite(query)
    if choice == 2:
        query = takeCommand()
        a = getAnswer(query)
    if choice == 3:
        query = takeCommand()
        a = repeatInput(query)
    else:
        print("Please Enter valid number")
def button_6():
    global choice
    choice = 1
    print(choice)
    choices()
def button_2():
    global choice
    choice = 2
    choices()
def button_3():
    global choice
    choice = 3
    choices()

app = AppBuilder(path="G:\AggieAsst\Layout.xml")

app.connect_callbacks(globals())

# app.button_6(command=makeSomething)
# app.button_2(command=makeSomething2)
# app.button_3(command=makeSomething3)
choices()
app.mainloop()
