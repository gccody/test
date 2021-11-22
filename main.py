from numpy.random import choice
import random
items = "Non-rare Gold","Rare Gold","Non-rare Silver","Rare Silver","Bronze","Icon"
itemProbabilities = [.35,.35,.1,.1,.099,.001]
nonGoldRatings = 83,82,81,80,79,78,77,76,75
nonGoldProbabilities = [.11,.11,.11,.11,.11,.11,.11,.11,.12]
nonRareGoldPlayers75 = 'Pedro Santos', 'Kuchta'
nonRareGoldPlayers76 = 'Morelos', 'Reynoso'
nonRareGoldPlayers77 = 'Rode', 'Omlin'
nonRareGoldPlayers78 = 'Pedro', 'Miranchuk'
nonRareGoldPlayers79 = 'Kepa', 'Alonso'
nonRareGoldPlayers80 = 'Alli', 'Coufal'
nonRareGoldPlayers81 = 'Orban', 'Kruse'
nonRareGoldPlayers82 = 'Suso', 'Rice'
nonRaregoldPlayers83 = 'Dzeko', 'Weghorst','Berardi'
N_TESTS = 9
unpack = []
for i in range(N_TESTS):
    rarity = choice(items,p=itemProbabilities)
    if rarity == "Non-rare Gold":
        rating = choice(nonGoldRatings,p=nonGoldProbabilities)
        if rating == 79:
            unpack.append(choice(nonRareGoldPlayers79))
        if rating == 78:
            unpack.append(choice(nonRareGoldPlayers78))
        if rating == 77:
            unpack.append(choice(nonRareGoldPlayers77))
        if rating == 76:
            unpack.append(choice(nonRareGoldPlayers76))
        if rating == 75:
            unpack.append(choice(nonRareGoldPlayers75))
    else:
        unpack.append(rarity)

print (unpack)

