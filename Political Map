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

try:
    file
except:
    file = geopandas.read_file("cb_2018_us_state_5m.shp")

i = 0

for key in list_states:
    for value in list_party:
        dict[key] = value
        list_party.remove(value)
        break
    
for key in list_states:
    for value in list_edge:
        dict_edge[key] = value
        list_edge.remove(value)
        break

    
fig = plt.figure(figsize=(18,12), dpi=125)
ax = fig.add_subplot(1,1,1, projection=ccrs.Orthographic(central_longitude=-95, central_latitude=30))

ax.add_feature(cfeat.STATES.with_scale("10m"), linewidth=0.8, alpha=1, edgecolor="#55595E")

ax.add_feature(cfeat.LAND, facecolor="#C1C1C1")
ax.set_extent([-124.5,-65.5,51,21.5])


for key in dict.keys():
    file1 = file[file["STUSPS"] == key]
    ax.add_geometries(file1["geometry"], crs=ccrs.PlateCarree(), facecolor=dict[key], edgecolor=dict_edge[key], linewidth=1.4, alpha=1)
    


ax.add_feature(cfeat.COASTLINE.with_scale("10m"), edgecolor="#55595E")
ax.add_feature(cfeat.BORDERS.with_scale("10m"))
ax.add_feature(cfeat.LAKES, edgecolor="black", facecolor="#BBC7D3")
ax.add_feature(cfeat.OCEAN.with_scale("10m"), edgecolor="black", facecolor="#B8C6D0")
ax.add_feature(cfeat.LAKES,path_effects=[path_effects.SimpleLineShadow(offset=(2,-2), linewidth=5, alpha=0.40, shadow_color="#8FAADC")])


plt.show()
