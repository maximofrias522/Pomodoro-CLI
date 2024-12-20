import time

def pomodoro_timer(work_minutes=25, short_break=5, long_break=15, cycles=4):
    """Función principal del temporizador Pomodoro."""
    for cycle in range(1, cycles + 1):
        print(f"\nCiclo {cycle}/{cycles}: Trabajo por {work_minutes} minutos.")
        countdown(work_minutes * 60)
        
        if cycle < cycles:
            print(f"Descanso corto por {short_break} minutos.")
            countdown(short_break * 60)
        else:
            print(f"Descanso largo por {long_break} minutos.")
            countdown(long_break * 60)

def countdown(seconds):
    """Cuenta regresiva en segundos."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")  # Reemplaza la línea para simular cuenta regresiva
        time.sleep(1)
        seconds -= 1
    print("¡Tiempo terminado!")

if __name__ == "__main__":
    print("Bienvenido al temporizador Pomodoro CLI.")
    pomodoro_timer()
