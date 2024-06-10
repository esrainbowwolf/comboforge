import os
import pandas as pd
import numpy as np
from operator import itemgetter

# Loading the data
KeyforgeCards = pd.read_csv(
    "C:/Users/video/Desktop/Coding fun/MyWebsites/comboforge/src/DataBase/dok-cards-2023-08-25.csv"
)
# Setting first itteration of the tables
KeyforgeCardsFixed = KeyforgeCards.where(pd.notnull(KeyforgeCards), None)
KeyforgeCardsActions = KeyforgeCardsFixed[KeyforgeCardsFixed["Type"] == "Action"]
KeyforgeCardsArtifacts = KeyforgeCardsFixed[KeyforgeCardsFixed["Type"] == "Artifact"]
KeyforgeCardsCreatures = KeyforgeCardsFixed[KeyforgeCardsFixed["Type"] == "Creature"]
KeyforgeCardsTokenCreatures = KeyforgeCardsFixed[
    KeyforgeCardsFixed["Type"] == "TokenCreature"
]
KeyforgeCardsUpgrades = KeyforgeCardsFixed[KeyforgeCardsFixed["Type"] == "Upgrade"]
KeyforgeCardsTraits = KeyforgeCardsFixed.where(pd.notnull(KeyforgeCards), None)

# Combines Keyforge Creatures and Token Creatures into one table call KeyforgeCardTotalCreatures
combineCreatures = [KeyforgeCardsCreatures, KeyforgeCardsTokenCreatures]
KeyforgeCardsTotalCreatures = pd.concat(combineCreatures)

# Setting the columns of the tables from the CSV using the titles of the CSV columns
cardFeatures = ["Name","House"]
# Setting final tables
cardTable = KeyforgeCardsFixed[cardFeatures].copy()
#For loading the names of the images into the database
path = "C:/Users/video/Desktop/Coding fun/MyWebsites/comboforge/src/assets/Cards"
# Paths for the folders of skills and traits
brobnar_path = path + "\Brobnar"
dis_path = path + "\Dis"
ekwidon_path = path + "\Ekwidon"
logos_path = path + "\Logos"
mars_path = path + "\Mars"
sanctum_path = path + "\Sanctum"
saurian_path = path + "\Saurian"
shadows_path = path + "\Shadows"
star_alliance_path = path + "\Star Alliance"
unfathomable_path = path + "\\Unfathomable"
untamed_path = path + "\\Untamed"
special_path = path + "\Special"

# List of skills and traits
brobnar_list = os.listdir(brobnar_path)
dis_list = os.listdir(dis_path)
ekwidon_list = os.listdir(ekwidon_path)
logos_list = os.listdir(logos_path)
mars_list = os.listdir(mars_path)
sanctum_list = os.listdir(sanctum_path)
saurian_list = os.listdir(saurian_path)
shadows_list = os.listdir(shadows_path)
star_alliance_list = os.listdir(star_alliance_path)
unfathomable_list = os.listdir(unfathomable_path)
untamed_list = os.listdir(untamed_path)
special_list = os.listdir(special_path)
combined_list=brobnar_list+dis_list+ekwidon_list+logos_list+mars_list+sanctum_list+saurian_list+shadows_list+star_alliance_list+star_alliance_list+unfathomable_list+untamed_list+special_list

sorted_combined_list=sorted(combined_list)
sortedCardTable=cardTable.sort_values(by=['Name'])
panda_comb_list=pd.DataFrame(sorted_combined_list)
nump_comb_list=np.array(sorted_combined_list)
print(cardTable)
sortedCardTable['Card_Image']=panda_comb_list
print(sortedCardTable)

np.savetxt('C:/Users/video/Desktop/Coding fun/MyWebsites/comboforge/src/Database/Card_Image_Table.txt',nump_comb_list)