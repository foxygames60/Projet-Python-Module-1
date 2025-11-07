base_score = 1000

coins_collected_str = input("Combien de pièces collectées ? ")
coins_collected = int(coins_collected_str)

no_damage_bonus_str = input("As-tu finis le niveau sans prendre de dégâts ? ")
no_damage_bonus = no_damage_bonus_str == "Oui"

coin_bonus = coins_collected * 50

damage_multiplier = 1
if no_damage_bonus == True :
    damage_multiplier = 2

final_score = (base_score + coin_bonus) * damage_multiplier

print("---NIVEAU TERMINÉ---")
print(f"Score de base : {base_score}\nBonus (Pièces) : {coins_collected}\nMultiplicateur : {no_damage_bonus}")
print(f"Score final :  {final_score}")