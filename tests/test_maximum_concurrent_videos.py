import os
import unittest

from maximum_concurrent_videos import maximum_concurrent_videos as m

test_file_path = os.path.join("tests", "test_video_plays.csv")


class TestFunctions(unittest.TestCase):
    def test_read_csv_file(self):
        """
        Tests reading csv correctly
        """
        result = m.get_video_plays_from_csv(test_file_path)
        expected = [
            [1642258105, 1642264582],
            [1642804420, 1642811333],
            [1642894670, 1642902031],
            [1642499398, 1642508900],
            [1643450687, 1643459086],
            [1643449910, 1643452994],
            [1643215430, 1643220621],
            [1643445349, 1643451586],
            [1642809672, 1642811491],
            [1643609779, 1643615874]
        ]
        self.assertEqual(result, expected)

    def test_csv_output_is_int(self):
        """
        Tests to see if value outputs are integers.
        """
        results = m.get_video_plays_from_csv(test_file_path)
        for result in results:
            with self.subTest(i=result):
                self.assertIsInstance(result[0], int)
                self.assertIsInstance(result[1], int)

    def test_video_play_time_splitter(self):
        """
        Tests splitting video play records into seperate lists with correct "start" and "end" labeling.
        """
        result = m.get_video_play_times([[1, 2], [3, 4]])
        expected = [[1, "start"], [2, "end"], [3, "start"], [4, "end"]]
        self.assertEqual(result, expected)

    def test_sorting_intervals(self):
        """
        Tests sorting video play times into correct order
        """
        result = m.sort_video_play_times(
            [[1, "start"], [3, "start"], [2, "end"],  [4, "end"]])
        expected = [[1, "start"], [2, "end"], [3, "start"], [4, "end"]]
        self.assertEqual(result, expected)

    def test_sorting_overlapping_intervals(self):
        """
        Tests sorting video play times into correct order when there are both video "starts"
        and "ends" at the same time.
        """
        result = m.sort_video_play_times(
            [[2, "end"], [2, "start"], [1, "start"], [3, "end"]])
        expected = [[1, "start"], [2, "start"], [2, "end"], [3, "end"]]
        self.assertEqual(result, expected)

    def test_max_concurrent_video_plays(self):
        """
        Tests finding maximum concurrent videos
        """
        result = m.get_max_concurrent_video_plays(
            [[1, "start"], [2, "start"],  [3, "end"], [5, "end"]])
        expected = 2
        self.assertEqual(result, expected)

    def test_max_concurrent_video_plays_with_no_concurrent_videos(self):
        """
        Tests finding maximum concurrent videos when there are no concurrent videos
        """
        result = m.get_max_concurrent_video_plays(
            [[1, "start"], [3, "end"], [4, "start"],  [5, "end"]])
        expected = 1
        self.assertEqual(result, expected)

    def test_max_video_plays_overlapping_start_and_end(self):
        """
        Tests finding maximum concurrent videos when there are both "start" and 
        "end" actions happening at the same time.
        """
        result = m.get_max_concurrent_video_plays(
            [[1, "start"], [2, "start"], [2, "end"], [3, "end"]])
        expected = 2
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
