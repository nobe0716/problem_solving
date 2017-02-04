__author__ = 'sunghyo.jung'
N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()

def cal_min_diff(lists):
    min_diff_val = lists[len(lists) - 1]
    for i in range(0, N - K):
        #print "i is " + str(i) + ' ' + str(lists[i + K - 1]) + ' - ' + str(lists[i]) + ' = ' + str(lists[i + K - 1] - lists[i])
        min_diff_val = min(min_diff_val, lists[i + K - 1] - lists[i])
        #print min_diff_val
    return min_diff_val
min_diff = cal_min_diff(lists)
print min_diff