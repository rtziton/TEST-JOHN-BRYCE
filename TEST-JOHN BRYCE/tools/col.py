# tools/col.py

def myzip(it1, it2):
    """
    A simplified version of the zip function for two collections.

    Parameters:
    - it1 (iterable): The first iterable.
    - it2 (iterable): The second iterable.

    Returns:
    list: A list of tuples, where each tuple contains elements from it1 and it2.
    """
    return list(zip(it1, it2))
