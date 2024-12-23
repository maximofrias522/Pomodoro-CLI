import argparse
import time
import os
import signal
import sys
from playsound import playsound
import pyfiglet
import random

motivational_quotes = [
    "Success is the sum of small efforts, repeated day in and day out.",
    "The future depends on what you do today.",
    "Believe you can and you're halfway there.",
    "Don't watch the clock; do what it does. Keep going.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream big. Work hard. Stay focused.",
    "Success doesn't come from what you do occasionally, it comes from what you do consistently.",
    "The key to success is to focus on goals, not obstacles.",
    "Strive for progress, not perfection.",
    "You don’t have to be great to start, but you have to start to be great.",
    "It's not about having time, it's about making time.",
    "Push yourself because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "You are capable of amazing things.",
    "Work hard in silence, let your success be your noise.",
    "If you are not willing to risk the usual, you will have to settle for the ordinary.",
    "Do something today that your future self will thank you for.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Great things never come from comfort zones.",
    "The way to get started is to quit talking and begin doing.",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.",
    "It does not matter how slowly you go as long as you do not stop.",
    "The only way to achieve the impossible is to believe it is possible.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes later becomes never. Do it now.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It’s a slow process, but quitting won’t speed it up.",
    "If you get tired, learn to rest, not to quit.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream it. Believe it. Build it.",
    "Success is what happens after you have survived all your mistakes.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Don’t wait for opportunity. Create it.",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Dream big. Pray bigger.",
    "The only place where success comes before work is in the dictionary.",
    "Hard work beats talent when talent doesn’t work hard.",
    "Make each day your masterpiece.",
    "The only way to do great work is to love what you do.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Opportunities don’t happen, you create them.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "You can’t go back and change the beginning, but you can start where you are and change the ending.",
    "Everything you can imagine is real.",
    "Don’t limit your challenges, challenge your limits.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
]

def cleanTerminal():
    os.system('cls' if os.name == "nt" else 'clear')

def showMotivationalQuote():
    return random.choice(motivational_quotes)

def print_ascii(message, font="univers"):
    ascii_art = pyfiglet.figlet_format(message, font=font)
    terminal_width = os.get_terminal_size().columns
    centered_ascii_art = "\n".join([line.center(terminal_width) for line in ascii_art.splitlines()])
    print(centered_ascii_art)

def countdown(minutes, message):
    total_seconds = minutes * 60
    quote = showMotivationalQuote()
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        cleanTerminal()
        print_ascii(message)
        print("\n") 
        print(f"{mins:02}:{secs:02}".center(os.get_terminal_size().columns))
        print("\n")
        print(f"{quote}".center(os.get_terminal_size().columns))
        time.sleep(1)
        total_seconds -= 1
    cleanTerminal()
    print_ascii(message)
    print("\n")
    print("beep beep".center(os.get_terminal_size().columns))
    playsound("./digital_watch_alarm.mp3")
    cleanTerminal()

def pomodoro(work_time, rest_time, sessions):
    for i in range(1, sessions + 1):
        cleanTerminal()
        print_ascii(f"Session {i} / {sessions}")
        countdown(work_time, f"Work! {i}/{sessions}")
        
        if i < sessions:
            cleanTerminal()
            print_ascii(f"Session {i} / {sessions}")
            countdown(rest_time, "Rest")
            cleanTerminal()

    print_ascii("Finished!")
    print("Good work.".center(os.get_terminal_size().columns))

def main():
    signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(0))

    parser = argparse.ArgumentParser(description="Pomodoro Timer CLI")
    parser.add_argument("-w", "--work", type=int, default=25, help="Work time in minutes (default: 25)")
    parser.add_argument("-r", "--rest-time", type=int, default=5, help="Rest time in minutes (default: 5)")
    parser.add_argument("-s", "--sessions", type=int, default=4, help="Number of sessions (default: 4)")

    args = parser.parse_args()
    cleanTerminal()
    pomodoro(args.work, args.break_time, args.sessions)

if __name__ == "__main__":
    main()
