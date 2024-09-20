from .auxiliares import obtener_maximo, promedio, obtener_mitad_de_maximo

def utn_mostrar_nombres_heroes(lis_nom: list):
    for n in lis_nom:
        print(n)

def utn_mostrar_identidades_heroes(lis_iden: list):
    for e in lis_iden:
        print(e)

def utn_mostrar_heroe_mayor_altura(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    altura = obtener_maximo(lis_alt)
    i = lis_alt.index(altura)

    print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}")

def utn_mostrar_heroes_mas_fuertes(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    poder = obtener_maximo(lis_pod)
    
    for i in range(len(lis_pod)):
        if float(lis_pod[i]) == poder:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")

def utn_filtrar_heroes_genero(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list, gen: str):
    for i in range(len(lis_gen)):
        if lis_gen[i] == gen:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")

def utn_mostrar_heroes_poder_superior_promedio(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    poder = promedio(lis_pod)

    for i in range(len(lis_pod)):
        if lis_pod[i] > poder:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")

def utn_mostrar_heroes_mas_debiles(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    poder = obtener_mitad_de_maximo(lis_pod)

    for i in range(len(lis_pod)):
        if lis_pod[i] <= poder:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")

if __name__ == '__main__':
    utn_mostrar_nombres_heroes(['Ironman', 'Batman', 'Wolverine', 'Flash', 'Spiderman', 'Remy LeBeau'])
    utn_mostrar_identidades_heroes(['Tony Stark', 'Bruce Wayne', 'James Howlett', 'Barry Allen', 'Miles Morales', 'Gambito'])