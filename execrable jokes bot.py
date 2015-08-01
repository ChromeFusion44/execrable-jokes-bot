import random
import time
import sys

def tellJoke():
    #Let's tell some absolutely horrendous jokes.
    
    #I could have stored all of the jokes and punchlines in a list myself,
    #but that would be horribly messy and end up as one ludicrously long line 
    #of code. So no. I'll just append them into the jokes and punchlines
    #variables.
    

    #List of Jokes
    jokes = []
    jokes.append("Why was six afraid of seven?")
    jokes.append("How do you make a plumber sad?")
    jokes.append("When SCUBA diving, why is it important to fall backward off the side of the boat?")
    jokes.append("What do you call a shady man selling drugs?")
    jokes.append("Where was the Declaration of Independence signed?")
    jokes.append("A cat walks into a bar and orders a bowl of milk.")
    jokes.append("Why are you reading these jokes?")
    
    #List of Punchlines
    punchlines = []
    punchlines.append("It wasn't. Numbers are not sentient and thus incapable of feeling fear.")
    punchlines.append("You murder their family.")
    punchlines.append("Because if you fell forward, you would still be in the boat.")
    punchlines.append("A pharmacist.")
    punchlines.append("The bottom of the paper.")
    punchlines.append("The bartender, realizing that cats cannot talk nor do they posses higher brain functions, realizes he is hallucinating.")
    punchlines.append("Because you have no life.")
    
    #Joke Telling System
    #
    #Generate a pseudorandom number between 0 and 6
    #Use that number to print a random joke and
    #its corresponding punchline.
    #
    #The sys command is required because python
    #doesn't pause correctly without it.
    jokeNumber = random.randint(0,6)
    print jokes[jokeNumber]
    sys.stdout.flush()
    time.sleep(3)
    print punchlines[jokeNumber]