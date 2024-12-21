#!/usr/bin/env python3

import argparse
import time
import os

def countdown(minutes, message):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"{message}: {mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("\n" + message + " terminado!")

def pomodoro(work_time, break_time, sessions):
    for i in range(1, sessions + 1):
        print(f"\n--- Sesión {i} de {sessions} ---")
        countdown(work_time, "Tiempo de trabajo")
        if i < sessions:
            countdown(break_time, "Tiempo de descanso")
    print("\n¡Pomodoro completado!")

def main():
    parser = argparse.ArgumentParser(description="Pomodoro Timer CLI")
    parser.add_argument("-w", "--work", type=int, default=25, help="Tiempo de trabajo en minutos (default: 25)")
    parser.add_argument("-b", "--break-time", type=int, default=5, help="Tiempo de descanso en minutos (default: 5)")
    parser.add_argument("-s", "--sessions", type=int, default=4, help="Cantidad de sesiones (default: 4)")

    args = parser.parse_args()

    pomodoro(args.work, args.break_time, args.sessions)

if __name__ == "__main__":
    main()
