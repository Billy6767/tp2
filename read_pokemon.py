import csv

def lire_pokemon_csv(fichier_csv):
    pokemon_dict = {}

    with open(fichier_csv, mode='r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            nom = row[0]
            stats = list(map(int, row[1:]))
            pokemon_dict[nom] = stats

    return pokemon_dict

if __name__ == "__main__":
    fichier_csv = 'pokemon.csv'
    pokemon_stats = lire_pokemon_csv(fichier_csv)
    print(pokemon_stats)