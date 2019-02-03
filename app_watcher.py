from AppMonitor.validatorlib.app import AppValidator
from threading import Lock
import sys
import time

spinner = ['|', '/', '-', '\\']


def interval():
    return 5


def main():
    mutex = Lock()
    AppValidator("http://google.com", mutex).start()
    AppValidator("http://googlers.com", mutex, interval).start()
    AppValidator("http://asdfa.com", mutex, interval).start()

    idx = 0

    while True:

        w_str = spinner[idx]
        sys.stdout.write("\b" * len(w_str))
        sys.stdout.write(w_str)
        sys.stdout.flush()
        time.sleep(.28)

        idx = idx + 1

        if not (idx < len(spinner)):
            idx = 0


if __name__ == '__main__':
    main()
