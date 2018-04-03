import datetime
import sys

if(len(sys.argv) != 4):
    print('usage: $ python', sys.argv[0], 'year month day')
    quit()

today = datetime.date.today()
birthday = datetime.date(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))

life = today - birthday

year = today.year - birthday.year
month = today.month - birthday.month
day = today.day - birthday.day

print(birthday, '->', today)

if(not((year >= 0) and (month >= 0) and (day >= 0))):
    year -= 1

print(year, 'years', end=' = ')
print(life.days, 'days')
