# plbdays

`plbdays` is a Python library designed to determine business days in Poland. This library provides functions to check if a date is a business day, find the last or next business day, and generate a list of business days between two dates. It is useful for handling date calculations in business applications that adhere to Polish holidays and weekends.

## Features

- **Check if a date is a business day**
- **Find the most recent business day before or on a given date**
- **Find the next business day after or on a given date**
- **Generate a list of business days between two dates**

## Installation

```bash
pip install plbdays
```
or
```bash
git clone https://github.com/yourusername/plbdays.git
```
## Usage

### `isBusinessDay(date='today')`

Checks if a given date is a business day in Poland.

- **Parameters:**
  - `date` (str, optional): The date to check in 'YYYY-MM-DD' format or as a datetime object. Defaults to 'today'.
- **Returns:**
  - `bool`: True if the date is a business day, False otherwise.

**Example:**

```python
from plbdays import isBusinessDay

print(isBusinessDay('2024-07-23'))  # Output: True or False
```

### `lastBD(date='today')`

Finds the most recent business day before or on the given date.


- **Parameters:**
  - `date` (str, optional): The date to check in 'YYYY-MM-DD' format or as a datetime object. Defaults to 'today'.
- **Returns:**
  - `str`: The most recent business day in 'YYYY-MM-DD' format.

**Example:**

```python
from plbdays import lastBD

# Find the last business day before or on a specific date
print(lastBD('2024-07-24'))  # Output: '2024-07-23'

# Find the last business day before or on today
print(lastBD())  # Output: 'YYYY-MM-DD' of the most recent business day
```

### `nextBD(date='today')`

Finds the next business day after or on the given date.


- **Parameters:**
  - `date` (str, optional): The date to start from in 'YYYY-MM-DD' format or as a datetime object. Defaults to 'today'.
- **Returns:**
  - `str`: The next business day in 'YYYY-MM-DD' format.

**Example:**

```python
from plbdays import lastBD

# Find the next business day after or on a specific date
print(nextBD('2024-07-24'))  # Output: '2024-07-25'

# Find the next business day after or on today
print(nextBD())  # Output: 'YYYY-MM-DD' of the next business day
```

### `BDays_list(start_date, end_date)`

Generates a list of business days between two dates.

- **Parameters:**
  - `start_date` (str, optional): The start date in 'YYYY-MM-DD' format.
  - `end_date` (str, optional): The end date in 'YYYY-MM-DD' format.

- **Returns:**
  - `list of lists`: Each sublist contains a date in 'YYYY-MM-DD' format and a boolean indicating if it's a business day.

**Example:**

```python
from plbdays import BDays_list

# Generate a list of business days between two dates
print(BDays_list('2024-07-20', '2024-07-25'))
# Output: [['2024-07-20', False], ['2024-07-21', False], ['2024-07-22', True], ['2024-07-23', True], ['2024-07-24', True], ['2024-07-25', True]]
```

## Usage
 - Python 3.x

## License

This project is licensed under the MIT License.