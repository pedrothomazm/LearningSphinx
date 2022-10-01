def get_random_ingredients(kind=None):
    """Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :raise lumache.InvalidKindError: If the kind is invalid.
   :return: The ingredients list.
   :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]

def sum(a, b):
    """Return the sum of a and b

    :param a: first term of sum
    :type a: int or float
    :param b: second term of sum
    :type b: int or float
    :return: the sum of a and b
    :rtype: int or float
    """
    return a + b

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass