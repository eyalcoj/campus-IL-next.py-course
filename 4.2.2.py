def parse_ranges(ranges_string):
    range_tuples_generator = (
        tuple(rang.split('-')) for rang in ranges_string.split(',')
    )

    numbers_generator = (num
                         for start_str, end_str in range_tuples_generator
                         for num in range(int(start_str), int(end_str) + 1)
                         )

    return numbers_generator


if __name__ == "__main__":
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))
