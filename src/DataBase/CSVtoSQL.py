import pandas as pd
import mariadb
import numpy as np

# Loading the data
KeyforgeCards = pd.read_csv(
    "C:/Users/video/Desktop/Coding fun/MyWebsites/comboforge/src/DataBase/dok-cards-2023-08-25.csv"
)
#SQL insert statment
sql_cards="INSERT INTO cards (name,house,expansion,type,rarity,rawAmber,text,flavor,power,armor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
sql_stats="INSERT INTO stats (cardName, `Creature Protection`, `Creature Protection Max`, `Creature Control`, `Creature Control Max`, `Expected Amber`, `Expected Amber Max`, `Amber Control`, `Amber Control Max`, Other, `Other Max`, Disruption, `Disruption Max`, Recursion, `Recursion Max`, Efficiency, `Efficiency Max`, Power, `Power Max`, `Artifact Control`, `Artifact Control Max`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
sql_ratings="INSERT INTO rating (cardName, aercMax, aercMin, win, loss, synergies, sasTraits) VALUES (?, ?, ?, ?, ?, ?, ?)"
sql_traits="INSERT INTO traits (cardName, traits) VALUES (?, ?)"
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
cardFeatures = [
    "Name",
    "House",
    "Expansion – #",
    "Type",
    "Rarity",
    "Raw Amber",
    "Power",
    "Armor",
    "Text",
    "Flavor Text",
]
statsFeatures = [
    "Name",
    "Creature Protection",
    "Creature Protection Max",
    "Creature Control",
    "Creature Control Max",
    "Expected Amber",
    "Expected Amber Max",
    "Amber Control",
    "Amber Control Max",
    "Other",
    "Other Max",
    "Disruption",
    "Disruption Max",
    "Recursion",
    "Recursion Max",
    "Efficiency",
    "Efficiency Max",
    "Effective Power",
    "Effective Power Max",
    "Artifact Control",
    "Artifact Control Max",
]
ratingFeatures = [
    "Name",
    "Aerc Max",
    "Aerc Min",
    "Wins",
    "Losses",
    "Synergies",
    "SAS traits",
]
actionsFeatures = ["Name"]
artifactFeatures = ["Name"]
creatureFeatures = ["Name", "Power", "Armor"]
upgradeFeatures = ["Name"]
traitsFeatures = ["Name", "Traits"]

# Setting final tables
cardTable = KeyforgeCardsFixed[cardFeatures].copy()
statTable = KeyforgeCardsFixed[statsFeatures].copy()
for i in range(statTable.shape[0]):  # iterate over rows
    for j in range(statTable.shape[1]):  # iterate over columns
        if pd.isna(statTable.iloc[i, j]):
            statTable.iloc[i, j] = statTable.iloc[i, j - 1]
ratingTable = KeyforgeCardsFixed[ratingFeatures].copy()
for i in range(ratingTable.shape[0]):  # iterate over rows
    if pd.isna(ratingTable.iloc[i, 1]):
        ratingTable.iloc[i, 1] = ratingTable.iloc[i, 2]
actionTable = KeyforgeCardsActions[actionsFeatures].copy()
artifactTable = KeyforgeCardsArtifacts[artifactFeatures].copy()
creatureTable = KeyforgeCardsTotalCreatures[creatureFeatures].copy()
for i in range(creatureTable.shape[0]):  # iterate over rows
    if pd.isna(creatureTable.iloc[i, 2]):
        creatureTable.iloc[i, 2] = 0
    if pd.isna(creatureTable.iloc[i, 1]):
        creatureTable.iloc[i, 1] = 0
upgradeTable = KeyforgeCardsUpgrades[upgradeFeatures].copy()
tempTraitsTable = KeyforgeCardsTraits[traitsFeatures].copy()

# Traits were tricky because they must be separated since some look like this:
# Ex Brammo GIANT | KNIGHT
# Must remove space using a tempstring and put the traits into an array using split()
traitsTable = [] * 2
traitPosition = 0
print(tempTraitsTable)
for index, row in tempTraitsTable.iterrows():
    if pd.isna(row["Traits"]):
        print("None trait found")
    else:
        tempString = row["Traits"]
        tempString.replace(" ", "")
        traitsToAdd = tempString.split("|")
        for k in range(len(traitsToAdd)):
            # Traits are singular words so we can replace blank space with a second check 
            traitsTable.append([row["Name"], traitsToAdd[k].replace(" ", "")])
            traitPosition += 1

# Trying to connect to the database
print("Connecting to db")

try:
    conn = mariadb.connect(
        user="root", password="Rw2023#24", host="127.0.0.1", port=3306, database="comboforge"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")

cur = conn.cursor()

# Start adding data into SQL database and commit after each table added
for x in range(len(cardTable.axes[0])):
    print("inserting " + str(cardTable.loc[x,:]))
    cur.execute(sql_cards, (cardTable['Name'][x], cardTable['House'][x], cardTable['Expansion – #'][x], cardTable['Type'][x], cardTable['Rarity'][x], str(cardTable['Raw Amber'][x]), cardTable['Text'][x], cardTable['Flavor Text'][x], cardTable['Power'][x], cardTable['Armor'][x]))

print("Committing db changes")
conn.commit()

for x in range(len(statTable.axes[0])):
    print("inserting " + str(statTable.loc[x,:]))
    cur.execute(sql_stats, (statTable['Name'][x], statTable['Creature Protection'][x], statTable['Creature Protection Max'][x], statTable['Creature Control'][x], statTable['Creature Control Max'][x], statTable['Expected Amber'][x], statTable['Expected Amber Max'][x], statTable['Amber Control'][x], statTable['Amber Control Max'][x], statTable['Other'][x], statTable['Other Max'][x], statTable['Disruption'][x], statTable['Disruption Max'][x], statTable['Recursion'][x], statTable['Recursion Max'][x], statTable['Efficiency'][x], statTable['Efficiency Max'][x], str(statTable['Effective Power'][x]), statTable['Effective Power Max'][x], statTable['Artifact Control'][x], statTable['Artifact Control Max'][x]))

print("Committing db changes")
conn.commit()

for x in range(len(ratingTable.axes[0])):
    print("inserting " + str(ratingTable.loc[x,:]))
    cur.execute(sql_ratings, (ratingTable['Name'][x], ratingTable['Aerc Max'][x], ratingTable['Aerc Min'][x], str(ratingTable['Wins'][x]), str(ratingTable['Losses'][x]), ratingTable['Synergies'][x], ratingTable['SAS traits'][x]))

print("Committing db changes")
conn.commit()
for x in range(len(traitsTable)):
    print("inserting " + traitsTable[x][0]+" "+traitsTable[x][1])
    cur.execute(
        sql_traits,
        (
            traitsTable[x][0],
            traitsTable[x][1],
        ),
    )

print("Committing db changes")
conn.commit()

print("Closing db connection")
conn.close()
