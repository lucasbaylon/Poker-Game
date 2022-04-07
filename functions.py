def score_interpreter(player):
    list_of_hand_types = ["Carte haute", "Paire", "Deux paire", "Brelan", "Suite", "Couleur",
                          "Full", "Carré", "Quinte flush", "Quinte flush royale"]
    list_of_values_to_interpret = ["Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix",
                                   "Valet", "Dame", "Roi", "As"]
    hand_type = list_of_hand_types[player.score[0]]
    mod1 = list_of_values_to_interpret[player.score[1]]
    mod2 = list_of_values_to_interpret[player.score[2]]
    mod3 = list_of_values_to_interpret[player.score[3]]
    if player.score[0] == 0:
        return hand_type + ": " + mod3
    if player.score[0] == 1:
        return hand_type + ": " + mod1
    if player.score[0] == 2:
        return hand_type + ": " + mod1 + " et " + mod2
    if player.score[0] == 3:
        return hand_type + ": " + mod1
    if player.score[0] == 4:
        return hand_type + ": Hauteur " + mod1
    if player.score[0] == 5:
        return hand_type + ": Hauteur " + mod1
    if player.score[0] == 6:
        return hand_type + ": " + mod1 + " et " + mod2  # TODO La bonne écriture est (exemple) : Full au 8 par les valets quand il y a 3 huits et 2 valets
    if player.score[0] == 7:
        return hand_type + ": " + mod1
    if player.score[0] == 8:
        return hand_type + ": Hauteur " + mod1
    if player.score[0] == 9:
        return hand_type
