import unittest
from import_new_tournaments.process_hh_files.process.hands.extract.tournament_id import tournament_id
from GLOBAL_VARIABLES import TEST_RANDOM_HAND_HISTORIES_FOLDER
from import_new_tournaments.process_hh_files.process.tournament.extract.hands import get_hands_in_list


class test(unittest.TestCase):
    def test_tournament_id(self):
        hands = get_hands_in_list(TEST_RANDOM_HAND_HISTORIES_FOLDER, ["HH20201217 SITGOID-G23140753T3 TN-$0{FULLSTOP}50 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt"])

        expected_tournament_id = [
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753,
            23140753]

        for idx, h in enumerate(hands):
            self.assertEqual(tournament_id(h), expected_tournament_id[idx])
