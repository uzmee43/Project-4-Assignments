# Constants
DAYS_IN_YEAR: int = 365
HOURS_PER_DAY: int = 24
MINUTES_PER_HOUR: int = 60
SECONDS_PER_MINUTE: int = 60

def calculate_seconds_in_year() -> int:
    return DAYS_IN_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE

def main() -> None:
    total_seconds: int = calculate_seconds_in_year()
    print(f"There are {total_seconds} seconds in a year!")

if __name__ == '__main__':
    main()
# This program calculates the number of seconds in a year.