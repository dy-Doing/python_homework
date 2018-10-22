def add_number(x, y):
    assert (isinstance(x, int) and isinstance(y, int)), 'Two numbers must be int object'
    return x+y


wrong_eg = add_number(1, 2.0)