def alarm_clock(day, vacation):
    if not vacation:
        if day == 0 or day == 6:
            time = '10:00'
        else:
            time = '7:00'
    elif vacation:
        if day == 0 or day == 6:
            time = 'off'
        else:
            time = '10:00'
    return time