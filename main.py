from CustomEventHandler import CustomEventHandler
from watchdog.observers import Observer


if __name__ == "__main__":
    print("Avvio test main")

    # converter = Csv2FltConverter("C:\\Users\\nicola\\Desktop\\15x15-tile15p5-um-d.csv")
    # converter.start()
    # converter.join()

    watchedDogPath = "C:\\Users\\nicola\\Desktop"
    destinationPath = "C:\\Users\\nicola\\Desktop"
    # eventHandler = CustomEventHandler(watchedDogPath)
    eventHandler = CustomEventHandler(watchedDogPath, destinationPath)
    obs = Observer()
    try:
        obs.schedule(eventHandler, watchedDogPath)
        obs.start()
        obs.join()
    except FileNotFoundError as fnfEx:
        print("Path di osservazione non trovata")
