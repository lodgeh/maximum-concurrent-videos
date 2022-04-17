import time
from random import randrange


def get_lists():
    """

    """
    i = 0
    v = []
    while i < 1_000_000:
        j = randrange(1, 100)
        k = randrange(10)
        v.append([j, j+k])
        i += 1
    return v


def get_start_and_end_lists(video_play_records: list):
    """

    """
    video_start_and_end_times_list = []
    for record in video_play_records:
        video_start_and_end_times_list.append([record[0], "start"])
        video_start_and_end_times_list.append([record[1], "end"])
    return video_start_and_end_times_list


def sort_video_play_times(video_play_times: list):
    """

    """
    return sorted(video_play_times, key=lambda x: (-x[0], x[1]), reverse=True)


def loop_through_video_play_times(video_play_times: list):
    """

    """
    counter = 0
    maximum_concurrent_videos = 0
    for play_time in video_play_times:
        if play_time[1] == "start":
            counter += 1
            maximum_concurrent_videos = max(counter, maximum_concurrent_videos)
        if play_time[1] == "end":
            counter -= 1
        print(counter, maximum_concurrent_videos)
    return maximum_concurrent_videos


def main():
    video_play_records = get_lists()
    video_start_and_end_times_list = get_start_and_end_lists(
        video_play_records)
    sorted_video_play_times = sort_video_play_times(
        video_start_and_end_times_list)

    tic = time.perf_counter()
    maximum_concurrent_videos = loop_through_video_play_times(
        sorted_video_play_times)
    toc = time.perf_counter()
    print(
        f"Code ran in {toc - tic:0.4f} seconds and there was a maximum of {maximum_concurrent_videos} videos playing at once")


if __name__ == "__main__":
    main()
