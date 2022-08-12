import time


def plug():
    print("Keeping container alive\n")
    time.sleep(60)
    plug()


plug()
