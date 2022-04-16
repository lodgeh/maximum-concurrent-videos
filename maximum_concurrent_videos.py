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
    video_play_list = []
    for vi in v:
        video_play_list.append([vi[0], "start"])
        video_play_list.append([vi[1], "end"])
    return video_play_list


def main():
    counter1 = 0
    maximum = 0

    video_list = generate_lists()
    video_play_list = get_start_end_lists(video_list)
    sorted_video_play_times = sorted(video_play_list)

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
