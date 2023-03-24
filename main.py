from datetime import datetime
from seed import res
from prettytable import PrettyTable

def generatetable(data):
    table = PrettyTable(["Start Date", "End Date", "Count"])

    startDate = data[0]
    previousDate = data[0]
    count = 1

    for date in data:
        diff = (date - previousDate).days
        if diff == 0:
            continue
        elif diff == 1:
            previousDate = date
            count += 1
        else:
            table.add_row([startDate, previousDate, count])
            previousDate = date
            startDate = date
            count = 1

    table.add_row([startDate, previousDate, count])
    result = table.get_string(sortby="Count", reversesort=True)
    print(result)

def getsorteddates():
    result = []

    for item in res:
        try:
            dateitem = datetime.strptime(item, '%Y-%m-%d %H:%M:%S').date()
            result.append(dateitem)
        except ValueError as err:
            pass
    
    result.sort()
    return result

def main():
    sorteddates = getsorteddates()
    generatetable(sorteddates)

if __name__ == "__main__":
    main()

