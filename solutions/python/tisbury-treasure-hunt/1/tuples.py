"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    name, coordinates = record
    return coordinates
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    pass


def convert_coordinate(coordinate):
    return tuple(coordinate)
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    pass


def compare_records(azara_record, rui_record):
    name, coordinates1 = azara_record
    name1, coordinates2, color = rui_record
    return tuple(coordinates1) == coordinates2
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """

    pass


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """

    pass


def clean_up(combined_record_group):
    cleaned = []
    for record in combined_record_group:
        new_record = record[:1] + record[2:]
        cleaned.append(new_record)
    return "\n".join(str(rec) for rec in cleaned) + "\n"
    
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """

    pass
