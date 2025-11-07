password = input("Saisissez un mot de passe : ")

password_length = len(password)

has_digit = any(i.isdigit() for i in password)

is_long_enough = password_length >= 8

if is_long_enough == True and has_digit == True :
    is_strong = True

print("---RAPPORT DE FORCE DU MOT DE PASSE---")
print(f"Longueur d'au moins 8 caractères : {is_long_enough}")

if is_strong == True :
    print("Conclusion : Votre mot de passe est considéré comme fort !")
else :
    print("Conclusion : Votre mot de passe peut être amélioré…")