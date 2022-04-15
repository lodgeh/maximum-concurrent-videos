import time
from random import randrange


def generate_lists():
    """
    
    """
    i = 0
    v = []
    while i < 10_000_000:
        j = randrange(1, 100)
        k = randrange(10)
        v.append([j, j+k])
        i += 1
    return v


def get_start_end_lists(v: list):
    """
    
    """
    start_list = []
    end_list = []
    for vi in v:
        start_list.append([vi[0], "a"])
        end_list.append([vi[1], "b"])
    return start_list, end_list


def combine_lists(start_list: list, end_list: list):
    """

    """
    return start_list + end_list


def sort_lists(list_to_sort: list):
    """

    """
    return sorted(list_to_sort)  # is this cheating?


def check_max(counter: int, maximum: int):
    """
    
    """
    if maximum < counter:
        return counter
    else:
        return maximum


def main():
    counter1 = 0
    maximum = 0

    video_list = generate_lists()
    start_list, end_list = get_start_end_lists(video_list)
    combined_list = combine_lists(start_list, end_list)
    s = sort_lists(combined_list)

    tic = time.perf_counter()
    for i in s:
        if i[1] == "a":
            counter1 += 1
            maximum = check_max(counter1, maximum)
        if i[1] == "b":
            counter1 -= 1

        print(f"counter: {counter1}, max: {maximum}")
    toc = time.perf_counter()
    print(f"Code ran in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()
