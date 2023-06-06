from date_getter import get_sorted_dates
from date_consecutive_getter import get_consecutive_date_table

def main():
    sorted_dates = get_sorted_dates()
    consecutive_dates_table = get_consecutive_date_table(sorted_dates)

    print(consecutive_dates_table)

if __name__ == "__main__":
    main()

