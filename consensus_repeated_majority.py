# -*- coding: utf-8 -*-
"""
Created on Sun June 02 18:05:49 2019

This program implements the repeated majority protocol for distributed computing (population protocol model).
There are n nodes, each having an initial belief (a bit in {0, 1}). The goal is that after running some 
distributed protocol each node has the correct initial belief with high probability. Relevant parameters are 
the amount of memory that each node has, the time to consensus, the amount of communication used.

System dynamics: each node keeps track of a state which is either 0, 1, or ?. 
Initially each node has state 0 or 1. In each round, a node gets selected uniformly at random and 
is matched with a random other node. The nodes that get matched exchange state and update their own state 
based on this communication. The repeated majority protocol works as follows:

  Let U, V, and S represent, respectively, the set of nodes storing 0, 1, and ?
    --> If a  node in U (resp. V) contacts a node in U, S (resp. V, S), then it does not update its value. 
    --> If a node in U (resp. V) contacts a node in V (resp. U), it updates its value to ? (resp. ?).  
    --> If a  node in S contacts a node in U (resp. V), then it updates it’s value to 1 (resp. 0).
"""
import random
import numpy
import math
import matplotlib.pyplot as plt

qval = 5

# simulate one round of the process, in which two random nodes get matched; 
# we work here with milan's version, where the initiator updates state 
# the input parameters are:
# n = number of nodes, t = time unit, b = belief vector, correct/wrong/q are vectors with the number of nodes that 
# are 1 (correct), 0 (wrong), and q (?) throughout time 
def simulate_round(n, t, b, correct, wrong):
    i = random.randint(0, n-1) # node that communicates in this round. This node will get matched with a random other node
    
    jj = random.randint(0, n-2)
    
    if jj < i: # we have to fix a bit the index of the node that i contacts possibly
        j = jj
    else:
        j = jj + 1

    # the pair (i,j) talks now, with i being the initiator
    if (b[i] == 0 and b[j] == 1):
        b[i] = qval
        wrong[t] = wrong[t] - 1
    elif (b[i] == 1 and b[j] == 0):
        b[i] = qval
        correct[t] = correct[t] - 1
    elif (b[i] == qval):
        b[i] = b[j]
        if b[j] == 1:
            correct[t] = correct[t] + 1
        elif b[j] == 0:
            wrong[t] = wrong[t] + 1
        
    return [b, correct, wrong]

# simulate the system dynamics
def sim(n, c, T, correct, wrong):
    
    total_time = 0 
                
    b = [1 for e in range(n)] # b[i] is the initial belief bit of node i
    
    z = math.ceil(c * n)
    for i in range(z):
        b[i] = 0 # the nodes from 0 to z are in the minority and have the wrong bit
    
    correct[0] = n - z # number of nodes with majority opinion (initially)
    wrong[0] = z # number of nodes with minority opinion
    
    t = 1 # round number 
    while (t < T): # while did not run until the max number of allowed rounds and there are beliefs different from 1 (i.e. the correct bit)
        
        correct[t] = correct[t-1]
        wrong[t] = wrong[t-1]
        
        [b, correct, wrong] = simulate_round(n, t, b, correct, wrong)
        
        if (correct[t] == n):
            print("Reached consensus at time", t)
            return [correct, wrong, t]

        t = t + 1
            
    return [correct, wrong, t]
                        
def main():
    n = 0 # simulating a system with 5000 nodes; this can be changed
    
    N_Default = 1000
        
    try:
        n_user = input("Enter the number of nodes (default: 1000):")
        n = int(n_user)
    except ValueError:
        print("Using default n =", N_Default)
        n = N_Default
    
    c = 0 # initial minority fraction; should be a number in [0, 1/2)
    
    try:
        c_user = input("Enter the initial minority fraction (default: 0.333)")
        c = float(c_user)
    except ValueError:
        print("Using default minority fraction = 1/3")
        c = 1/3 
    
    T = 10 * n * math.ceil(math.log(n)) # number of rounds for simulating the system dynamics
    
    correct = [0 for i in range(T)]  # correct[t] contains the fraction of correct nodes at time t 
    wrong = [0 for i in range(T)] # wrong[t] contains the fractions of wrong nodes at time t
    q = [0 for i in range(T)] # q[t] contains the fraction of ? nodes at time t
    
    time = 0 # keep track of the exact time it takes to run the simulation
    
    [correct, wrong, time] = sim(n, c, T, correct, wrong)
                
    q = [0 for e in range(time)]
    
    for t in range(time):
        correct[t] = correct[t] / n
        wrong[t] = wrong[t] / n
        q[t] = (n - correct[t] - wrong[t]) / n
        
    print("Showing the fraction of correct, incorrect, and ? nodes over time")
    
    plt.figure(0)
    plt.ylabel("Fraction of correct nodes")
    plt.xlabel("Time")
    plt.plot(correct[0:time], color='blue')
    
    plt.figure(1)
    plt.ylabel("Fraction of wrong nodes")
    plt.xlabel("Time")
    plt.plot(wrong[0:time], color='red')
    
    plt.figure(2)
    plt.ylabel("Fraction of question marks")
    plt.xlabel("Time")

    plt.plot(q[0:time], color = 'orange')
        
    plt.show()   
    
main()
    
