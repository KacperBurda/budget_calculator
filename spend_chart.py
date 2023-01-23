from math import floor


def create_spend_chart(categories: list):
    sum_of_cats = sum([x.sum_category_withdraws() for x in categories])
    percentage = [round(x.sum_category_withdraws() / sum_of_cats * 10, 2) for x in categories]

    names = [x.name for x in categories]
    max_length = max([len(x.name) for x in categories])

    o = 'o'
    space = ' '
    list_of_splited_names = []
    for name in names:
        single_name_list = [n for n in name]
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

    title = f"Percentage spent by category\n"
    top = list(zip(*list_of_splited_percentages))
    bottom = list(zip(*list_of_splited_names))

    str1 = f"100| {'  '.join(top[0])}  \n" \
           f" 90| {'  '.join(top[1])}  \n" \
           f" 80| {'  '.join(top[2])}  \n" \
           f" 70| {'  '.join(top[3])}  \n" \
           f" 60| {'  '.join(top[4])}  \n" \
           f" 50| {'  '.join(top[5])}  \n" \
           f" 40| {'  '.join(top[6])}  \n" \
           f" 30| {'  '.join(top[7])}  \n" \
           f" 20| {'  '.join(top[8])}  \n" \
           f" 10| {'  '.join(top[9])}  \n" \
           f"  0| {'  '.join(top[10])}  \n" \
           f"    -{''.join(top[11])}\n     "

    str2 = [f"{'  '.join(n)}  \n     " for n in bottom]

    joined_str2 = ''.join(str2)
    display_chart = title + str1 + joined_str2[:-6:]
    return display_chart
