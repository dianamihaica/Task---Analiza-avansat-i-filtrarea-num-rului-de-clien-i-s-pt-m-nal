# Introducerea numărului de clienți pentru fiecare zi a săptămânii
clienți_luni = int(input("Introduceți numărul de clienți pentru luni: "))
clienți_marți = int(input("Introduceți numărul de clienți pentru marți: "))
clienți_miercuri = int(input("Introduceți numărul de clienți pentru miercuri: "))
clienți_joi = int(input("Introduceți numărul de clienți pentru joi: "))
clienți_vineri = int(input("Introduceți numărul de clienți pentru vineri: "))
clienți_sâmbătă = int(input("Introduceți numărul de clienți pentru sâmbătă: "))
clienți_duminică = int(input("Introduceți numărul de clienți pentru duminică: "))

# Calcularea valorilor
total_săptămână = (clienți_luni + clienți_marți + clienți_miercuri + clienți_joi + clienți_vineri + clienți_sâmbătă + clienți_duminică)
print(f"Total clienți în săptămână: {total_săptămână}")
total_lucrătoare = clienți_luni + clienți_marți + clienți_miercuri + clienți_joi + clienți_vineri
print(f"Total clienți în zilele lucrătoare: {total_lucrătoare}")
total_weekend = clienți_sâmbătă + clienți_duminică
print(f"Total clienți în weekend: {total_weekend}")

# Verificare duminică vs sâmbătă
print("Duminică a fost o zi de vânzări mai bună decât sâmbătă"
      if clienți_duminică > clienți_sâmbătă
      else "Sâmbătă a fost o zi de vânzări mai bună decât duminică")

# Comparare zile lucrătoare vs. weekend
if total_lucrătoare > total_weekend:
    print("În zilele lucrătoare fost mai mulți clienți decât în  weekend.")
else:
    print("În weekend au fost mai mulți clienți decât zilele lucrătoare.")

# Verificare zile de weekend individual
if clienți_sâmbătă > 100 and clienți_duminică > 100:
    print("Ambele zile de weekend au avut mai mult de 100 de clienți.")
elif clienți_sâmbătă > 100 or clienți_duminică > 100:
    print("Doar o zi de weekend a avut mai mult de 100 de clienți.")
else:
    print("Nici o zi de weekend nu a avut mai mult de 100 de clienți.")
