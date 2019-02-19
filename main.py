from CustomEventHandler import CustomEventHandler
from watchdog.observers import Observer


if __name__ == "__main__":
    print("Avvio test main")

    # converter = Csv2FltConverter("C:\\Users\\nicola\\Desktop\\15x15-tile15p5-um-d.csv")
    # converter.start()
    # converter.join()

    eventHandler = CustomEventHandler()
    obs = Observer()
    obs.schedule(eventHandler, "C:\\Users\\nicola\\Desktop")
    obs.start()
    obs.join()
