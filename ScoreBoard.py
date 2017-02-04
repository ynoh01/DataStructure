# CS241 Project1
# Score class will be used to create objects that track several aspects (score,
# level, lives,multiplier) of a player’s performance during an arcade-style game.
# Scoreboard class will maintain (as long as the program is running) a 
# leaderboard of high scores sorted in decreasing order. 




class Score:

  def __init__(self, player_name):
    # The required attributes
    self._player_name = player_name
    self._current_score = 0
    self._current_level = 0
    self._current_multiplier = 1
    self._lives_remaining = 3



  # The required methods
  def add_points(self, amount):
    # implement this method by adding the number of points
    # specified by amount times the currentMultiplier value
    # to the currentScore. If the new score value should
    # result in the level changing, then change currentLevel.
    # return the new value of currentScore.
    if amount < 0:
      return
    
    if amount % 1 != 0 :
      return
    
    self._current_score = self._current_score + amount * self._current_multiplier
    upperbound = (2 ** self._current_level) * 10000 - 1 
    
    while self._current_score > upperbound:
      self._current_level = self._current_level + 1
      upperbound = (2 ** self._current_level) * 10000 - 1 
    
    return self._current_score
  
  
  
  def subtract_points(self, amount):
    # reset currentMultipler to 1. subtract the number of
    # points specified by amount from currentScore, and update
    # currentLevel if necessary.
    # return the new value of currentScore.
    if amount < 0:
      return
    
    if amount % 1 != 0:
      return
    
    self._current_multiplier = 1
    self._current_score = self._current_score - amount
    lowerbound = 2 ** (self._current_level-1) * 10000
    
    if self._current_score < 0:
      self._current_score = 0
      
    while self._current_score < lowerbound and self._current_level > 0:
      self._current_level = self._current_level - 1    
      lowerbound = 2 ** (self._current_level-1)*10000    
      
    return self._current_score
  
  
  
  def get_player_name(self):
    # return the name of the player associated with this object.
    return self._player_name



  def get_multiplier(self):
    # return the current value of the multiplier attribute.
    return self._current_multiplier



  def increment_multiplier(self):
    # increase the value of currentMultiplier by one.
    # return the new value of currentMultiplier.
    self._current_multiplier = self._current_multiplier + 1
    return self._current_multiplier 
    


  def get_score(self):
    # return the current value of the score attribute.
    return self._current_score



  def get_level(self):
    # return the current value of the level attribute.
    return self._current_level



  def get_lives(self):
    # return the number of lives remaining.    
    return self._lives_remaining
  
  
  
  def lose_life(self):
    # decrement the number of lives remaining. If, after you
    # have decremented the lives attributes, that attribute
    # has a positive value, return True, indicating play can
    # continue. If the number is zero, return false,
    # indicating that the game is over.
    self._lives_remaining = self._lives_remaining - 1
    
    if self._lives_remaining > 0:
      return True
   
    else:
      self._lives_remaining = 0
      return False
    
    
    
  def gain_life(self):
    # increase the current value of the lives attribute
    # by one.
    self._lives_remaining = self._lives_remaining + 1



  def __str__(self):
    return self._player_name + ' SCORE: ' + str(self._current_score) +\
        ' LVL: '+ str(self._current_level) +\
        ' MULT: ' + str(self._current_multiplier) +\
        ' LIVES: ' + str(self._lives_remaining)
  
  
  
class Scoreboard:

  def __init__(self, capacity):
    self._high_scores = [None] * capacity
    self._entries = 0



  def update(self, candidate_score):
    # if candidate_score has a score value higher than the
    # lowest score in the Scoreboard, add it at the correct position.   
    score = candidate_score.get_score()  
    good = self._entries < len(self._high_scores) or score > self._high_scores[-1].get_score() 
    
    if good: 
      
      if self._entries < len(self._high_scores):
        self._entries += 1
        
      j = self._entries - 1
      
      while j > 0 and self._high_scores[j-1].get_score() < score:
            self._high_scores[j] = self._high_scores[j-1]
            j -= 1
            
      self._high_scores[j] = candidate_score        
  



  def print_scoreboard(self):
    # take advantage of the fact that the Score object implements
    # the __str__() method, and can therefore be passed directly to
    # print(). Use this to print the current score board.    
    for i in range(0,self._entries):
      print (self._high_scores[i])
      
    
   
   


if __name__ == '__main__':
    # your test code goes here
    # Create multiple Score objects, 
    # Test the methods thoroughly.
    # Be careful not to make assumptions
    # about how the methods behave or what
    # order things happen in.
    # Finally, create a Scoreboard instance and
    # add your score objects to it, printing it 
    # each time to ensure that they are ordered
    # correctly.
     
    bob = Score("bob")
    alice = Score("alice")
    sue = Score("sue")
    
    # Does it add the number of points correctly?
    test1 = Score.add_points(bob,500)
    print("Expected: 500 Actual:" + str(test1))
    
    # Does it subtract the number of points correctly?
    test2 = Score.subtract_points(bob,100)
    print("Expected: 400 Actual:" + str(test2))
    
    # Does it get values correctly?
    # (Player name, multiplier, level, score,lives)
    test3 = Score.get_player_name(bob)
    print("Expected: bob Actual:" + str(test3))
    
    test4 = Score.get_multiplier(bob)
    print("Expected: 1 Actual:" + str(test4))
    
    test5 = Score.get_level(bob)
    print("Expected: 0 Actual:" + str(test5))
    
    test6 = Score.get_score(bob)
    print("Expected: 400 Actual:" + str(test6))
    
    test7 = Score.get_lives(bob)
    print("Expected: 3 Actual:" + str(test7))
    
    # Does it increase multiplier correctly
    test8 = Score.increment_multiplier(bob)
    print("Expected: 2 Actual:" + str(test8))
    
    # when subtract function is called, does it set multiplier as 1?
    Score.subtract_points(bob,100)
    test9 = Score.get_multiplier(bob)
    print("Expected: 1 Actual:" + str(test9))
    
    # Does it decrement lives correctly
    Score.lose_life(bob)
    test10 = Score.get_lives(bob)
    print("Expected: 2 Actual:" + str(test10))
    
     # Does it increment lives correctly
    Score.gain_life(bob)
    test11 = Score.get_lives(bob)
    print("Expected: 3 Actual:" + str(test11))
    
    # Does it return false when remaining lives is zero
    Score.lose_life(bob)
    Score.lose_life(bob)
    test12 = Score.lose_life(bob)
    print("Expected: False Actual:" + str(test12))
     
    # Does it take care of bad input? Adding non-integer
    Score.add_points(bob,1.5)
    test13 = Score.get_score(bob)
    print("Expected: 300 Actual:" + str(test13))
     
    # Does it take care of bad input? Subtracting non-integer
    Score.subtract_points(bob,1.5)
    test14 = Score.get_score(bob)
    print("Expected: 300 Actual:" + str(test14))    
      
    # Does it taking care of a bad input? Subtract negative amount
    Score.subtract_points(bob,-40000)
    test15 = Score.get_score(bob)
    print("Expected: 300 Actual:" + str(test15))    
        
    # Does it taking care of bad input? Add negative amount
    Score.add_points(bob,-40000)
    test16 = Score.get_score(bob)
    print("Expected: 300 Actual:" + str(test16))  
     
    # Does it take care of more than one level changes? (Add)
    Score.add_points(bob,50000)
    test17 = Score.get_level(bob)
    print("Expected: 3 Actual:" + str(test17)) 
    
    # Does it take care of more than one level changes? (Subtract)
    Score.subtract_points(bob,50000)
    test18 = Score.get_level(bob)
    print("Expected: 0 Actual:" + str(test18)) 
    
    # Check the score on the edge 
    
    # add to the upperbound
    Score.add_points(bob,39699)
    test19 = Score.get_level(bob)
    print("Expected: 2 Actual:" + str(test19))
    
    #subtract to the lowerbound
    Score.subtract_points(bob,29999)
    test20 = Score.get_level(bob)
    print("Expected: 1 Actual:" + str(test20))
    
    # add to the lowerbound
    Score.add_points(bob,10000)
    test21 = Score.get_level(bob)
    print("Expected: 2 Actual:" + str(test21))
    
    # subtract to the upperbound
    Score.subtract_points(bob,10000)
    test22 = Score.get_level(bob)
    print("Expected: 1 Actual:" + str(test22))  
    
    # when the score becomes negative, does it set the score and level as 0?
    Score.subtract_points(bob,20000)
    test23 = Score.get_score(bob)
    print("Expected: 0 Actual:" + str(test23)) 
    
    test24 = Score.get_level(bob)
    print("Expected: 0 Actual:" + str(test24))
    
    # Does it taking care of the case when there is less than 10 players
    # in total? 
    # Test25   
    sb = Scoreboard(10)
    Score.add_points(alice,12345)
    Score.add_points(sue,333334)    
    sb.update(bob)       
    sb.update(alice)       
    sb.update(sue)
    print('')          
    print('''Expected: 
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3 
alice SCORE: 12345 LVL: 1 MULT: 1 LIVES: 3  
bob SCORE: 0 LVL: 0 MULT: 1 LIVES: 0''')
    print('')
    print('''Actual:''') 
    sb.print_scoreboard()
    
    # Does the scoreboard update top 10 scores correctly? 
    # Test26
    james = Score("james")
    john = Score("john")
    bill = Score("bill")
    susan = Score("susan")
    rob = Score("rob")
    patrick = Score("patrick")
    jim = Score("jim")
    Score.add_points(james,40000)
    Score.add_points(john,30000)
    Score.add_points(bill,20000)
    Score.add_points(susan,50000)
    Score.add_points(rob,60000)
    Score.add_points(patrick,70000)
    Score.add_points(jim,80000)    
    sb.update(james)
    sb.update(john)
    sb.update(bill)
    sb.update(susan)
    sb.update(rob)
    sb.update(patrick)   
    sb.update(jim)  
    print('')
    print('''Expected:
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3
rob SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
susan SCORE: 50000 LVL: 3 MULT: 1 LIVES: 3
james SCORE: 40000 LVL: 3 MULT: 1 LIVES: 3
john SCORE: 30000 LVL: 2 MULT: 1 LIVES: 3
bill SCORE: 20000 LVL: 2 MULT: 1 LIVES: 3
alice SCORE: 12345 LVL: 1 MULT: 1 LIVES: 3
bob SCORE: 0 LVL: 0 MULT: 1 LIVES: 0''')
    print('')    
    # assume this as the original scoreboard to test different cases below 
    print('''Actual:''')
    print("Original Scoreboard")
    sb.print_scoreboard()
    
    # when the new highest score is added 
    # Test27
    kate = Score("kate")
    Score.add_points(kate,333335)
    sb.update(kate)
    print('')
    print('''Expected:
kate SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3
rob SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
susan SCORE: 50000 LVL: 3 MULT: 1 LIVES: 3
james SCORE: 40000 LVL: 3 MULT: 1 LIVES: 3
john SCORE: 30000 LVL: 2 MULT: 1 LIVES: 3
bill SCORE: 20000 LVL: 2 MULT: 1 LIVES: 3
alice SCORE: 12345 LVL: 1 MULT: 1 LIVES: 3''') 
    print("")
    print("Actual:")
    sb.print_scoreboard()
    
    # when the new highest score is equal to the original highest score
    # since the new highest score does not beat the original score, it should 
    # be added below the original highest score. 
    # Test28
    jenny = Score("jenny")
    Score.add_points(jenny,333335)
    sb.update(jenny)
    print("")
    print('''Expected:
kate SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
jenny SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3
rob SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
susan SCORE: 50000 LVL: 3 MULT: 1 LIVES: 3
james SCORE: 40000 LVL: 3 MULT: 1 LIVES: 3
john SCORE: 30000 LVL: 2 MULT: 1 LIVES: 3
bill SCORE: 20000 LVL: 2 MULT: 1 LIVES: 3''')
    print("")
    print("Actual:")
    sb.print_scoreboard()  
    
    # when the new score is added on the bottom of the score board 
    # Test29
    benny = Score("benny")
    Score.add_points(benny,20001)
    sb.update(benny)
    print("")
    print('''Expected:
kate SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
jenny SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3
rob SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
susan SCORE: 50000 LVL: 3 MULT: 1 LIVES: 3
james SCORE: 40000 LVL: 3 MULT: 1 LIVES: 3
john SCORE: 30000 LVL: 2 MULT: 1 LIVES: 3
benny SCORE: 20001 LVL: 2 MULT: 1 LIVES: 3''')   
    print("")
    print("Actual:")
    sb.print_scoreboard()     
    
    # when the new 10th score is equal to the original 10th score
    # the new score should not be shown in the scoreboard 
    # Test30
    sarah = Score("sarah")
    Score.add_points(sarah,20001)
    sb.update(sarah)
    print("")
    print('''Expected: 
kate SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
jenny SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3
rob SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
susan SCORE: 50000 LVL: 3 MULT: 1 LIVES: 3
james SCORE: 40000 LVL: 3 MULT: 1 LIVES: 3
john SCORE: 30000 LVL: 2 MULT: 1 LIVES: 3
benny SCORE: 20001 LVL: 2 MULT: 1 LIVES: 3''')
    print("")
    print("Actual")
    sb.print_scoreboard()    
    
    # when the new score is added in the middle of the scoreboard 
    # this data should be added 6th from the top, and remove the 10th score
    # from the scoreboard
    # Test31
    ben = Score("ben")
    Score.add_points(ben,60001)
    sb.update(ben)
    print("")
    print('''Expected:
kate SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
jenny SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3
ben SCORE: 60001 LVL: 3 MULT: 1 LIVES: 3
rob SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
susan SCORE: 50000 LVL: 3 MULT: 1 LIVES: 3
james SCORE: 40000 LVL: 3 MULT: 1 LIVES: 3
john SCORE: 30000 LVL: 2 MULT: 1 LIVES: 3''')
    print("")
    print("Actual")
    sb.print_scoreboard()  
    
    # capacity controls the number of players (and its following data)
    # displayed in the scoreboard. 
    # Set capacity = 20. Scoreboard can display up to 20 players. 
    # Test 32
    
    SB = Scoreboard(15)
    SB.update(sarah)
    SB.update(kate)
    SB.update(james)
    SB.update(jenny)  
    SB.update(john)
    SB.update(bill) 
    SB.update(susan)
    SB.update(rob)
    SB.update(patrick)  
    SB.update(jim) 
    SB.update(ben)
    SB.update(benny)
    SB.update(bob)
    SB.update(alice)
    SB.update(sue)
    print("")
    print('''Expected:
kate SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
jenny SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3
ben SCORE: 60001 LVL: 3 MULT: 1 LIVES: 3
rob SCORE: 60000 LVL: 3 MULT: 1 LIVES: 3
susan SCORE: 50000 LVL: 3 MULT: 1 LIVES: 3
james SCORE: 40000 LVL: 3 MULT: 1 LIVES: 3
john SCORE: 30000 LVL: 2 MULT: 1 LIVES: 3
sarah SCORE: 20001 LVL: 2 MULT: 1 LIVES: 3
benny SCORE: 20001 LVL: 2 MULT: 1 LIVES: 3
bill SCORE: 20000 LVL: 2 MULT: 1 LIVES: 3
alice SCORE: 12345 LVL: 1 MULT: 1 LIVES: 3
bob SCORE: 0 LVL: 0 MULT: 1 LIVES: 0''')
    print("")
    print("Actual")
    SB.print_scoreboard()
    
    # Set capacity =5 to display only 5 players. 
    # Test 33
    board = Scoreboard(5)
    board.update(sarah)
    board.update(kate)
    board.update(james)
    board.update(jenny)  
    board.update(john)
    board.update(bill) 
    board.update(susan)
    board.update(rob)
    board.update(patrick)  
    board.update(jim) 
    board.update(ben)
    board.update(benny)
    board.update(bob)
    board.update(alice)
    board.update(sue)
    print("")
    print('''Expected:
kate SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
jenny SCORE: 333335 LVL: 6 MULT: 1 LIVES: 3
sue SCORE: 333334 LVL: 6 MULT: 1 LIVES: 3
jim SCORE: 80000 LVL: 4 MULT: 1 LIVES: 3
patrick SCORE: 70000 LVL: 3 MULT: 1 LIVES: 3''')
    print("")
    print("Actual")
    board.print_scoreboard()
    
    
  
    
   
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    
   
    

    
    
