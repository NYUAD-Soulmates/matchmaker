from matching.games import StableRoommates

def match(pref):
    game = StableRoommates.create_from_dictionary(pref)
    return game.solve()
