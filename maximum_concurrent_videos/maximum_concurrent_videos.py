import argparse
import time
from csv import reader


def get_video_plays_from_csv(file_name):
    """
    Reads video record data from a csv file. 

    Expects start and end times to be in Epoch time.

    Returns a list of lists containing video start and end play times.
    """
    with open(file_name) as csv_file:
        csv_reader = reader(csv_file)
        header = next(csv_reader)
        video_plays_records = [[int(row[0]), int(row[1])]
                               for row in csv_reader]
    return video_plays_records


def get_video_play_times(video_play_records: list):
    """
    Loops through video play records list.

    Appends list containing the time and action e.g.: ["1642395175", "start"]
    to video_start_and_end_times_list

    Returns video_start_and_end_times_list
    """
    video_start_and_end_times_list = []
    for record in video_play_records:
        video_start_and_end_times_list.append([record[0], "start"])
        video_start_and_end_times_list.append([record[1], "end"])
    return video_start_and_end_times_list


def sort_video_play_times(video_play_times: list):
    """
    Sorts video_play_times list by first element ascendind and second element
    reverse alphabetically. 
    """
    return sorted(video_play_times, key=lambda x: (-x[0], x[1]), reverse=True)


def get_max_concurrent_video_plays(video_play_times: list):
    """
    Loops through sorted video play times. 

    Adds to counter if "start" and subtracts from counter if "end".

    Compares counter to maximum_concurrent_videos and replaces if counter is higher.

    Returns maximum_concurrent_videos
    """
    counter = 0
    maximum_concurrent_videos = 0
    for play_time in video_play_times:
        if play_time[1] == "start":
            counter += 1
            maximum_concurrent_videos = max(counter, maximum_concurrent_videos)
        if play_time[1] == "end":
            counter -= 1
    return maximum_concurrent_videos


def main(file_name):
    start_timer = time.perf_counter()

    video_play_records = get_video_plays_from_csv(file_name)
    video_start_and_end_times_list = get_video_play_times(video_play_records)
    sorted_video_play_times = sort_video_play_times(
        video_start_and_end_times_list)
    maximum_concurrent_videos = get_max_concurrent_video_plays(
        sorted_video_play_times)

    end_timer = time.perf_counter()

    print(f"{len(video_play_records):,} video records processed in {end_timer - start_timer:0.4f} seconds.")
    print(f"There was a maximum of {maximum_concurrent_videos:,} videos playing at one time.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Process video play times to find the maximum videos playing concurrently')

    parser.add_argument(
        "file_name",
        metavar="file_name",
        type=str,
        help="Name of csv file"
    )
    args = parser.parse_args()
    file_name = args.file_name

    main(file_name)
