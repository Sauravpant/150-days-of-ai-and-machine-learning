from logger import logging


def add_numbers(a, b):
    logging.info(f"Adding numbers {a} and {b}")
    return a + b


def divide_numbers(a, b):
    try:
        result = a / b
        logging.info(f"Dividing numbers {a} by {b}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero")
        return None


add_numbers(5, 3)
divide_numbers(10, 5)
