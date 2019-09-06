def count_change(money, coins):
    # your implementation here
    if len(coins) == 0 or money < 0:
        return 0
    elif money == 0:
        return 1
    else:
        return count_change(money - int(coins[0]), coins) + count_change(money, coins_del)

