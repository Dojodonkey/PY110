'''
Some people believe that Fridays that fall on the 13th day of the month are unlucky days.
Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year.
You may assume that the year is greater than 1752,
which is when the United Kingdom adopted the modern Gregorian Calendar.
You may also assume that the same calendar will remain in use for the foreseeable future.

P:

- input: integer (year)
- output: integer (amount of fridays in that year)

- explicit rules:
    - return the number of months which friday lands on the 13th.
- implicit rules:
    - none

- questions:
    - none

E:
```python
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
```
D:

- integer to keep count of months which friday lands on the 13th.

- High Level Strategy:
    - using the datetime module, keep a count of the months which friday lands on the 13th
    of the specified year.

A:

1. import the datetime module.
2. create a count to keep track of months which friday lands on the 13th,
starting at 0.
3. iterate through months in the year (12).
4. using the .day attribute, if the 13th is equal to 4, update the count by 1.

C:
'''
import datetime

def friday_the_13ths(year):
    friday_13_count = 0
    for month in range(1, 13):
        day = datetime.date(year, month, 13)
        if day.weekday() == 4:
            friday_13_count += 1
    return friday_13_count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
print(friday_the_13ths(2026))