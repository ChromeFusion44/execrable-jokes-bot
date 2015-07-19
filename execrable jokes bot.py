import random
import time

def tellJoke():
    #Let's tell some absolutely horrendous jokes
    #jokes = {'jack': 4098, 'sape': 4139}
    
    #List of Jokes 
    joke0x0 = "Why was six afraid of seven?"
    joke0x1 = "It wasn't. Numbers are not sentient and thus incapable of feeling fear."
    
    joke1x0 = "How do you make a plumber sad?"
    joke1x1 = "You murder their family."
    
    joke2x0 = "When SCUBA diving, why is it important to fall backward off the side of the boat?"
    joke2x1 = "Because if you fell forward, you would still be in the boat."
    
    joke3x0 = "What do you call a shady guy selling drugs?"
    joke3x1 = "A pharmacist."
    
    joke4x0 = "Where was the Declaration of Independence signed?"
    joke4x1 = "The bottom of the paper."
    
    joke5x0 = "A cat walks into a bar and orders a bowl of milk."
    joke5x1 = "The bartender, realizing that cats cannot talk nor do they posses higher brain functions, realizes he must be dreaming."
    
    joke6x0 = "Why are you reading these jokes?"
    joke6x1 = "Because you have no life."
    
    joke7x0 = ""
    joke7x1 = ""
    
    
    #Joke Telling System
    jokeNum = str(random.randint(0, 6))    
    jokeToTell1 = "joke"+jokeNum+"x1"
    jokeToTell2 = "joke"+jokeNum+"x2"
    
    print jokeToTell1
    time.sleep(2)
    print jokeToTell2