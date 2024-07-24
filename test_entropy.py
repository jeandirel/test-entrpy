def generate_diagonal_table(width, height):
    # Crée une table vide
    table = [[None for _ in range(width)] for _ in range(height)]
    
    value = 0
    # Remplissage de la table selon la diagonale
    for start_col in range(width):
        row = 0
        col = start_col
        while row < height and col >= 0:
            table[row][col] = value
            value += 1
            row += 1
            col -= 1
    
    for start_row in range(1, height):
        row = start_row
        col = width - 1
        while row < height and col >= 0:
            table[row][col] = value
            value += 1
            row += 1
            col -= 1
    
    # Affichage du tableau de manière esthétique
    max_value_length = len(str(value - 1))
    for row in table:
        print(" ".join(f"{x:>{max_value_length}}" if x is not None else " " * max_value_length for x in row))

# Exemple d'utilisation
width = 4
height = 6
generate_diagonal_table(width, height)
