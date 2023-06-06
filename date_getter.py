from datetime import datetime
from seed import res

def get_sorted_dates():
    sorted_dates = []

    for item in res:
        try:
            date_item = datetime.strptime(item, '%Y-%m-%d %H:%M:%S').date()
            sorted_dates.append(date_item)
        except ValueError as err:
            pass
    
    sorted_dates.sort()
    return sorted_dates