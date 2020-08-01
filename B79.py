import random


def split_name(names):
    return names.split()


def generate_conversion_list():
    alphabets = list("abcdefghijklmnopqrstuvwxyz")

    alphabet_dict = {}
    for num, c in enumerate(alphabets):
        alphabet_dict[c] = num + 1

    return alphabet_dict


def convert_name_to_num(conversion_list, name):
    # NOTE：この書き方もできるよ
    # buddy_point_list = []
    # for n in list(name):
    #     buddy_point_list.append(conversion_list[n])
    return [conversion_list[n] for n in list(name)]


def calculate_buddy_point(buddy_point):
    return random.randint(0, 100)


def generate_structured_buddy_point(converted_names):
    '''
    相性チェックの計算のためにconverted_namesから計算用数列を生成する❤️
    '''
    return [
        converted_names[0] + converted_names[1],
        converted_names[1] + converted_names[0]]


if __name__ == "__main__":
    test_name = "rose hiyo"
    names = split_name(test_name)
    conversion_list = generate_conversion_list()

    # Convert name from alphabet to number for calculating buddy point
    converted_names = []

    calculate_results = []

    for name in names:
        converted_names.append(convert_name_to_num(conversion_list, name))

    buddy_point_list = generate_structured_buddy_point(converted_names)

    for buddy_point in buddy_point_list:
        calculate_results.append(
            calculate_buddy_point(buddy_point)
        )

    # Print maximam buddy point
    print(max(calculate_results))
