# Atomic Time
A python class that gets the current Atomic Time in TIA and UTC formats from https://www.timeanddate.com/time/international-atomic-time.html

### Dependencies:
Requires `lxml` and `requests` modules

### Usage
```
>>> import atomic_time
>>> new_utc_time = atomic_time.UTC()  
>>> print(new_utc_time)  
22:34:43  
>>> new_utc_time.get_hours()  
22  
>>> new_utc_time.get_seconds()  
43
>>> new_utc_time.update_time()  
>>> new_utc_time.get_seconds()  
13
```

### Author
Zach Welden
