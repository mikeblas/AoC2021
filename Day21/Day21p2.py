import pprint

# 27 possible rolls when rolling 3d3
# key == roll total, value == probability/27
roll_curve = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


# True if there are any active (un-won) games
def any_active(universes):
    for k, v in universes.items():
        if k[1] < 21 and k[3] < 21:
            return True
    return False


def main():

    p1_pos = 6
    p2_pos = 9

    # histogram of universes
    # game state key --> count of universes
    # game state key: p1 position, p1 score; p2 position, p2 score
    # at the start, only one game exists and it is in the initial state
    universes = { (p1_pos, 0, p2_pos, 0): 1 }

    iteration = 0
    while True:

        # play player 1
        # update the universe for their rolls, skipping games already in win state
        new_universes = {}
        for k, v in universes.items():
            # if someone won this, skip it
            if k[1] >= 21 or k[3] >= 21:
                if k in new_universes:
                    new_universes[k] += v
                else:
                    new_universes[k] = v
            else:
                for distance, prob in roll_curve.items():
                    new_pos = ((k[0] + distance - 1) % 10) + 1
                    new_score = k[1] + new_pos
                    new_k = (new_pos, new_score, k[2], k[3])
                    if new_k in new_universes:
                        new_universes[new_k] += v * prob
                    else:
                        new_universes[new_k] = v * prob

        # reset back
        universes = new_universes.copy()
        if not any_active(universes):
            break

        # same for player 2
        new_universes = {}
        for k, v in universes.items():
            # if someone won this, skip it
            if k[1] >= 21 or k[3] >= 21:
                if k in new_universes:
                    new_universes[k] += v
                else:
                    new_universes[k] = v
            else:
                for distance, prob in roll_curve.items():
                    new_pos = ((k[2] + distance - 1) % 10) + 1
                    new_score = k[3] + new_pos
                    new_k = (k[0], k[1], new_pos, new_score)
                    if new_k in new_universes:
                        new_universes[new_k] += v * prob
                    else:
                        new_universes[new_k] = v * prob

        universes = new_universes.copy()
        if not any_active(universes):
            break
        iteration += 1

    print(f"iterations: {iteration}")
    print(len(universes))
    # pprint.pprint(universes)

    # 116555242726181794 too high
    p1_win_sets = 0
    p2_win_sets = 0
    for k, v in universes.items():
        if k[1] >= 21:
            p1_win_sets += v
        if k[3] >= 21:
            p2_win_sets += v
        assert k[1] != k[3]
        assert k[1] >= 21 or k[3] >= 21

    print(f"p1_win_sets = {p1_win_sets}")
    print(f"p2_win_sets = {p2_win_sets}")

if __name__ == '__main__':
    main()
