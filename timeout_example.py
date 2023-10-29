import signal
from contextlib import contextmanager
import time

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds): # define a context manager. This generator needs three parts: pre yeild, yeild and post yeild
    # 1) __enter__
    def signal_handler(signum, frame): # define the signal handler that raises the correct exception when called
        raise TimeoutException()
    signal.signal(signal.SIGALRM, signal_handler) # define the signal
    signal.alarm(seconds) # set the alarm
    # 2) yeild - in this case we have no function to yeild
    yield 
    # 3) __exit__
    signal.alarm(0)


def long_function_call(t):
    time.sleep(t)
    print("function complete")


# try-expect is needed to handle the timeout error
try:
    with time_limit(5): # with uses the contextmanager
        long_function_call(20)
except TimeoutException as e:
    print("Timed out!")
