N, M = map(int,input().split())

AB = [list(map(int,input().split())) for _ in range(M)]

result = [["-" for _ in range(N)] for _ in range(N)] #試合の結果表



for game in AB:
    winner_index = game[0] - 1
    loser_index  = game[1] - 1

    result[winner_index][loser_index] = "o"
    result[loser_index][winner_index] = "x"

for row in result:
    print(*row)