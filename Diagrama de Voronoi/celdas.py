import seaborn as sns
from random import randint
from PIL import Image, ImageColor
from math import sqrt

def celda(pos):
    y = pos // n
    x = pos % n
    if (x, y) in semillas:
        return semillas.index((x, y))  # Corregido para que compare coordenadas (x, y)
    
    cercano = None
    menor = n * sqrt(2)  # Distancia máxima posible en la imagen
    for i in range(k):
        (xs, ys) = semillas[i]
        dx = x - xs
        dy = y - ys
        dist = sqrt(dx**2 + dy**2)
        if dist < menor:
            cercano = i
            menor = dist
            
    return cercano

n = 500  # Tamaño de la imagen (500x500 píxeles)
k = 25   # Número de semillas
semillas = []

# Generar las semillas aleatorias
for s in range(k):
    while True:
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        if (x, y) not in semillas:
            semillas.append((x, y))
            break
print('Semillas creadas')

fondo = (255, 255, 0)  # Fondo AMARILLO
zona = Image.new('RGB', (n, n), color=fondo)  # Crear la imagen
p = zona.load()
c = sns.color_palette("dark", k).as_hex()  # Paleta de colores oscuros para las semillas

# Colorear las semillas con la paleta
for i, (x, y) in enumerate(semillas):
    p[x, y] = ImageColor.getrgb(c[i])

# Guardar una imagen inicial con solo las semillas
visual = zona.resize((10 * n, 10 * n))  # Redimensionar para visualizar mejor
visual.save("p4p.png")
print('Celdas calculadas')

# Calcular la celda más cercana para cada píxel y colorearlo
celdas = [celda(i) for i in range(n * n)]  # Generar la lista de celdas
for i in range(n * n):
    s = celdas[i]
    p[i % n, i // n] = ImageColor.getrgb(c[s])

# Volver a colorear las semillas en negro para destacarlas
for i in range(k):
    (x, y) = semillas[i]
    p[x, y] = (0, 0, 0)

# Guardar la imagen final
visual = zona.resize((2 * n, 2 * n))  # Redimensionar la imagen final
visual.save("p4pc.png")
