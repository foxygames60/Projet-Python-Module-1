original_amount_str = input("Quantité de l'ingrédient : ")
original_amount = float(original_amount_str)

original_servings_str = input("Nombre de personnes initial : ")
original_servings = int(original_servings_str)

desired_servings_str = input("Pour combien de personnes tu cuisines finalement ? ")
desired_servings = int(desired_servings_str)

scaling_factor = desired_servings / original_servings

new_amount = float(original_amount * scaling_factor)

print("---RECETTE AJUSTÉE---")
print(f"La recette originale est pour {original_servings} personnes.")
print(f"Pour cuisiner pour {desired_servings} personnes, il faut {new_amount} unités de votre ingrédient.")