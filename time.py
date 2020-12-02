import datetime
import pyttsx3
import wikipedia

friend = pyttsx3.init()
voices = friend.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
friend.setProperty('voice', voices[1].id)
friend.say("Hi sir, I am your personal assistant. How are you?")
friend.runAndWait()


def main():
    while True:
        action = select_action()
        if action == 'time' or 'time' in action:
            time()
        elif action == 'date':
            date()
        elif action == 'fine' or 'fine' in action:
            fine()
        elif action == 'tamim' or 'tamim' in action:
            tamim()
        elif action == 'name' or 'name' in action:
            name()
        elif action == 'exit':
            exit()
            break
        else:
            wiki()


def select_action():
    return input(">> >> ")


def time():

        now = datetime.datetime.now()
        print("Current time : ")
        print(now.strftime("%H:%M:%S"))
        friend = pyttsx3.init()
        friend.say(now.strftime("%H:%M:%S"))
        friend.runAndWait()


def date():

        date = datetime.datetime.now()
        print("Current date:")
        print(date.strftime("%d-%m-%Y"))
        friend = pyttsx3.init()
        friend.say(date.strftime("%d-%m-%Y"))
        friend.runAndWait()


def exit():
    exit_voice = pyttsx3.init()
    exit_voice.say("Bye sir, Have a good day.")
    exit_voice.runAndWait()


def fine():
    friend = pyttsx3.init()
    friend.say("It's great to know that you are fine.")
    friend.runAndWait()


def tamim():
    friend = pyttsx3.init()
    friend.say("Yes,I know her sir   She is Saquib's wife.")
    friend.runAndWait()


def name():
    friend = pyttsx3.init()
    friend.say("My name is asif And I am always with you")
    friend.runAndWait()


def wiki():

    n = select_action()
    result = wikipedia.search(n, results=2)
    print(result)


if __name__ == '__main__':
    main()