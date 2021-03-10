from matching.games import StableRoommates
from matching.games import HospitalResident

def match_bi(all_prefs, bi_prefs):
    capacity = {k: 1 for k in bi_prefs}
    game = HospitalResident.create_from_dictionaries(all_prefs, bi_prefs, capacity)
    return game.solve()

def match_same(prefs):
    game = StableRoommates.create_from_dictionary(prefs)
    return game.solve()
