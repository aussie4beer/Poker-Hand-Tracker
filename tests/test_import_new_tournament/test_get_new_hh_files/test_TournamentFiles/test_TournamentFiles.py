#
# import unittest
# from import_new_tournaments.get_new_hh_files.TournamentFiles.TournamentFiles import TournamentFiles
#
#
# class test(unittest.TestCase):
#     def test_TournamentFiles(self):
#         f = TournamentFiles(tournament_id=123)
#         f.add_hand_history_filename('test_hh')
#         f.set_tournament_summary_filename('test_ts')
#         f.set_re_entries(3)
#
#         self.assertEqual(
#             f.re_entries, 3
#         )
#
#         self.assertEqual(
#             f.tournament_id, 123
#         )
#
#         self.assertEqual(
#             f.hand_history_filenames, ['test_hh']
#         )
#
#         self.assertEqual(
#             f.tournament_summary_filename, 'test_ts'
#         )
#
