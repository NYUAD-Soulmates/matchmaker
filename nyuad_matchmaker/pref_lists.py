def pref_distance(pref_a, pref_b, weights):
    sigma = 0
    for i, (a, b) in enumerate(zip(pref_a, pref_b)):
        sigma += (a - b) ** 2 * weights[i]

    return sigma ** .5
