from math import floor


def create_spend_chart(categories: list):
    sum_of_cats = [x.sum_category_withdraws() for x in categories]
    total_sum_of_cats = sum(sum_of_cats)
    percentage = [round(x.sum_category_withdraws() / total_sum_of_cats * 10, 2) for x in categories]

    names = [x.name for x in categories]
    name_length_list = [len(x.name) for x in categories]
    max_length = max(name_length_list)

    o = 'o'
    space = ' '
    list_of_splited_names = []
    for name in names:
        single_name_list = []
        for n in name:
            single_name_list.append(n)
        name_len_diff = max_length - len(name)
        single_name_list.extend(space for _ in range(name_len_diff))
        list_of_splited_names.append(single_name_list)

    list_of_splited_percentages = []
    for p in percentage:
        single_list = []
        y = floor(p) * 10
        blank_difference = int((100 - y) / 10)
        ooos = int(y / 10)
        single_list.extend(space for _ in range(blank_difference))
        single_list.extend(o for _ in range(ooos))
        if p > 0:
            single_list.extend(o)
        else:
            single_list.extend(space)
        single_list.extend(['---'])
        list_of_splited_percentages.append(single_list)

    top = list(zip(*list_of_splited_percentages))
    bottom = list(zip(*list_of_splited_names))

    str1 = f"Percentage spent by category\n100| " \
        f"{'  '.join(top[0])}  \n 90| " \
        f"{'  '.join(top[1])}  \n 80| " \
        f"{'  '.join(top[2])}  \n 70| " \
        f"{'  '.join(top[3])}  \n 60| " \
        f"{'  '.join(top[4])}  \n 50| " \
        f"{'  '.join(top[5])}  \n 40| " \
        f"{'  '.join(top[6])}  \n 30| " \
        f"{'  '.join(top[7])}  \n 20| " \
        f"{'  '.join(top[8])}  \n 10| " \
        f"{'  '.join(top[9])}  \n  0| " \
        f"{'  '.join(top[10])}  \n    -" \
        f"{''.join(top[11])}\n     "

    str2 = []
    for n in bottom:
        str2.append(f"{'  '.join(n)}  \n     ")

    joined_str2 = ''.join(str2)
    display_chart = str1 + joined_str2[:-6:]
    return display_chart
