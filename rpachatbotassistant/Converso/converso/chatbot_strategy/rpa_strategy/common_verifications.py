def validate_date(date: str):
    """ Validates if the date is in the format YYYY-MM-DD.
    :param date: str: The date to be validated.
    :return: bool: True if the date is valid, False otherwise.
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False