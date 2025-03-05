"""
Consultar: 
    https://docs.python.org/3/library/time.html

"""
import time

class Date:
    SECS_PER_DAY = 86_400

    def __init__(self, year: int, month: int, day: int):
        # VALIDAÇÕES
        if year < 1900:
            raise InvalidDateValues(f'year should be >= 1900 and not {year}')

        if not 1 <= month <= 12:
            raise InvalidDateValues(f'invalid month {month}')

        valid_date_parts = (
                1 <= day <= 31 and month in (1, 3, 5, 7, 8, 10, 12)
            or  1 <= day <= 30 and month in (4, 6, 9, 11)
            or  1 <= day <= 29 and month == 2 and is_leap_year(year)
            or  1 <= day <= 28 and month == 2 and not is_leap_year(year)
        )
        if not valid_date_parts:
            raise InvalidDateValues(f'invalid day {day} for month {month}')

        self.year = year
        self.month = month
        self.day = day
    #:

    @classmethod
    def from_iso(cls, date: str) -> 'Date':
        date_parts = date.split('-')
        return cls(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
    #:

    @classmethod
    def from_julian(cls, date: int) -> 'Date':
        date_str = str(date)
        if len(date_str) != 8:
            raise InvalidDateValues(f'Invalid julian date: {date_str}')
        return cls(int(date_str[0:4]), int(date_str[4:6]), int(date_str[6:8]))
    #:

    @classmethod
    def today(cls) -> 'Date':
        s = time.localtime()
        return cls(s.tm_year, s.tm_mon, s.tm_mday)
    #:

    def __str__(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'
    #:

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.year}, {self.month}, {self.day})'
    #:

    @property
    def is_leap_year(self):
        return is_leap_year(self.year)
    #:

    def __add__(self, days: int) -> 'Date':
        days_in_secs = days * Date.SECS_PER_DAY
        new_time = self.time + days_in_secs
        new_date = time.localtime(new_time)
        return Date(new_date.tm_year, new_date.tm_mon, new_date.tm_mday)
    #:

    def __radd__(self, days: int):
        return self + days
    #:

    def __sub__(self, days_or_date: 'int | Date') -> 'Date | int':
        if isinstance(days_or_date, int):
            return self.__add__(-days_or_date)
        time_diff = self.time - days_or_date.time
        return int(time_diff / Date.SECS_PER_DAY)
    #:

    def __eq__(self, obj) -> bool:
        if not isinstance(obj, Date):
            return False
        return self.year == obj.year and self.month == obj.month and self.day == obj.day
    #:

    @property
    def time(self) -> float:
        return time.mktime(time.strptime(str(self), '%Y-%m-%d'))
    #:
#:

def is_leap_year(year: int):
    return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)
#:

class InvalidDateValues(ValueError):
    pass
#:

def test():
    dt0 = Date(2025, 3, 15)
    dt1 = Date(2024, 2, 27)
    print(f'{dt1.year = }')     # 2024
    print(f'{dt1.month = }')    # 2
    print(f'{dt1.day = }')      # 27
    print(f'{dt1.is_leap_year = }')  # True
    print(dt1)                 # 2024-02-27

    iso_date = '2024-02-27'
    dt2 = Date.from_iso('2024-02-27')
    print(f'iso_date {iso_date} => Date {dt2}')
    print(f'dt1 == dt0? {dt1 == dt0}')          # True
    print(f'dt1 == dt2? {dt1 == dt2}')          # True

    julian_date = 20240227
    print(f'julian_date {julian_date} => Date {Date.from_julian(julian_date)}')

    print(f'{dt1} + 2 = {dt1 + 2}')
    print(f'{dt1} - 2 = {dt1 - 2}')

    dt4 = Date(2024, 3, 3)
    print(f'{dt4} - {dt1} = {dt4 - dt1}')    # 5 
    print(f'{dt1} - {dt4} = {dt1 - dt4}')    # -5 

    print(f'Today is {Date.today()!r}')

    invalid_dates = (
        '2024-13-11', 
        '2024-04-31', 
        '2025-02-29', 
        '2025-07-32',
        '1890-02-15',
    )
    for invalid_date in invalid_dates:
        try:
            Date.from_iso(invalid_date)
        except InvalidDateValues:
            print(f"Data {invalid_date} inválida")
#:

