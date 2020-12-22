from datetime import datetime
from helpers.check_no_tourney_summary import check_no_tourney_summary
from helpers.extract_id_from_title import extract_id_from_title

def extract_price_from_title(title: str) -> float:
    if "$0{FULLSTOP}50 Hold'Em Turbo" in title:
        return 0.55


def extract_id_from_content(content: str) -> int:
    return int(content.split('\n')[0].split('Tournament ')[1][1:9])


def extract_finished_time_from_content(content: str) -> str:
    all_times = []
    for line in content.split('\n'):
        if ')- 2' in line:
            all_times.append('2' + line.split(')- 2')[1].replace(' UTC', ''))
    return all_times[-1]


def extract_elapsed_time_from_content(content: str) -> int:
    all_times = []

    for line in content.split('\n'):
        if ')- 2' in line:
            all_times.append('2' + line.split(')- 2')[1].replace(' UTC', ''))

    last_hand_time = datetime.strptime(all_times[-1].replace('/', '-'), '%Y-%m-%d %H:%M:%S')
    first_hand_time = datetime.strptime(all_times[0].replace('/', '-'), '%Y-%m-%d %H:%M:%S')

    duration = last_hand_time - first_hand_time
    duration_in_mn = duration.total_seconds()/60

    return round(duration_in_mn)


def extract_nb_of_participants(tourney_summary: dict):
    if check_no_tourney_summary(tourney_summary): return None
    return tourney_summary['player_count']


def extract_prize(tourney_summary: dict):
    if check_no_tourney_summary(tourney_summary): return None
    for player in tourney_summary['tournament_finishes_and_winnings']:
        if player['player_name'] == 'PotNoodle99912':
            return player['prize']


def extract_position(tourney_summary: dict):
    if check_no_tourney_summary(tourney_summary): return None
    for player in tourney_summary['tournament_finishes_and_winnings']:
        if player['player_name'] == 'PotNoodle99912':
            return player['finish_position']

# -------


def extract_new_tournament(tourney_title: str, hands: list, tourney_summary: dict) -> dict:
    return {
        'id': extract_id_from_title(tourney_title),
        'price': extract_price_from_title(tourney_title),
        'finished_time': extract_finished_time_from_content(hands[-1]),
        'elapsed_time': extract_elapsed_time_from_content(hands[0] + hands[-1]),
        'prize': extract_prize(tourney_summary),
        'position': extract_position(tourney_summary)
    }