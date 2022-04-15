import csv
from random import randrange


def generate_random_video_plays(rows: int):
    """
    Generates a list of lists where each sub-list contains a start 
    and end time

    Start and end times are in epoch time

    Start time is a randomly generated epoch time between 2022/01/01 
    and 2022/01/31

    End time is calculated by adding a random time between 15 minutes 
    to 3 hours to the start time
    """
    video_plays = []
    for row in range(rows):
        start_time = randrange(1640995200, 1643662799)
        random_play_time = randrange(900, 10800)
        video_plays.append([start_time, start_time+random_play_time])
    return video_plays


def write_to_csv(rows: int, data: list):
    """
    Writes data to a csv file
    """
    with open(f"video_plays_{rows}.csv", "w", newline="", ) as f:
        writer = csv.writer(f)
        header = [["start_time", "end_time"]]
        writer.writerows(header)
        writer.writerows(data)


def main(rows):
    video_plays = generate_random_video_plays(rows)
    write_to_csv(rows, video_plays)


if __name__ == "__main__":
    main(1_000_000)
