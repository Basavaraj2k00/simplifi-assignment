def gi_hun():
    t = int(input())  # number of test cases
    output = []
    for i in range(t):
        n, k = map(int, input().split())  # number of players and their height
        heights = list(map(int, input().split()))  # heights of the players
        min_shots = 0  # minimum number of players who need to get shot
        
        max_height = k  # initialize the maximum height seen so far

        for height in heights:
            if height > max_height:  # if the player is taller than the previous tallest
                max_height = height  # update the tallest player
                min_shots += 1  # one more player needs to get shot

        output.append(min_shots)  # output the result for this test case
    return output

result = gi_hun()

print("Output here: \n")
for i in result:
    print(i)
