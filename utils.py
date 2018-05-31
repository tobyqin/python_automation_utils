import time

DEFAULT_TIMEOUT = 60
DEFAULT_POLL_TIME = 5


def wait_for(method, timeout=DEFAULT_TIMEOUT, poll_time=DEFAULT_POLL_TIME):
    """
    Wait for a method with timeout, return its result or raise error.
    The expecting result should NOT be False or equal to False.
    """

    end_time = time.time() + timeout
    exc_info = ()

    while True:
        try:
            value = method()
            if value:
                return value

        except Exception as exc:
            args_as_str = [str(x) for x in exc.args]
            exc_info = (type(exc).__name__, ','.join(args_as_str))

        time.sleep(poll_time)
        if time.time() > end_time:
            break

    message = "Timeout to wait for '{}()' in {} seconds.".format(
        method.__name__, timeout)

    if exc_info:
        message += " [{}]: {}".format(exc_info[0], exc_info[1])

    raise Exception(message)
