import pprint

def main():

    p1_pos = 10
    p2_pos = 9
    p1_score = 0
    p2_score = 0
    p1_win_sets = 0
    p2_win_sets = 0

    # histogram of universes
    # roll total key --> (position, score, count)
    p1_universes = { 0: (p1_pos, p1_score, 1) }
    p2_universes = { 0: (p2_pos, p2_score, 1) }


    iteration = 0
    while iteration < 2:

        # play player 1
        # three rolls of 3 make a result in [3..9]
        # which is 7 possible outcomes
        p1_new_universes = {}
        for k, v in p1_universes.items():
            for distance in range(3,9+1):
                new_k = k + distance

                if new_k in p1_new_universes:
                    p1_new_universes[new_k] = ( p1_new_universes[new_k][0],
                                                p1_new_universes[new_k][1],
                                                p1_new_universes[new_k][2] + 1 )
                else:
                    temp_pos = ((v[0] + distance - 1) % 10) + 1
                    temp_score = v[1] + temp_pos
                    p1_new_universes[new_k] = ( temp_pos, temp_score, 1 )

        p1_universes = p1_new_universes.copy()

        # check who wins

        # multiply all p2 counts by 3^3
        for k,v  in p1_universes.items():
            p1_universes[k] = ( p1_universes[k][0],
                                p1_universes[k][1],
                                p1_universes[k][2] * 27 )

        # play player 2

        p2_new_universes = {}
        for k, v in p2_universes.items():
            for distance in range(3,9+1):
                new_k = k + distance

                if new_k in p2_new_universes:
                    p2_new_universes[new_k] = ( p2_new_universes[new_k][0],
                                                p2_new_universes[new_k][1],
                                                p2_new_universes[new_k][2] + 1 )
                else:
                    temp_pos = ((v[0] + distance - 1) % 10) + 1
                    temp_score = v[1] + temp_pos
                    p2_new_universes[new_k] = ( temp_pos, temp_score, 1 )

        p2_universes = p2_new_universes.copy()

        # check winners

        # multiply all p1 by 3**3
        for k,v  in p1_universes.items():
            p1_universes[k] = ( p1_universes[k][0],
                                p1_universes[k][1],
                                p1_universes[k][2] * 27 )





        iteration += 1

    print("=== p1 universes")
    pprint.pprint(p1_universes)
    print("\n=== p2 universes")
    pprint.pprint(p2_universes)



if __name__ == '__main__':
    main()
