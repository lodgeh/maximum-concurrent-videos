import time
from random import randrange


def get_lists():
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


def get_start_end_lists(video_play_records: list):
    """

    """
    video_start_and_end_times_list = []
    for record in video_play_records:
        video_start_and_end_times_list.append([record[0], "start"])
        video_start_and_end_times_list.append([record[1], "end"])
    return video_start_and_end_times_list


def main():
    counter1 = 0
    maximum = 0

    video_play_records = get_lists()
    video_start_and_end_times_list = get_start_end_lists(video_play_records)
    sorted_video_play_times = sorted(video_start_and_end_times_list)

    tic = time.perf_counter()
    for video_play_time in sorted_video_play_times:
        if video_play_time[1] == "start":
            counter1 += 1
            maximum = max(counter1, maximum)
        if video_play_time[1] == "end":
            counter1 -= 1

        print(f"counter: {counter1}, max: {maximum}")
    toc = time.perf_counter()
    print(f"Code ran in {toc - tic:0.4f} seconds")


if __name__ == "__main__":

    main()
