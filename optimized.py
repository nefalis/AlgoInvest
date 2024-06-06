import csv
import time

def choice_csv():
    #choix du fichier csv a lire
    print("Veuillez choisir le fichier CSV à analyser :")
    print("1. action_bruteforce.csv")
    print("2. data/dataset1_Python+P7.csv")
    print("3. data/dataset2_Python+P7.csv")
    choice = input("Entrez le numéro correspondant au fichier (1, 2 ou 3) : ")

    if choice == '1':
        return 'data/action_bruteforce.csv'
    elif choice == '2':
        return 'data/dataset1_Python+P7.csv'
    elif choice == '3':
        return 'data/dataset2_Python+P7.csv'
    else:
        print("Choix invalide. Veuillez relancer le programme et choisir 1, 2 ou 3.")
        return

def optimized():
    """ algorithme optimisé """

    csv_file_path = choice_csv()

    # Début de la mesure du temps
    start_time = time.time()

    max_budget = 500

    # lecture des données du fichier csv
    actions = []
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cost = float(row['price'])
            profit = float(row['profit'])
            if cost > 0 and profit > 0:
                action = {
                    'name': row['name'],
                    'cost': cost,
                    'profit': profit
                }
                actions.append(action)

    # Initialise le tableau de programmation dynamique
    # n= nombre total d'action dispo
    # dp = tableau dynamique - dp[i][w] = profit maximum
    n = len(actions)
    dp = [[0] * (max_budget + 1) for _ in range(n + 1)]

    # Remplir le tableau
    # parcourt chaque action dispo
    for i in range(1, n + 1):
        # parcourt chaque budget possible
        for w in range(max_budget + 1):
            # si cout action est inf a budget w - dp[i][w] prend la valeur max
            if actions[i-1]['cost'] <= w:
                # dp[i-1][w] profit max sans action actuelle
                # actions[i-1]['cost'] * actions[i-1]['profit'] / 100 profit de l'action actuel
                # dp[i-1][w - actions[i-1]['cost']] profit max pour le budget restant avec action actuelle
                dp[i][w] = max(dp[i-1][w], actions[i-1]['cost'] * actions[i-1]['profit'] / 100 + dp[i-1][w - int(actions[i-1]['cost'])])
            # si cout depasse budget on garde la valeur dp[i][w]
            else:
                dp[i][w] = dp[i-1][w]


    # Reconstituer la meilleure combinaison avec le tableau dp
    # on commence par budget max et on remonte en verif les actions incluses dans la combinaison optimale
    w = max_budget
    best_combination = []
    # on parcourt les actions en sens inverse de n à 1 - n=nb total action
    for i in range(n, 0, -1):
        # verif si dp[i][w] est différent de dp[i-1][w] car i-1 a été inclu si oui donc ajout action a best_combination
        if dp[i][int(w)] != dp[i-1][int(w)]:
            best_combination.append(actions[i-1])
            # on reduit le budget w de cost de l'action i-1
            w -= actions[i-1]['cost']

    # Calculer le profit total de la meilleure combinaison
    best_profit = sum(action['cost'] * action['profit'] / 100 for action in best_combination)
    best_cost = sum(action['cost'] for action in best_combination)

    # Affichage des résultats
    if not best_combination:
        print("Pas de combinaison valide trouvée.")
    else:
        print("Les actions sélectionnées sont :")
        for action in best_combination:
            print(f"  {action['name']} - Coût: {action['cost']}€, Profit: {action['profit']}%")
        print(f"\nCoût total des actions : {best_cost} euros")
        print(f"Profit total après 2 ans: {best_profit:.2f}€\n")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nTemps d'exécution : {execution_time:.4f} secondes\n")