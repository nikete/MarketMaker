""" 

Copyright 2010 Nicolas Della Penna.

An implementaiton of Abe's and Sandholms practical liquidity sensitive market maker. A combinatorial version using cost-function based sampling."""

from numpy import array
from scipy.optimize import 
import random
form math import exp,log
from numpy import array

def b(q):
  return alpha*sum(q)

def C(q):
  """ Maps a vector of quantities to a vector of prices. In a path independent market maker the price of state i is given by the partial derivative of the cost function along i, namely"""
  foo=0
  for i in range(n):
    foo+=exp(q[i]/b(q)) 
  return b(q)*log(foo)

def quote_reward(A,Ca):
  """We create an indicator for wether each Si in S satisfies A.  So A is a function which takes an input a state and checks outputs wether or not the (1,0) the reward is payed in that state.) Then we use this and the cost function to solve for r."""
  I = []
  for Si in q.keys():
    I = A(Si)
  C(q + Ir) 
  return reward

def make_trade(state,q):
  
  return 'trade done'
  


# 20 teams, upt o 5 goals each means each game has a state of 6*6, they all play each other so there are 380 games.
n=2

#select alpha, the comision taken by the market maker, to emulate a comission that does not exceed v one sets it to = v/(n log n), so for v=0.1
alpha= 0.1/(n*log(n))

#make a generative prior for this specific market
def generative_prior():
  """ Draws a state from prior, calculates it's prior probability.
  Our prior is over the outcome of the 380 games in the premier league. We consider all outcomes with up to 5 goals for each team. We give a home team advantage of 0.37 and an average of 2.5 goals per game. Home team is the first in the pair. Everything else is iid.
  """
  home_team_advantage = 0.37
  average_goals = 2.5
  
  #pull a state from our prior
  
  l =[(average_goals/2)+home_team_advantage,(average_goals/2)-home_team_advantage]
  #Note we could have the prior take into account team handicap the teams by doing this by team and adding the handicap to the l[team]
  home_teams_goals = s = np.random.poisson( l[0], 380)
  away_teams_goals = s = np.random.poisson( l[1], 380)
  #calculate the prior probability of this state.
  teams_goals=[]
  for i in range(380):
    teams_goals.append(home_teams_goals[i])
    teams_goals.append(away_teams_goals[i])
  for i in range(380):
    if i==0:
      p= ((l[0]**teams_goals[0])*exp(-1*l[0]))/factorial(teams_goals[0])
    else:
      ((l[i%2]**teams_goals[i])*exp(-1*l[i%2]))/factorial(teams_goals[i])
  s = []
  for i in range(380):
    s.append((i,home_teams_goals[i],away_teams_goals[i]))
  return s, p

#generate a set of states acroding to the prior
nstates=0
q={}
while nstates < 10**5:
  state,prior=generative_prior()
  q[state] = prior

#lets get a quote for a bid of 1 dollar on team 1 winning game 1.


# Research question: Suppose the generative prior has some draw of team skills for the whole tournament, and then a draw using that as a mean for each game. Then rising the prob of a win on a game should make it more likely that the winer will win mroe and the looser will loose more. We could have a learner (inthis case that bids on outcomes in t based on prices in t-1) do this, but perhaps there is a beter way?


