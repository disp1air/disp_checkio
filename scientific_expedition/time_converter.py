def time_converter(time: str):
    time_arr = time.split(':')
    
    if time_arr[0] == '00':
        return f'{12}:{time_arr[1]} a.m.'
    elif time_arr[0] == '12':
        return f'{time} p.m.'
    elif int(time_arr[0]) >= 13:
        return f'{int(time_arr[0]) - 12}:{time_arr[1]} p.m.'
    else:
        return f'{int(time_arr[0])}:{time_arr[1]} a.m.'


def time_converter(time):
    hours, minutes = int(time.split(':')[0]), time.split(':')[1]
    if hours >=12:
        if hours >12:
            hours = hours - 12
        time = "{}:{} p.m.".format(hours,minutes)
    else:
        if hours == 0:
            hours += 12
        time = "{}:{} a.m.".format(hours,minutes)
    return time


def time_converter(time):
        
    if time[:2] == "00":
        hour = "12"
    elif int(time[:2]) < 13:
        hour = str(int(time[:2]))       
    else:
        hour = str(int(time[:2])-12)

    part = ' a.m.' if int(time[:2]) < 12 else ' p.m.'    
    time = hour + ":" + time[3:] + part

    return time


if __name__ == '__main__':
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
