# Liste des commandes de sandwichs
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"
]

# 1 :
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []

#  2 :
while sandwich_orders:  # Tant qu'il reste des sandwichs à préparer
    sandwich = sandwich_orders.pop(0)  # Prendre le premier sandwich de la liste
    finished_sandwiches.append(sandwich)  # Ajouter le sandwich préparé à la liste
    print(f"I made your {sandwich.lower()}")  # Afficher un message de confirmation

#  3 :
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)