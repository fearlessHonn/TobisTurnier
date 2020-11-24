from random import *

path = input("Dateipfad zum Beispiel eingeben: ")
text_start = open(path, "r").read()
players = text_start.split()

for p, p2 in enumerate(players):
    players[p] = int(p2)

player_num = players[0]
players.pop(0)
best_player_power = max(players)
best_player = players.index(best_player_power)
print(players)

rand = 0
rep = 1000
wins_for_best_player = 0
r = 0
print("LIGA - SYSTEM")
while r < rep:
    l1 = 0
    l2 = 0
    wins_per_player = [0] * player_num
    while l1 < len(players):
        while l2 < len(players):
            if l1 != l2:
                if players[l1] > players[l2]:
                    ratio = players[l2] / (players[l2] + players[l1])
                    rand = random()
                    if rand < ratio:
                        wins_per_player[l2] += 1
                    else:
                        wins_per_player[l1] += 1
                elif players[l2] > players[l1]:
                    ratio = players[l1] / (players[l2] + players[l1])
                    rand = random()
                    if rand < ratio:
                        wins_per_player[l1] += 1
                    else:
                        wins_per_player[l2] += 1
                elif players[l1] == players[l2]:
                    rand = random()
                    if rand < 0.5:
                        wins_per_player[l1] += 1
                    else:
                        wins_per_player[l2] += 1
            l2 += 1
        l1 += 1
        l2 = l1
    if best_player == wins_per_player.index(max(wins_per_player)):
        wins_for_best_player += 1
    r += 1
print("Der beste Spieler hat von " + str(rep) + " Spielen " + str(
    wins_for_best_player) + "-mal gewonnen! Das ist eine Rate von ca. " + str(
    round((wins_for_best_player / rep) * 100)) + " %!")

pos = 0
while pos < 3:
    if pos == 0:
        players_mod = players.copy()
        players_mod.sort()
        print("\n" + "#1 vs #2")
    if pos == 1:
        i = 0
        while i < len(players):
            players_mod[i] = players[i]
            players_mod[i + 1] = players[len(players) - i - 1]
            i += 2
        print("\n" + "#1 vs #8")
    if pos == 2:
        players_mod = players.copy()
        shuffle(players_mod)
        print("\n" + "Zufallsprinzip")

    sys = 0
    while sys < 2:
        if sys == 0:
            game_reps = 1
            print("mit einer Wiederholung:")
        if sys == 1:
            game_reps = 5
            print("mit fünf Wiederholungen:")
        wins_for_best_player = 0
        r = 0
        while r < rep:
            wins_prev = players_mod.copy()
            while len(wins_prev) > 1:
                w = 0
                while w < len(wins_prev):
                    if wins_prev[w + 1] > wins_prev[w]:
                        g = 0
                        win1 = 0
                        win2 = 0
                        while g < game_reps:
                            ratio = wins_prev[w] / (wins_prev[w] + wins_prev[w + 1])
                            rand = random()
                            if rand < ratio:
                                win1 += 1
                            else:
                                win2 += 1
                            g += 1
                        if win1 > win2:
                            wins_prev.pop(w + 1)
                        else:
                            wins_prev.pop(w)
                    elif wins_prev[w] > wins_prev[w + 1]:
                        g = 0
                        win1 = 0
                        win2 = 0
                        while g < game_reps:
                            ratio = wins_prev[w + 1] / (wins_prev[w] + wins_prev[w + 1])
                            rand = random()
                            if rand < ratio:
                                win2 += 1
                            else:
                                win1 += 1
                            g += 1
                        if win1 > win2:
                            wins_prev.pop(w + 1)
                        else:
                            wins_prev.pop(w)
                    elif wins_prev[w] == wins_prev[w + 1]:
                        g = 0
                        win1 = 0
                        win2 = 0
                        while g < game_reps:
                            rand = random()
                            if rand < 0.5:
                                win2 += 1
                            else:
                                win1 += 1
                            g += 1
                        if win1 > win2:
                            wins_prev.pop(w + 1)
                        else:
                            wins_prev.pop(w)
                    w += 1
            if best_player_power == wins_prev[0]:
                wins_for_best_player += 1
            r += 1
        print("Der beste Spieler hat von " + str(rep) + " Spielen " + str(
            wins_for_best_player) + "-mal gewonnen! Das ist eine Rate von ca. " + str(
            round((wins_for_best_player / rep) * 100)) + " %!")
        sys += 1
    pos += 1
