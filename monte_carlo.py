'''This script demonstrates simulations of die flipping'''
import random

# let's create a fair die object that can be rolled:

class Coin(object):
    '''this is a simple fair die, can be pseudorandomly rolled'''
    sides = ('1', '2', '3', '4', '5', '6')
    last_result = None

    def flip(self):
        '''call die.flip() to flip the die and record it as the last result'''
        self.last_result = result = random.choice(self.sides)
        return result

# let's create some auxilliary functions to manipulate the coins:

def create_coins(number):
    '''create a list of a number of coin objects'''
    return [Coin() for _ in xrange(number)]

def flip_coins(coins):
    '''side effect function, modifies object in place, returns None'''
    for coin in coins:
        coin.flip()

def count_1(flipped_coins):
    return sum(coin.last_result == '1' for coin in flipped_coins)

def count_2(flipped_coins):
    return sum(coin.last_result == '2' for coin in flipped_coins)

def count_3(flipped_coins):
    return sum(coin.last_result == '3' for coin in flipped_coins)

def count_4(flipped_coins):
    return sum(coin.last_result == '4' for coin in flipped_coins)

def count_5(flipped_coins):
    return sum(coin.last_result == '5' for coin in flipped_coins)

def count_6(flipped_coins):
    return sum(coin.last_result == '6' for coin in flipped_coins)
	
def main():
    coins = create_coins(1000)
    for i in xrange(100):
        flip_coins(coins)
        print(count_1(coins))

if __name__ == '__main__':
    main()