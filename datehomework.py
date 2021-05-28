from datetime import datetime, timedelta
delta1 = timedelta (days = 1)
delta2 = timedelta (days = 30)
yesterday = datetime.now() - delta1
monthago = datetime.now() - delta2
print(datetime.now()); print(yesterday); print(monthago)





date_string = '01/01/25 12:10:03.234567'
date_to_date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
date_to_date