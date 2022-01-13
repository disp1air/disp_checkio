from datetime import date

def days_diff(a, b):
    second_date = date(b[0], b[1], b[2])
    first_date = date(a[0], a[1], a[2])

    if b[0] > a[0] or b[1] > a[1] or b[2] > a[2]:
        return (second_date - first_date).days
    return (first_date - second_date).days
    

from datetime import datetime

def days_diff(date1, date2):
    return abs((datetime(*date1)-datetime(*date2)).days)


from datetime import date
def days_diff(date1, date2):
   f=date(*date1)
   b=date(*date2)
   a=(f-b).days
   return abs(a)


if __name__ == "__main__":
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
