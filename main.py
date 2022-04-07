from app import App
from game import Game
from settings import *


def update_gui(game1):
    print("updating gui...")
    print(game1)


def play(game):
    game.deck.shuffle()
    game_info_q.put(game)
    update_gui(game)
    game.establish_player_attributes()
    game.deal_hole()
    game.print_round_info()
    game.act_one()
    game.print_round_info()
    if not game.round_ended:
        game.deal_flop()
        game.print_round_info()
    if not game.round_ended:
        game.ask_players()
        game.print_round_info()
    if not game.round_ended:
        game.deal_turn()
        game.print_round_info()
    if not game.round_ended:
        game.ask_players()
        game.print_round_info()
    if not game.round_ended:
        game.deal_river()
        game.print_round_info()
    if not game.round_ended:
        game.ask_players()
        game.print_round_info()
    if not game.round_ended:
        game.score_all()
        game.print_round_info()
    game.find_winners()
    game_info_q.put(game)

    # game.print_round_info()
    game.round_ended = True
    print(game.winners, game.winner, [player for player in game.list_of_players_not_out if player.win])
    game.end_round()


def run_app():
    app = App()
    app.mainloop()


def run_game_data():
    game0 = Game()
    while True:
        play(game0)


end_update = threading.Event()
t1 = threading.Thread(target=run_app)
t1.start()
t2 = threading.Thread(target=run_game_data())
t2.start()
