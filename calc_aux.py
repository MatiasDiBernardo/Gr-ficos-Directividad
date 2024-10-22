import numpy as np 

def ventaneo_f(freqs, rtas, f_inf):
    # Encuentra el índice de la primera frecuencia que sea mayor que f_inf
    idx = np.argmax(freqs > f_inf)  # Busca el primer índice donde la frecuencia es mayor que f_inf
    
    if idx == 0:  # Si no hay ninguna frecuencia mayor que f_inf, no recortamos
        return freqs, rtas

    freqs = freqs[idx:]  # Recorta las frecuencias

    for clave in rtas:
        rtas[clave] = rtas[clave][idx:]  # Recorta cada array de respuestas

    return freqs, rtas

def dict_to_arr_v(f, dict):
    angles = np.array(list(dict.keys()))
    Z = np.array(list(dict.values()))
    X, Y = np.meshgrid(f, angles )
    return X, Y, Z

def dict_to_arr(f, data_dict):
    """
    Genera un grid a partir de un diccionario de datos y un vector.

    Parámetros:
    -----------
    f : array-like
        Vector que se utilizará para el eje X.
    data_dict : dict
        Diccionario donde las claves son los ángulos (eje Y) y los valores son las listas o arrays para Z.

    Retorna:
    --------
    X, Y, Z : arrays
        Arrays 2D para las coordenadas X, Y y Z del grid.
    """
    # Crear la matriz de valores
    Z = np.zeros((len(data_dict.keys()), len(f) )) 
    angles = []

    for i in range(len(data_dict.keys())):
        Z[i, :] = data_dict[i*15]
        angles.append(i*15)  

    # Crear el grid X, Y
    X, Y = np.meshgrid(f, np.array(angles))

    return X, Y, Z

def normalizacion_amplitud(rta):
    max_nivel = np.max(rta[0])
    for grados in rta:
       rta[grados] -= max_nivel - 5

    return rta

def normalizacion(rta):
    rta_cero = rta[0]
    for grados in rta:
       rta[grados] -= rta_cero
    return rta

def remove_noise(rta, min_level):
    for angle, mag in rta.items():
        rta[angle] = np.where(mag < min_level, min_level, mag)
    
    return rta

# Definir la función para el componente verde
def funcion_green(ang):
    cte_color = ang/180
    c = np.abs(cte_color - 0.5)
    c = np.round(0.9 - c, 2)
    return c
