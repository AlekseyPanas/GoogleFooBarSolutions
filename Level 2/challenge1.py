

def solution(l):
    # splits strings into lists
    array_form = [ver.split(".") for ver in l]
    dict_form = {}

    # Converts list into dictionary (separates into blocks by major version)
    for itm in array_form:
        # Adds 1 to every version value
        new_itm = [int(i) + 1 for i in itm]

        # Adds 0s to represent missing values (no other 0s exist since 1s were added)
        while len(new_itm) != 3:
            new_itm.append(0)

        # Divides versions into dictionary by their major versions
        try:
            dict_form[new_itm[0]].append(new_itm)
        except KeyError:
            dict_form[new_itm[0]] = [new_itm]

    new_arr = []

    # Sorts each dictionary block
    for itm in dict_form:
        dict_form[itm] = sorted(dict_form[itm])

        # Adds each value from the sorted block to the new array
        for itm1 in dict_form[itm]:
            new_arr.append(itm1)

    # Reverts initial "add 1" and "append 0s" from the first for loop and converts to string
    for itm in range(len(new_arr)):
        # Removes 0s according to how many there are
        if new_arr[itm][1] == 0:
            new_arr[itm] = new_arr[itm][:1]
        elif new_arr[itm][2] == 0:
            new_arr[itm] = new_arr[itm][:2]

        # Subtracts 1 (since 1 was added in first loop) and converts to string
        new_arr[itm] = [str(int(i) - 1) for i in new_arr[itm]]

        # Joins string by periods
        new_arr[itm] = ".".join(new_arr[itm])

    return new_arr


print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "2.0", "2.0.11", "2.1.0", "1.0.0", "1"]))
