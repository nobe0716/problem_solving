from collections import defaultdict


def solve(n, name_scores):
    name_to_score_history = defaultdict(list)

    for i in range(len(name_scores)):
        name, score = name_scores[i]
        if len(name_to_score_history[name]) == 0:
            name_to_score_history[name].append((score, i))
        else:
            name_to_score_history[name].append((name_to_score_history[name][-1][0] + score, i))

    max_score = float('-inf')
    candidates = set()

    for name, history in name_to_score_history.items():
        score = history[-1][0]
        if score > max_score:
            max_score = score
            candidates = {name}
        elif score == max_score:
            candidates.add(name)

    earliest_turn = float('inf')
    winner = None
    for name in candidates:
        history = name_to_score_history[name]
        for i in range(len(history)):
            if history[i][0] >= max_score:
                if earliest_turn > history[i][1]:
                    earliest_turn = history[i][1]
                    winner = name

                    # print(earliest_turn, name)
    # print(winner)
    return winner


assert solve(3, [['mike', 3], ['andrew', 5], ['mike', 2]]) == 'andrew'
assert solve(3, [['mike', 3], ['andrew', 5], ['mike', 2]]) == 'andrew'
assert solve(15,
             [['aawtvezfntstrcpgbzjbf', 681],
              ['zhahpvqiptvksnbjkdvmknb', -74],
              ['aawtvezfntstrcpgbzjbf', 661],
              ['jpdwmyke', 474],
              ['aawtvezfntstrcpgbzjbf', -547],
              ['aawtvezfntstrcpgbzjbf', 600],
              ['zhahpvqiptvksnbjkdvmknb', -11],
              ['jpdwmyke', 711],
              ['bjmj', 652],
              ['aawtvezfntstrcpgbzjbf', -1000],
              ['aawtvezfntstrcpgbzjbf', -171],
              ['bjmj', -302],
              ['aawtvezfntstrcpgbzjbf', 961],
              ['zhahpvqiptvksnbjkdvmknb', 848],
              ['bjmj', -735]]) == 'aawtvezfntstrcpgbzjbf'

n = int(input())
name_scores = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    name_scores.append((name, score))

res = solve(n, name_scores)
print(res)
