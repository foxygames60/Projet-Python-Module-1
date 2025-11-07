distance_km_str = input("Sélectionnez la distance à parcourir : ")
distance_km = float(distance_km_str)

efficiency_str = input("Sélectionnez le carburant à dépenser : ")
efficiency = float(efficiency_str)

prince_per_liter_str = input("Sélectionnez le prix d'un litre de carburant : ")
prince_per_liter = float(prince_per_liter_str)

fuel_needed = (distance_km / 100) * efficiency
total_cost = fuel_needed * prince_per_liter
final_total_cost = round(total_cost)

print("---BUDGET CARBURANT ESTIMÉ---")
print(f"Distance totale : {distance_km}")
print(f"CLe coût estimé du carburant pour ce voyage sera de {total_cost} €")
print(f"Nombre total de litres d'essence nécessaire : {fuel_needed} litres")