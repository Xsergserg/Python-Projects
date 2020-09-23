def ask_number(qwestion, low, high):

    response = None
    while response not in range(low, high, krat):
        response = int(input(qwestion))
    return response


