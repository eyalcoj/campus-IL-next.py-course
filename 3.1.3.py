def raise_stop_iteration():
    iterator = iter([1, 2, 3])
    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator)


def raise_zero_division_error():
    result = 10 / 0


def raise_assertion_error():
    assert False, " W "


def raise_import_error():
    import non_existent_module


def raise_key_error():
    my_dict = {'a': 1, 'b': 2}
    value = my_dict['c']


def raise_syntax_error():
    eval("1 +")


def raise_indentation_error():
    exec("def defy():\n  return 1\n   return 2")


def raise_type_error():
    result = "69" + 42


if __name__ == "__main__":
    pass
    # raise_stop_iteration()
    raise_zero_division_error()
    # raise_assertion_error()
    # raise_import_error()
    # raise_key_error()
    # raise_syntax_error()
    # raise_indentation_error()
    # raise_type_error()
