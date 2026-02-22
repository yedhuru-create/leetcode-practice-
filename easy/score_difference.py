nums = [4, 1, 7, 3, 2]

nums.sort(reverse=True)

player1 = sum(nums[::2])
player2 = sum(nums[1::2])

print(abs(player1 - player2))
