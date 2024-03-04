import time

# Seconds since epoch (January 1, 1970, 00:00:00)
def since_epoch():
    epoch = time.time()
    return(epoch)

# Current local time
def local_time():
    local = time.localtime()
    return(local)

# Current time in a readable format
def readable_local():
    rltime = time.ctime()
    return(rltime)

# Current time in UTC format
def utc_time():
    utc = time.gmtime()
    return(utc)

# Current time in a readable UTC format
def readable_utc():
    rutime = time.asctime(utc_time())
    return(rutime)

# Converts time tuple to calculate elapsed time since epoch
def custom_epoch():
    ttuple = (2024, 3, 3, 16, 11, 0, 0, 0, 0)
    elap_time = time.mktime(ttuple)
    return(elap_time)

# Delays the execution of code for a set time, in seconds
def sleep():
    count = 0
    while count <= 3:
        print(count)
        count += 1
        time.sleep(1)

# Converts a time tuple into a custom format
def custom_time_format():
    formatted_time = time.strftime("%m-%d-%Y %H:%M:%S", local_time())
    return(formatted_time)

# Converts a time string into a tuple
def time_tuple():
    time_tuple = time.strptime(custom_time_format(), "%m-%d-%Y %H:%M")
    return(time_tuple)

FUNCTION = custom_time_format()
print(FUNCTION)