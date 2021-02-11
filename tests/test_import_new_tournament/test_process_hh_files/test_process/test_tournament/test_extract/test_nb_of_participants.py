import unittest

from import_new_tournaments.process_hh_files.process.tournament.extract.nb_of_participants import nb_of_participants
from GLOBAL_VARIABLES import FAKE_TOURNAMENT_SUMMARY_FOLDER


class test(unittest.TestCase):
    def test_nb_of_participants(self):

        parent_folder = FAKE_TOURNAMENT_SUMMARY_FOLDER
        ts_filename = 'TS20201217 T23127921 E197421416 NL Hold’em $1.00 + $0.10.ots'

        self.assertEqual(
            nb_of_participants(parent_folder, ts_filename),
            181)
