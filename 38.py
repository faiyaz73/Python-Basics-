# Datetime

# datatime module is a get hour, mint, second
# import a module named datatime to work with dates as date objects

import datetime
x =  datetime.datetime.now()
print(x)
y = datetime.datetime(2002,2,17)
print(y)

# He methods ic is called strftime(),and takes and one parameter, format to specified the format
# of the returned string
#
#
# Format Code	                                            Meaning	Example
# `%Y`   	Year with century as a decimal number             	2024
# `%m`	Month as a zero-padded decimal number	              01 (for January)
# `%d`	Day of the month as a zero-padded decimal number	  16
# `%H`	Hour (00 to 23)	15 (for 3:00 PM)
# `%S`	Second (00 to 59)	45
# `%a`	Abbreviated weekday name	Mon
# `%b`	Abbreviated month name	Jan
# `%c`	Locale’s appropriate date and time representation	Mon Jan 16 15:30:45 2024
# `%I`	Hour (01 to 12)	03 (for 3:00 PM)
# `%p`	AM or PM	PM
# `%x`	Locale’s appropriate date representation	01/16/24 (for January 16, 2024)
# `%Z`	Time zone name (empty string if the object is naive)	UTC
# `%j`	Day of the year as a zero-padded decimal number	16
# `%U`	Week number of the year (Sunday as the first day of the week)	3
# `%W`	Week number of the year (Monday as the first day of the week)	3
# `%%`	A literal ‘%’ character	%
# `%f`	Microsecond as a decimal number (000000 to 999999)	500000
# `%G`	ISO 8601 year with century as a decimal number	2024
# `%V`	ISO 8601 week number of the year (01 to 53)	3
# %U	Week number of the year (Sunday as the first day of the week)	3
# %W	Week number of the year (Monday as the first day of the week)	3
# %y	Year without century as a zero-padded decimal number	24
# %Z	Time zone offset in seconds (empty string if the object is naive)	0
# %%	A literal ‘%’ character	%
# %f	Microsecond as a decimal number (000000 to 999999)	500000
# %G	ISO 8601 year with century as a decimal number	2024
# %V	ISO 8601 week number of the year (01 to 53)	3
# %C	Century as a decimal number (the year divided by 100 and truncated to an integer)	20
# %D	Short date representation (equivalent to ‘%m/%d/%y’)	01/16/24
# %e	Day of the month as a decimal number, space-padded (1 to 31)	16
# %h	Abbreviated month name (equivalent to %b)	Jan
# %k	Hour (0 to 23) space-padded	15 (for 3:00 PM)
# %l	Hour (1 to 12) space-padded	3 (for 3:00 PM)
# %n	Newline character
# %r	Locale’s 12-hour clock time (am/pm)	3:30:45 PM
# %T	Locale’s 24-hour clock time	15:30:45


#
x = datetime.datetime.now()
print(x)
m = x.strftime("%y")
# n = x.strftime("%D")
# print(m)
# print(n)