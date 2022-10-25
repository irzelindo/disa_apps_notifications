import psutil
import autopep8


def check(process_name):
    """
    Check if there is any running process that contains the given name process_name.
    Parameters:
        String: process_name
    Returns:
        Boolean: True or False depending if the process is running
    """
    for process in psutil.process_iter():
        print(process.name())
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(e)
    return False

