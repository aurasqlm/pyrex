import random

print("""
      ██████╗ ██╗   ██╗██████╗ ███████╗██╗  ██╗         █████╗ ██╗
      ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝╚██╗██╔╝        ██╔══██╗██║
      ██████╔╝ ╚████╔╝ ██████╔╝█████╗   ╚███╔╝         ███████║██║
      ██╔═══╝   ╚██╔╝  ██╔══██╗██╔══╝   ██╔██╗         ██╔══██║██║
      ██║        ██║   ██║  ██║███████╗██╔╝ ██╗        ██║  ██║██║
      ╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝        ╚═╝  ╚═╝╚═╝
""")

users = ["usr1","usr2","usr3","usr4","usr5","usr6","usr7","usr8","usr9","usr10",
         "usr11","usr12","usr13","usr14","usr15","usr16","usr17","usr18","usr19","usr20",
         "usr21","usr22","usr23","usr24","usr25","usr26","usr27","usr28","usr29","usr30",
         "usr31","usr32","usr33","usr34","usr35","usr36","usr37","usr38","usr39","usr40",
         "usr41","usr42","usr43","usr44","usr45","usr46","usr47","usr48","usr49","usr50"]

usern = random.choice(users)

def chatbot():
    know_name = 0
    name = input("What's your name😁? ").strip()

    if name:
        know_name = 1
        print(f"Pyrex: What's going on {name}?")
    else:
        name = usern
        print(f"Pyrex: What's going on {name}?")

    while True:
        ask = input(f"{name}: ").lower()

        if "hi" in ask or "hello" in ask or "hey" in ask or "hii" in ask or "hlw" in ask:
            print("Pyrex: Hello!")

        elif "how are you" in ask or "how r u" in ask or "you ok" in ask or "are you fine" in ask or "how you doing" in ask:
            print("Pyrex: I'm fine.")

        elif "your name" in ask or "who are you" in ask or "ai name" in ask or "what is your name" in ask or "tell your name" in ask:
            print("Pyrex: My name is Pyrex.")
        elif ask in ["what?","what","wht","wht?"]:
            print("Nothing,brah🤦‍♂️")
        elif "my name" in ask or "do you know my name" in ask or "who am i" in ask or "tell my name" in ask or "remember my name" in ask:
            if know_name:
                print(f"Pyrex: Your name is {name}.")
            else:
                print(f"Pyrex: Default name is {name}.")

        elif "help" in ask or "help me" in ask or "need help" in ask or "assist me" in ask or "support me" in ask:
            print("Pyrex: Tell me your problem.")

        elif "thank" in ask or "thanks" in ask or "thank you" in ask or "thx" in ask or "thanks a lot" in ask:
            print("Pyrex: You're welcome.")

        elif "bye" in ask or "exit" in ask or "quit" in ask or "goodbye" in ask or "see you" in ask:
            print("Pyrex: Goodbye!")
            break

        elif "sing" in ask or "song" in ask or "music" in ask or "play song" in ask or "sing a song" in ask:
            print("Pyrex: 🎵 La la la~")

        elif "joke" in ask or "funny" in ask or "make me laugh" in ask or "tell joke" in ask or "joke please" in ask:
            print("Pyrex: Why did Python sleep? Too many bugs.")

        elif "sad" in ask or "unhappy" in ask or "depressed" in ask or "feeling low" in ask or "down" in ask:
            print("Pyrex: Stay strong.")

        elif "happy" in ask or "excited" in ask or "feeling good" in ask or "great mood" in ask or "joyful" in ask:
            print("Pyrex: Nice to hear that!")

        elif "bored" in ask or "nothing to do" in ask or "free time" in ask or "boring" in ask or "idle" in ask:
            print("Pyrex: Want something fun?")

        elif "tired" in ask or "sleepy" in ask or "exhausted" in ask or "need rest" in ask or "fatigue" in ask:
            print("Pyrex: Take rest.")

        elif "motivate" in ask or "motivation" in ask or "inspire" in ask or "encourage" in ask or "push me" in ask:
            print("Pyrex: Don't give up.")

        elif "fail" in ask or "failure" in ask or "lost exam" in ask or "bad result" in ask or "didn't pass" in ask:
            print("Pyrex: Failure teaches.")

        elif "success" in ask or "achieve" in ask or "goal reached" in ask or "win" in ask or "successful" in ask:
            print("Pyrex: Hard work wins.")

        elif "life" in ask or "life problem" in ask or "life hard" in ask or "life pain" in ask or "life struggle" in ask:
            print("Pyrex: Be patient.")

        elif "future" in ask or "career" in ask or "future plan" in ask or "my future" in ask or "future worry" in ask:
            print("Pyrex: Focus today.")

        elif "goal" in ask or "aim" in ask or "target" in ask or "life goal" in ask or "set goal" in ask:
            print("Pyrex: Set clear goals.")

        elif "discipline" in ask or "routine" in ask or "habit" in ask or "self control" in ask or "discipline tips" in ask:
            print("Pyrex: Discipline matters.")

        elif "computer" in ask or "pc" in ask or "laptop" in ask or "desktop" in ask or "system" in ask:
            print("Pyrex: Computers are useful.")

        elif "windows" in ask or "mini pc" in ask or "windows pc" in ask or "microsoft" in ask or "win system" in ask:
            print("Pyrex: Windows system detected.")

        elif "linux" in ask or "ubuntu" in ask or "mint" in ask or "debian" in ask or "linux os" in ask:
            print("Pyrex: Linux is powerful.")

        elif "android" in ask or "android phone" in ask or "apk" in ask or "google phone" in ask or "android os" in ask:
            print("Pyrex: Android is flexible.")

        elif "virus" in ask or "malware" in ask or "trojan" in ask or "infected" in ask or "pc virus" in ask:
            print("Pyrex: Use antivirus.")

        elif "slow pc" in ask or "pc slow" in ask or "computer slow" in ask or "lag pc" in ask or "pc lag" in ask:
            print("Pyrex: Restart helps.")

        elif "internet" in ask or "wifi" in ask or "network" in ask or "slow net" in ask or "net issue" in ask:
            print("Pyrex: Check connection.")

        elif "battery" in ask or "battery low" in ask or "battery drain" in ask or "low battery" in ask or "charging" in ask:
            print("Pyrex: Reduce background apps.")

        elif "study" in ask or "exam" in ask or "homework" in ask or "revision" in ask or "reading" in ask:
            print("Pyrex: Study daily.")

        elif "english" in ask or "learn english" in ask or "english help" in ask or "speak english" in ask or "grammar" in ask:
            print("Pyrex: Practice English.")

        elif "confidence" in ask or "low confidence" in ask or "self belief" in ask or "be confident" in ask or "confidence tips" in ask:
            print("Pyrex: Believe in yourself.")

        elif "respect" in ask or "respect others" in ask or "be respectful" in ask or "manners" in ask or "respect life" in ask:
            print("Pyrex: Respect matters.")

        elif "time" in ask or "current time" in ask or "time now" in ask or "clock" in ask or "tell time" in ask:
            print("Pyrex: Check system clock.")

        elif "date" in ask or "today date" in ask or "current date" in ask or "calendar" in ask or "what date" in ask:
            print("Pyrex: Check today's date.")

        elif "game" in ask or "play" in ask or "play game" in ask or "gaming" in ask or "game time" in ask:
            print("Pyrex: We can play games.")

        elif "fact" in ask or "fun fact" in ask or "random fact" in ask or "interesting fact" in ask or "tell fact" in ask:
            print("Pyrex: Honey never spoils.")

        elif "sleep" in ask or "sleeping" in ask or "do you sleep" in ask or "sleep ai" in ask or "rest ai" in ask:
            print("Pyrex: I don't sleep.")

        elif "eat" in ask or "food" in ask or "do you eat" in ask or "hungry ai" in ask or "eat ai" in ask:
            print("Pyrex: I don't eat.")

        elif "friend" in ask or "friends" in ask or "like me" in ask or "we friends" in ask or "friendship" in ask:
            print("Pyrex: I'm here with you.")
        elif "going on?" in ask or "how are you" in ask or "going on" in ask or "h r u" in ask:
            print("Pyrex: I am well , wbu")      
        elif "WBU" in ask or "wbu" in ask or "what wbu mean" in ask or "what wbu" in ask or "mean wbu" in ask:
            print("WBU is a freindly text that means What about you?")
        elif "stop" in ask or "end" in ask or "close" in ask or "finish" in ask or "shutdown" in ask:
            print("Pyrex: Chat ended.")
            break

        else:
            print("Pyrex: Sorry, that question is not available in my database.")

chatbot()
