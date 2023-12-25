def list_to_int_tuple(search_list):
    int_list = []

    for item in search_list:
        try:
            i = int(item)
            int_list.append(i)
        except ValueError:
            continue

    int_tuple = tuple(int_list)
    return int_tuple