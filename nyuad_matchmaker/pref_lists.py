def filter_users(responses, user, users):
    res = []
    user_data = responses[user]
    for cand in users:
        cand_data = responses[cand]
        if (user != cand
                and user_data.gender in cand_data.pref
                and cand_data.gender in user_data.pref):
            res.append(cand)
    return res

def gen_weights(weights):
    return weights

def pref_distance(pref_a, pref_b, weights):
    sigma = 0
    for i, (a, b) in enumerate(zip(pref_a, pref_b)):
        sigma += (a - b) ** 2 * weights[i]
    return sigma ** .5

def get_prefs(responses, user, w):
    return lambda cand: pref_distance(user.res, cand.res, w)

def sort_prefs(responses, user, users, w):
    return sorted(users, reverse=True, key=get_prefs(responses, user, w))

def gen_preflists(responses, weights):
    res = {}
    users = responses.keys()
    for user in responses:
        filtered = filter_users(responses, user, users)
        w = gen_weights(weights)
        res[user] = sort_prefs(responses, user, filtered, w)
    return res
