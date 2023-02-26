""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def num_shutdowns(logfile):

    shutdown_events = get_shutdown_events(logfile)

    count = len(shutdown_events)

    return count
    
    
    
# >>>> The code below will call your function and print the results
if _name_ == "_main_":
    print(f'{num_shutdowns(FILENAME)=}')
