import random
from Crot import Crot
from Section import Section
import networkx as nx

#Reference on DiGraph: https://networkx.org/documentation/stable/reference/classes/digraph.html#methods

run_loop = True
run_num = 0

def createGraph(rand_depth, rand_style, rand_artist_affinity, rand_ethan_hurts, rand_friend_judgment):

  """ Creates crots and places crots into sections.
      Turns sections into a graph, using an adjacency list representation.
  """

  #Add choices as text at end of section
  # (clarify what options are being shown and why)

  title = Crot("the missing image", "The missing image")
  my_mother = Crot("My mother, my mother, my \n My mother ate me up with love.", "my mother my mother yes she ate she ate she ate me up did she say how she said she ate me up with love")

  a = Crot("Chocolate halls. Dripped ceilings. Sugar breath.", "the halls drip down saliva thick burns like oils under fingernails the ceilings press close get caught in your throat")
  b = Crot("Tour guide. Clipped, shell-slicked hair. Skull doesn't crack. She built this place—it won't hurt her. (At least, not in a way you can understand).", "the girl the girl the woman with her hair pulled back her skull doesn't crack this place won't hurt won't hurt can't hurt her you don't see with your eye wide open the lids pulled back shore lines receding dry this place can't touch her no you can't see it touch her yes")
  c = Crot("\"Welcome to my gallery,\" she says. \"Watch the steps. They're slick.\"", "the steps the steps they slide saliva sticky-slick-burns smells like sex she says to watch them watch watch watch with your eye open dried flowers blooming out from dead center")
  d = Crot("Second floor. Flows downwards. Soft ceiling. Brutal railing. Cuts.\n\"Don't eat the artwork,\" she says. \"It bites back.\"", "the floor the floor the floor flows downwards pools into ceiling blood blood blood pools and dries grown brown grows flaky grows rose petals you got in the mail turned moldy like the sun the artwork tears the artwork chews the artwork has teeth, she says, teeth teeth teeth don't be afraid they'll cut you so quick you won't even feel pain")
  e = Crot("(Even without you biting first.) The artwork gnaws. Brushstrokes like fur, hair caught in its throat.", "brushstrokes fur prickle down your throat slides down vomit the artwork has no manners the artwork touches you without permission")

  section_1_text = [a, b, c, d, e]
  section_1 = Section(section_1_text, "1")

  f_you = Crot("\"But not your mother, huh?\" Quirk. Carved into lip. Sharp tooth, gleaming smile. \"At one point in my life, that would have made me jealous. Not anymore.\"", "your mother your mother no she did not eat she did not eat she did not eat you she did not love you up with love")
  f_mother = Crot("\"Your mother, too?\" Lips tighten. Old fruity skin. Bursting. \"A friend once told me all mothers are the same. I wonder how much that's true.\"", "all mothers all mothers the same with their hands linked in a circle spinning the ritual the moon wide and liquid not dry you can't understand you're not woman girl no not the way they are you should have empathy you should know this ritual changes them know no they are not the same they feel the same but only because the center whirlpools it pulls with their water up your throat you cannot see it see see see")

  section_1_you_text = [f_you]
  section_1_mother_text = [f_mother]

  section_1_you = Section(section_1_you_text, "1ay")
  section_1_mother = Section (section_1_mother_text, "1am")

  g = Crot("Ethan. Sugar-spun hair. Butterscotch curls. Candy-slick tongue between filmed teeth.", "the boy the boy blonde hair like an angel curled not subverted innocent pink teeth with slime the animal the creature no spine no nose no mouth no ears bumpy little eyes existed before us in the caves in the soft warm dark where it ate it crawled all mouth it sucked at the walls and drew trails of slime")
  h = Crot("Drag eyes over him. No artist anymore. So be it: you're not sure she's your friend.", "the create ignores the creature keeps sucking keeps moving keeps its slime the artist the woman she left but she's no better you looked closer but the creature has no answer tells no secrets")
  i = Crot("Ethan kicks at the wall. Spins. Whistles. \"Strange place, huh?\" he says. \"I never could make sense of this artsy-fartsy stuff. \'My mother ate me up with love.\' So what? It seems a bit thin for a whole gallery, doesn't it?\"", "the wall the wall the boy the creature ethan spins and whistles a top with no gravity what a strange place strange place he says, the mother ate ate ate so what? are you afraid of a little teeth little bite little acid tearing down your skin a bit thin for a gallery doesn't it the fear recedes it pulls back from the shore it goes to rot far in the center of the ocean but maybe not for you huh")
  j = Crot("Doesn't wait. Turns again, hands buried behind head. Starts walking.", "the top spins further the gravity loosens its grip another ring out another planet far away the boy the create moving so far away spinning out from under you spinning out from your center")

  section_2_text = [g, h, i, j]
  section_2 = Section(section_2_text, "2")

  artistDangerWithEthan = Crot("Ethan curses. Broad shoulders against wall. Crack. Crumble him inside himself. \n \"Fuck!\" he says. Then turns. Dull, blinded. Sharp knives less dangerous. \"What the fuck did you say to her?\" Blunt force. Head spins. \"What the ever-locking fuck did you say to her?\"", "the boy the boy the creature crumbles falls back into himself spins faster spins a black hole yells screams spits shooting stars firesparks you stupid bastard what the fuck did you say to her what did i say what")
  artistDangerWithoutEthan = Crot("Standing in stairs. Spiral, fall. Or rise. Or stand still. \n Your head pounds. When you swallow, there's a taste of metal in your throat.", "the stairs the stairs you fall you spiral down drip-drop drip you conglomerate you smell you rot")
  artistNoDangerWithEthan = Crot("Ethan glances. Swivels his head. Still whistling. Then side-eye. Face stone house, windows closed. Movement secret, sacred. Unreachable through deep-set windows. \nSmiles broadly. Teeth dull. Wish you could read him.", "the boy the boy turns turns away the creature the creature keeps sucking the wall pays you no mind draws out the color the light the flesh turns pale the blood the blood the blood is gone the ritual the ritual what ritual lives inside the spiral the spiral the spiral of his stomach his putty intestines his pre-historic body")
  artistNoDangerWithoutEthan = Crot("Fall down stairs. Slick, almost wet. Stumble breath caught in throat. \nArtist with long dark dress, small sharp teeth. Tools held loosely in luminous hands. Silken scars knot. \"Nothing to see here,\" says she. Eyes narrow, make you small. Pointed tongue through still lips. \"You came here with a friend, didn't you? You should keep better track of them.\"", "the stairs the stairs you spiral drip-drop drip you conglomerate you smell you rot you contract you expand breath shudders out of you bones rattle bones decompose bones elasticize the woman the woman the girl the artist arrowheads in her teeth nighttime falling against her skin pale pale pale moon hands cratered veined uncooked sinewed nothing nothing to see she says why don't you believe her why does she lie when you can see her her shadow her eyes her shadow behind the moon you turn you turn you turn your face away no shadow no more your friend your friend you came here with them you held their hand your friend your friend may have fallen down with you your friend your fried clumped hair beneath your nail a morsel between your teeth your friend your friend where did they go?")

  section_2a_ade_text = [artistDangerWithEthan]
  section_2a_ade = Section(section_2a_ade_text, "2a_ade")
  section_2a_adne_text = [artistDangerWithoutEthan]
  section_2a_adne = Section(section_2a_adne_text, "2a_ad!e")
  section_2a_nade_text = [artistNoDangerWithEthan]
  section_2a_nade = Section(section_2a_nade_text, "2a_!ade")
  section_2a_nadne_text = [artistNoDangerWithoutEthan]
  section_2a_nadne = Section(section_2a_nadne_text, "2a_!ad!e")

  room = Crot("Dark room. Vibrations. You came here with your best friend and now you miss them. Walls squelch, suction. Get closer. \nPress against you. Wet soft warm. You sink through. Start to decompose.","Dark room. Vibrations. You came here with your best friend and now you miss them. Walls squelch, suction. Get closer. \nPress against you. Wet soft warm. You sink through. Start to decompose.")

  story_graph = nx.DiGraph()
  story_graph.add_edge(section_1, section_1_you)
  story_graph.add_edge(section_1, section_1_mother)

  story_graph.add_edge(section_1_you, section_2)
  story_graph.add_edge(section_1_mother, section_2)

  if rand_artist_affinity:
    story_graph.add_edge(section_1_you, section_2a_ade)
    story_graph.add_edge(section_1_mother, section_2a_nade)
    story_graph.add_edge(section_1_you, section_2a_adne)
    story_graph.add_edge(section_1_mother, section_2a_nadne)
  
  if not rand_artist_affinity:
    story_graph.add_edge(section_1_you, section_2a_nade)
    story_graph.add_edge(section_1_mother, section_2a_ade)
    story_graph.add_edge(section_1_you, section_2a_nadne)
    story_graph.add_edge(section_1_mother, section_2a_adne)

  print("Story graph complete!")

  return story_graph

def continue_on(): #Function to allow reader to continue
  input("\nPRESS ENTER  ")
  print ('\n')

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

  story_graph = createGraph(rand_depth, rand_style, rand_artist_affinity, rand_ethan_hurts, rand_friend_judgment)

  run_num += 1

  story_tree = nx.dfs_tree(story_graph)

  for s in story_tree:
    crot_list = s.crot_list
    for c in range(len(crot_list)):
      print(crot_list[c].return_random())
      continue_on()

  print("EOF reached!")

  break
