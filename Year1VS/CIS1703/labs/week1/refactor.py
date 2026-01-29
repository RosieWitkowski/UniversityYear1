from __future__ import annotations
"""
Lab goal
You will take a messy, linear script and refactor it into a small engineered application
with:
    ● functions + main()
    ● type hints
    ● docstrings
    ● validation + exception handling
    ● clean data handling (dict/list transformations)
    ● no accidental mutation leaks
"""

# messy_script.py
"""data = input("Enter comma-separated numbers: ")
nums = data.split(",")
total = 0
for n in nums:
    total += float(n)
print("count:", len(nums))
print("sum:", total)
print("avg:", total / len(nums))"""

def main() -> None:
    """CLI entry point."""
    while True:
        try:
            option = input("Input thorugh file (F) or command-line-interace (C)?: ")
            if option[0].upper() == 'F':
                path = input("File path: ")
                data = read_text_file(path)
            else:
                data = input("Enter comma-separated numbers: ")

            values = parse_numbers(data)
            stats = summary(values)
            print(format_summary(stats))   

            option = 'F'
            while option not in ['Y', 'N']:
                option = input("Calculate again? (y/n) ")
                option = option[0].upper()
                if option == 'N':
                    return 
                elif option == 'Y':
                    break

        except ValueError as e:
            print(f"Error: {e}") 

def read_text_file(path: str) -> str:
    try:
        with open(path, 'r') as f:
            data = f.read()
            return data
    except Exception as e:
        raise ValueError("Problem with reading the file.") from e 

def parse_numbers(txt: str) -> list[float]:
    """Parse comma-serperated numbers into a list of floats.

    Args:
        text: User input of comma-seperated numeric tokens, e.g. "5, 8, 3.2".

    Returns:
        list: Parsed floats.

    Raises:
        ValueError: If invalid tokens.
    """
    try:
        tokens = [t.strip() for t in txt.split(',')]
        tokens = [t for t in tokens if t != ""]
    except AttributeError as e:
        raise ValueError("Poblem with reading the file.")

    if not tokens:
        raise ValueError("No values provided. Please provide a list of comma-seperated numbers (e.g. 1, 3, 4).")

    values: list[float] = []
    for t in tokens:
        try:
            values.append(float(t))
        except ValueError as e:
            raise ValueError(f"Invalid number: {t!r}") from e 

    return values 

def summary(values: list[float]) -> dict[str, float]:
    """Calculate total, count and average.

    Args:
        values: non-empty list of floats.

    Returns:
        dict: keys are strings (total, count, average), values are computations.

    Raises:
        ValueError: if values is empty.
    """
    if not values:
        raise ValueError("Values cannot be empty for summary.") from e 

    # Sorted creates a new list as opposed to sort(), avoids mutation
    vals = sorted(values)

    total = sum(values)
    count = int(len(values))
    avg = total / count
    median = calc_median(values, count)
    smallest, biggest = values[0], values[count-1]

    return({"total": total, "count": float(count), "avg": avg, "med": median, "small": smallest, "big": biggest})

def calc_median(values: list[float], count: float) -> float:
    mid = count // 2
    if count % 2 == 1:
        return values[mid]
    return (values[mid - 1] + values[mid]) / 2.0



def format_summary(stats: dict[str, float]) -> str:
    """Format summary for display."""
    return(
        f"+--- Summary ---+\n"
        f"Total: {int(stats['total'])}\n"
        f"Count: {stats['count']:.2f}\n"
        f"Average: {stats['avg']:.3f}\n"
        f"Median: {stats['med']:.2f}\n"
        f"Min: {stats['small']:.2f}\n"
        f"Max: {stats['big']:.2f}"
    )

if __name__ == "__main__":
    main()