from datetime import datetime



#------------------------------------------------------------
# creating the hour and minute info
def time():
    '''Create the time info.
        Args: It doesn't take any argument.
        Return:
            time (str): An info which is formatted like hour:minutes:seconds
        Example:
            t = ml.whatTime()
    '''
    now = datetime.now()
    hour = now.strftime('%H')
    minutes = now.minute
    seconds = now.strftime('%S')
    time = f'{hour}:{minutes}:{seconds}'
    return time


#------------------------------------------------------------

