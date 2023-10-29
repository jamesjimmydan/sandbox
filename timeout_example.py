import signal
from contextlib import contextmanager
import time

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def long_function_call(t):
    time.sleep(t)
    print("function complete")



try:
    with time_limit(10):
        long_function_call(8)
except TimeoutException as e:
    print("Timed out!")
