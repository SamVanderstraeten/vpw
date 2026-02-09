cases = int(input())
P = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
L = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
W = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
for _ in range(cases):
    persons, locations, weapons = [int(x) for x in input().split()]
    playermap = {
        "1": { 'weapons': W[:weapons], 'locations': L[:locations], 'persons': P[:persons] },
        "2": { 'weapons': W[:weapons], 'locations': L[:locations], 'persons': P[:persons] },
        "3": { 'weapons': W[:weapons], 'locations': L[:locations], 'persons': P[:persons] },
        "4": { 'weapons': W[:weapons], 'locations': L[:locations], 'persons': P[:persons] }
    }

    questions = int(input())
    for _ in range(questions):
        player_question, combo, player_answer_input = input().split(" ")
        print(player_question, combo, player_answer_input)
        player_question = int(player_question)

        is_answered = player_answer_input != "X"
        player_answer = -1
        if is_answered:
            player_answer = int(player_answer_input)

        for pp in range(4):
            player_number = (player_question + pp + 1)
            if player_number > 4:
                if player_number % 4 == 0:
                    player_number = 4
                else:
                    player_number = player_number % 4

            if player_number == player_answer or player_number == player_question:
                break
        
            print("removing ", combo, "from player", player_number)
            playermap[str(player_number)]['weapons'] = [x for x in playermap[str(player_number)]['weapons'] if x != combo[2]]
            playermap[str(player_number)]['locations'] = [x for x in playermap[str(player_number)]['locations'] if x != combo[1]]
            playermap[str(player_number)]['persons'] = [x for x in playermap[str(player_number)]['persons'] if x != combo[0]]


        for player in range(4):
            player_number = player + 1

            if len(playermap[str(player_number)]['weapons']) == 1:
                # remove the weapon from all other players
                for pn in range(1, 5):
                    if player_number != pn:
                        playermap[str(pn)]['weapons'] = [x for x in playermap[str(pn)]['weapons'] if x != playermap[str(player_number)]['weapons'][0]]

            if len(playermap[str(player_number)]['locations']) == 1:
                # remove the location from all other players
                for pn in range(1, 5):
                    if player_number != pn:
                        playermap[str(pn)]['locations'] = [x for x in playermap[str(pn)]['locations'] if x != playermap[str(player_number)]['locations'][0]]
            
            if len(playermap[str(player_number)]['persons']) == 1:
                # remove the person from all other players
                for pn in range(1, 5):
                    if player_number != pn:
                        playermap[str(pn)]['persons'] = [x for x in playermap[str(pn)]['persons'] if x != playermap[str(player_number)]['persons'][0]]

    for player_number in range(1, 5):
        print("".join(playermap[str(player_number)]['persons']), end="")
        print("".join(playermap[str(player_number)]['locations']), end="")
        print("".join(playermap[str(player_number)]['weapons']), end="")
        print()
    break

