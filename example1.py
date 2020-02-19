####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
'''
team_name = 'E1'
strategy_name = 'Betray'
strategy_description = 'Always betray.'
    
def move(my_history, their_history, my_score, their_score):
    ''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    ''
    
    #This example player always betrays.      
    return 'b'
'''
'''


team_name = 'Ours'
strategy_name = 'betray if worse off'
strategy_description = 'Collude, unless we are worse than the other, and collude every tenth round'
    
def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'c'
  
  elif len(my_history) % 10 == 0:
    return 'c'
  
  elif my_score < their_score:
    return 'b'
  else:
    return 'c'

'''
'''
team_name = 'Ours'
strategy_name = 'betray if worse, collude if equal, betray once every 10 rounds'
strategy_description = 'Collude, unless we are worse than the other, then betray until we are better, and do the inverse of what should have happened every 10 rounds'


def move(my_history, their_history, my_score, their_score):
  decision = 1

  if len(my_history) == 0:
    decision = 1

  elif my_score < their_score:
    decision = 0
  
  elif len(my_history) % 10 == 0:
    if decision == 1:
      decision = 0
    else:
      decision = 1
      
  if decision == 1:
    return 'c'
  else: 
    return 'b'

'''
'''

team_name = 'Ours'
strategy_name = 'collude until they betray, then keep colluding'
strategy_description = 'Collude, until they betray, then 2 of each'



def move(my_history, their_history, my_score, their_score):
  returning = 'c'
  if len(my_history)==0:
    return 'c'
  elif my_history[-1] == 'b':
    if len(my_history) % 2 == '0':
      returning = 'b'
    else:
      returning = 'c'
    return returning
  else:
    return 'c'

'''