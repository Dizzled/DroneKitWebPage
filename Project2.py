#!/usr/bin/env python
#***************************************************************************************
#Project 2 Computing Minimum Coins for given change amount
#Group Members: Dustin LaGrone, Jonathan Andrew, James Stallkamp
#Date: May 5th, 2017
#Description: Cointains 4 different variations of the problem ranging from Top to Bottom
# Dynamic Programming with Memoization
# Dynamic Programming without Memoization
# Greedy 
# Brute Force Divide and Conquer 
#****************************************************************************************
import numpy
import time
import pickle
import os
import sys
from collections import Counter

#Top Down Dynamic Programming with memoization uses recursive calls to subdivide problem into smaller sections
#Input: Recieves in a loop the amount of change to be tested and the coin set to be used to calculate the problem
#Output: Returns the amount of each coin used to calculate the amount of change
def changedp(change, coins):
    
    coins_to_count = 0
    coin = {}

    if len(coins) == 1:
        coins_to_count =  change / coins[0]
        coin[coins[0]] = coins_to_count
    
    elif change == 1:
        coins_to_count = 1
        coin[coins[0]] = 1
    
    elif change == 0: 
        coins_to_count = 0
    
    else:
        if (change - coins[-1] >= 0):
            ways1 = changedp(change - coins[-1], coins) #Memoization via dictionary
            ways2= changedp(change, coins[:1])
            coins_to_count += min(1 + ways1[0], ways2[0])
            if 1 + ways1[0]<ways2[0]:
                if coins[-1] in coin:
                    coin[coins[-1]] += 1
                else:
                    coin[coins[-1]] = 1
                coin = {x: coin.get(x,0) + ways1[1].get(x,0) for x in set(coin) | set(ways1[1]) }
            else:
                coin = coin + min2[1]
                coin = {x: coin.get(x,0) + ways2[1].get(x, 0) for x in set(coin) | set(ways2[1])}
        else:
            ways = changedp(change, coins[:-1])
            coins_to_count += ways[0]
            coin = { x: coin.get(x, 0) + ways[1].get(x,0) for x in set(coin) | set(ways[1]) }
            
    return(coins_to_count, coin)

#Dynamic without memoization
#def changedp2(change, coins):

    #combinations = [0 for k in range(change + 1)]
    #combinations[0] = 1
    #for coin in coins:
     #   for x in range(1, len(combinations)):       
      #      if x >= coin:
       #         combinations[x] += combinations[x - coin]
    
   # return combinations[change]


#Greedy method selects the largest value to a given change amount 
#Input: Receives the amount of change to be tested and the values of a given coin set
#Ouput: Returns the number of coins used to calculate the given change
def changegreedy(change, coins):

    pennies = coins[0]
    nickles = coins[1]
    dimes = coins[2]
    quarter = coins[3]
    
    if len(coins) == 5:
        half_dollar = coins[4]
    else:
        half_dollar = coins[3]

    stored_coin = []
    stored_change = [change]

    if change == pennies:
     return penny
    elif change == nickles:
     return nickles
    elif change == dimes:
     return dimes
    elif change == quarter:
     return quarter

    while(0 < change):
        
        if  change >= half_dollar:
            change = (change - half_dollar)
            stored_change.append(change)
            stored_coin.append(half_dollar)

        if  quarter <= change < half_dollar:
            change = (change - quarter) #Subtract Quarter from leftover change
            stored_change.append(change) #Set the quarter to the stored coin
            stored_coin.append(quarter) #Store this in the array

        if dimes <= change < quarter: #Greater than dime less than quarter          
            change = (change - dimes) 
            stored_change.append(change)
            stored_coin.append(dimes) #Store this in the array

        if nickles <= change < dimes: #Greater than dime less than quarter     
            change = (change - nickles)
            stored_change.append(change)
            stored_coin.append(nickles) #Store this in the array
           
        if  0 < change < nickles:
            change = (change - pennies) 
            stored_change.append(change)
            stored_coin.append(pennies) #Store this in the array
          
    
    return stored_change, stored_coin

#Brute Force Method Divide and Conquer
#Input: Receives the amount of change to be calculated in a loop and the given coins to be used
#Output: This takes a very exponentially long time to calculate, but when it does will return
# the coin type used to calculate the given change (Don't recommend using this method)
def changeslow(change, coins):

    min_value = change
    
    if change in coins:   
        return [change]
    elif change == 0:
        return 0
    else:
        for x in [z for z in coins if z <= change ]:
            coin_count = [x] + changeslow(change - x, coins)
            print [x]
            print coin_count, min_value
        if (coin_count <= min_value): 
            min_value = coin_count
            
        return [min_value]
    
#Main Section Takes from a file and parses it into separate lines 
#Returns the amount of coin for the input file
#Input is run as Project2.py coin.txt and will use coin file as read input
def main():

    file =  sys.argv[1]
    path = os.getcwd()
    result_file = os.path.join(path,file[:-4] + str('change.txt'))#Assuming that the filename has .txt at the end
    result_file = open(result_file, 'w+')
    coin_to_use = []
    change_to_make = []
    
    with open(file) as f:
        count = 0   
        for line in f:
            count += 1
            line = line.split()
            if count % 2 == 0:
               line  = [int(i) for i in line]
               change_to_make.append(line)
        
        count = 1
        f.seek(0) 
        for line in f:
            count += 1
            line = line.split()
            if count % 2 == 0:
               line  = [int(i) for i in line]
               coin_to_use.append(line)

        change_to_make = numpy.asarray(change_to_make)
        coin_to_use = numpy.asarray(coin_to_use)
        stored_count = [0]
        
        #print>>result_file, "**Change Greedy**"
        #for x, val in enumerate(change_to_make):
            #coin_count, coin_type = changegreedy(val,coin_to_use[x])
            
            #print>>result_file, Counter(coin_type)
        
        #print>>result_file, "**Change Dynamic Programming With Memoization**"
        #for z, item in enumerate(change_to_make):
            #coin_count, coin_type = changedp(item,coin_to_use[z])
        
            #print>>result_file, Counter(coin_type)

        #print "**Change Dynamic Programming without Memoization**"
        #for q, stuff in enumerate(change_to_make):
           
            #coin_count = changedp2(stuff,coin_to_use[q])
            
            #print coin_count

        v1 = [1,2,6,12,24,28,60]
        v2 = [1,5,10,25,50]
        v3 = [1,6,13,37,150]

        print>>result_file, "** Change Slow Brute Force Method O(E^n)"
        for w in range(1,50):
            start_time = [0] * 50
            start_time[w] = time.time()
            coin_count = changeslow(w,coin_to_use[0])
            start_time[w] = time.time() - start_time[w]
            #coin_count = numpy.asarray(coin_count)
            
            print>>result_file, coin_count
            print>>result_file,"Runtime:%d" % start_time[w]


if __name__ == '__main__':
    main()
