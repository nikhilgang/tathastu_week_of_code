player1=int(input('enter the runs scored by 1st player in 60 balls \n'))
player2=int(input('enter the runs scored by 2nd player in 60 balls \n'))
player3=int(input('enter the runs scored by 3rd player in 60 balls \n'))

strike1 = player1 * 100 / 60
strike2 = player2 * 100 / 60
strike3 = player3 * 100 / 60

six1 = int(player1 / 6)
six2 = int(player2 / 6)
six3 = int(player3 / 6)

player1*=2
player2*=2
player3*=2

print('\n\n\n strike rate of player 1 is : ', strike1)
print('\n strike rate of player 2 is : ', strike2)
print('\n strike rate of player 3 is : ', strike3)

print('\n\n\n the runs scored by player1 in 120 balls is : ', player1)
print('\n the runs scored by player1 in 120 balls is : ', player2)
print('\n the runs scored by player1 in 120 balls is : ', player3)

print('\n\n\n the maximum number of sixes hitted by player 1 is : ', six1)
print('\n the maximum number of sixes hitted by player 1 is : ', six2)
print('\n the maximum number of sixes hitted by player 1 is : ', six3)
