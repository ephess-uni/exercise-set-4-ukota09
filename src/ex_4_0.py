""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile): #function signature
    
    with open(logfile) as file:
        
        lines = file.readlines()

    
    shutdown_events = []
   
    for line in lines:
        
        if "Shutdown initiated" in line:
            
            shutdown_events.append(line.strip())

    # Return the list of shutdown events
    return shutdown_events


# >>>> The code below will call your function and print the results
if _name_ == "_main_":
    print(f"{get_shutdown_events(FILENAME)=}")
