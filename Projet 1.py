bill_total_str = input("Quel est le montant de la facture ? ")
bill_total = float(bill_total_str)

tip_percentage_str = input("Pourcentage de pourboire que vous désirez laisser : ")
tip_percentage = int(tip_percentage_str)

num_people_str = input("Combien y a t-il de personnes ? ")
num_people = int(num_people_str)

tip_amount = bill_total * (tip_percentage / 100)
total_with_tip = bill_total + tip_amount
amount_per_person = total_with_tip / num_people
final_amount_per_person = round(amount_per_person, 2)

print("---RÉSUMÉ DU PAIEMENT---")
print(f"Montant final : {total_with_tip}")
print(f"Chaque personne doit payer {final_amount_per_person} €")
print(f"Basé sur une facture de {total_with_tip} avec un pourboire de {tip_percentage}% partagé entre {final_amount_per_person} personnes.")