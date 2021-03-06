import matplotlib.pyplot as plt
import numpy as np
import random
import geopandas
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import matplotlib.patheffects as path_effects
from matplotlib.patches import Circle
import xarray as xr
import matplotlib.colors as col

#Create setting to flip text:
Flip = True
#Will print the results for each state
Developer = False

#Create list to append to map
list_1 = []
list_2 = []
list_states = []
list_party = []
list_edge = []
list_rep = []
list_dem = []
dict = {}
dict_edge = {}

class voters:
    def __init__(self, states, lean, party, delegates, population):
        self.states = states
        self.lean = lean
        self.party = party
        self.delegates = delegates
        self.population = population
        
        global Winparty
        global Wincolor
        global edge
        global VoterTurnout
        
        #Determine raw voters
        percent_turnout = np.random.uniform(0.5, 0.7)
        VoterTurnout = population * percent_turnout
        voters = np.random.randint(0, VoterTurnout)

        #Create function to print the result
        def answer():
            print(states, "Has won the vote as:", Winparty, "with", advantage, "to", disadvantage, "The Winner is:", 
                  winner, "With", delegates, "delegates")

        
            
        #Statements to include voter leans
        if lean == "extreme":
            disadvantage = 0.50 * voters
            disadvantage = int(disadvantage)
            
        if lean == "high":
            disadvantage = 0.55 * voters
            disadvantage = int(disadvantage)

        elif lean == "moderate":
            disadvantage = 0.75 * voters
            disadvantage = int(disadvantage)

        elif lean == "swing":
            disadvantage = 1.0 * voters
            
        advantage = VoterTurnout - disadvantage
        advantage = int(advantage)

         #Statements to determine the winning party
        if party == "Republican":
            if advantage > disadvantage:
                Winparty = "red"
                Wincolor = "#CB293E"
                edge = "#EF8891"
                list_1.append(advantage)
                list_2.append(disadvantage)
                list_rep.append(delegates)
                list_party.append(Wincolor)
            elif disadvantage > advantage:
                Winparty = "blue"
                Wincolor = "#3D7AD3"
                edge = "#84BDDE"
                list_1.append(disadvantage)
                list_2.append(advantage)
                list_dem.append(delegates)
                list_party.append(Wincolor)
                if Flip == True:
                    temp = disadvantage
                    disadvantage = advantage
                    advantage = temp

        if party == "Democrat":
            if advantage > disadvantage:
                Winparty = "blue"
                Wincolor = "#3D7AD3"
                edge = "#84BDDE"
                list_1.append(disadvantage)
                list_2.append(advantage)
                list_dem.append(delegates)
                list_party.append(Wincolor)
            elif disadvantage > advantage:
                Winparty = "red"
                Wincolor = "#CB293E"
                edge = "#EF8891"
                list_1.append(disadvantage)
                list_2.append(advantage)
                list_rep.append(delegates)
                list_party.append(Wincolor)
                if Flip == True:
                    temp = disadvantage
                    disadvantage = advantage
                    advantage = temp

        if Winparty == "red":
            winner = "Trump"
            if Developer == True:
                answer()
        if Winparty == "blue":
            winner = "Biden"
            if Developer == True:
                answer()

        #append data to list
        list_states.append(states)
        list_edge.append(edge)

    
AL = voters("AL", "extreme",  "Republican", 9,  4903185)    
AK = voters("AK", "extreme",  "Republican", 3,  731545)        
AZ = voters("AZ", "moderate", "Republican", 11, 7278717)    
AR = voters("AR", "extreme",  "Republican", 6,  3017825)    
CA = voters("CA", "extreme",  "Democrat",   55, 39512223)   
CO = voters("CO", "swing",    "Democrat",   9,  5758736)       
CT = voters("CT", "extreme",  "Democrat",   7,  3565287)  
DE = voters("DE", "extreme",  "Democrat",   3,  973764)  
DC = voters("DC", "extreme",  "Democrat",   3,  705749)          
FL = voters("FL", "swing",    "Republican", 29, 21477737)      
GA = voters("GA", "high",     "Republican", 16, 10617423)       
HI = voters("HI", "extreme",  "Democrat",   4,  1415872)        
ID = voters("ID", "extreme",  "Republican", 4,  1787065) 
IL = voters("IL", "extreme",  "Democrat",   20, 12671821)
IN = voters("IN", "moderate", "Republican", 11, 6732219)
IA = voters("IA", "moderate",    "Republican", 6,  3155070)
KS = voters("KS", "extreme",  "Republican", 6,  2913314)
KY = voters("KY", "high",     "Republican", 8,  4467673) 
LA = voters("LA", "extreme",  "Republican", 8,  4648794)
ME = voters("ME", "high",     "Democrat",   4,  1344212)
MD = voters("MD", "extreme",  "Democrat",   10, 6045680)
MA = voters("MA", "extreme",  "Democrat",   11, 6949503)
MI = voters("MI", "swing",    "Democrat",   16, 12671821)       
MN = voters("MN", "moderate", "Democrat",   10, 6732219)    
MS = voters("MS", "extreme",  "Republican", 6,  3155070)    
MO = voters("MO", "moderate", "Republican", 10, 2913314)      
MT = voters("MT", "extreme",  "Republican", 3,  4467673)        
NE = voters("NE", "extreme",  "Republican", 5,  4648794)     
NV = voters("NV", "swing",    "Democrat",   6,  1344212)       
NH = voters("NH", "moderate", "Democrat",   4,  6045680) 
NJ = voters("NJ", "extreme",  "Democrat",   14, 6949503)    
NM = voters("NM", "moderate", "Democrat",   5,  9986857)    
NY = voters("NY", "extreme",  "Democrat",   29, 5639632)    
NC = voters("NC", "swing",    "Republican", 15, 2976149) 
ND = voters("ND", "extreme",  "Republican", 3,  6137428)  
OH = voters("OH", "moderate", "Republican", 18, 1068778)         
OK = voters("OK", "extreme",  "Republican", 7,  1934408)      
OR = voters("OR", "extreme",  "Democrat",   7,  3080156)        
PA = voters("PA", "swing",    "Democrat",   20, 1359711)  
RI = voters("RI", "extreme",  "Democrat",   4,  8882190)  
SC = voters("SC", "extreme",  "Republican", 9,  2096829) 
SD = voters("SD", "extreme",  "Republican", 3,  19453561)   
TN = voters("TN", "extreme",  "Republican", 11, 10488084)     
TX = voters("TX", "high",     "Republican", 38, 762062)     
UT = voters("UT", "extreme",  "Republican", 6,  3205958)           
VT = voters("VT", "extreme",  "Democrat",   3,  623989)        
VA = voters("VA", "swing",    "Democrat",   13, 8535519)      
WA = voters("WA", "extreme",  "Democrat",   12, 7614893)     
WV = voters("WV", "extreme",  "Republican", 5,  1792147) 
WI = voters("WI", "swing",    "Democrat",   10, 5822434)    
WY = voters("WY", "extreme",  "Republican", 3,  578759)  
print(len(list_dem))

print("Republican Delegates: ", sum(list_rep))
print("Democrat Delegates: ", sum(list_dem))

num = 45

vote_country_set = True
vote_states_set = False



def vote_country():
    total_voters = sum(list_1) + sum(list_2)
    Rep_votes = sum(list_1) / total_voters *100
    Dem_votes = sum(list_2) / total_voters *100
    Rep_votes = str(round(Rep_votes, 2)) + "%"
    Dem_votes = str(round(Dem_votes, 2)) + "%"
    print("Republican Gets:", Rep_votes, "Democrat Gets:", Dem_votes)
    plot("United States", sum(list_1), sum(list_2))

    
def vote_states():
    total_voters = list_1[num] + list_2[num]
    Rep_votes = list_1[num] / total_voters *100
    Dem_votes = list_2[num] / total_voters *100
    Rep_votes = str(round(Rep_votes, 2)) + "%"
    Dem_votes = str(round(Dem_votes, 2)) + "%"
    print("Republican Gets:", Rep_votes, "Democrat Gets:", Dem_votes)
    plot(list_states[num], list_1[num], list_2[num])


if vote_country_set == True:
    vote_country()
    
if vote_states_set == True:
    vote_states()
    
    
def plot(state, bar1, bar2):
    ind = np.arange(2) + 1
    fig = plt.figure(figsize=(8,10))
    fig.add_subplot(1,1,1)
    rect1 = plt.bar(1, bar1, color="red")
    rect2 = plt.bar(2, bar2, color="blue")
    plt.xticks(ind,("Republican", "Democrat"))
    plt.ticklabel_format(style='plain', axis='y')
    plt.title("Popular Vote")
    plt.xlabel(state)

plt.show()
