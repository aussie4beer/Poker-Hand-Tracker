

# ---- 1. Update the db with new data, if there's any
# from hh_import.run import wrapper_import_new as run
# run()


# ---- 2. Play with the API
from db_api.plots.plot_money_won_lost_per_buyin import plot_money_won_lost
#
# plot_money_won_lost(buyin=6.6, sigma=7)

from db_api.plots.plot_chips_won_lost_for_tournament import plot_chips_won_lost_for_tournament
# plot_chips_won_lost_for_tournament(23115737, width=50)

from db_api.plots.plot_rate_of_profit_per_game import plot_rate_of_profit_per_game
plot_rate_of_profit_per_game(buyin=0.55)
