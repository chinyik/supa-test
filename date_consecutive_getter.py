from prettytable import PrettyTable

def get_consecutive_date_table(data):
    table = PrettyTable(["START", "END", "LENGTH"])

    current_start_date = data[0]
    current_end_date = data[0]
    consecutive_days_count = 1
    
    for index, date in enumerate(data[1:], 1):
        diff = (data[index] - data[index-1]).days
        if diff == 0 or diff == 1:
            current_end_date = data[index]
            consecutive_days_count += 1
        else:
            table.add_row([current_start_date, current_end_date, consecutive_days_count])
            current_start_date = data[index]
            current_end_date = data[index]
            consecutive_days_count = 1

    table.add_row([current_start_date, current_end_date, consecutive_days_count])
    
    sorted_table = table.get_string(sortby="LENGTH", reversesort=True)

    return sorted_table