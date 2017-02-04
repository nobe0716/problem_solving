__author__ = 'sunghyo.jung'

# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
    #Compute and return final answer over here
    answer = 0
    prices = sorted(prices)
    while rupees > prices[0]:
        rupees -= prices[0]
        answer += 1
        prices.pop(0)
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)

