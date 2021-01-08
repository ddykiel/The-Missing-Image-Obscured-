import random
from Crot import Crot
from f import f

#To create graph: https://networkx.org/documentation/stable/reference/classes/digraph.html#methods

run_loop = True
run_num = 0

while run_loop:

  choices = [0, 1]

  # The Missing Pieces = the reader can control one more of these pieces after these runthroughs

  if run_num <=0:
    rand_depth = bool(random.choice(choices))
  #else user input
  
  if run_num <=1:
    rand_style = True
  #else user input

  if run_num <=2:
    rand_artist_affinity = bool(random.choice(choices))
  #else user input

  if run_num <=3:
    rand_ethan_hurts = bool(random.choice(choices))
  #else user input

  if run_num <=4:
    rand_friend_judgment = bool(random.choice(choices))
  #else user input


  run_num += 1
