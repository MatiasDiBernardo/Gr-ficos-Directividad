import matplotlib.pyplot as plt
import matplotlib

from load_rta import load_data_directivity
from calc_aux import ventaneo_f, dict_to_arr, normalizacion, normalizacion_amplitud, remove_noise

def grafico_contorno(path_data, nombre, tiempo_ventaneo):
    # Cargamos los datos
    freqs, rta = load_data_directivity(path_data)
    
    # Recortamos data según ventaneo
    freqs, rta =  ventaneo_f(freqs, rta, 1/tiempo_ventaneo)
    
    # Normalización amplitud
    rta = normalizacion_amplitud(rta)
    
    # Normalización de ejes respecto a eje central
    rta = normalizacion(rta)
    
    # Remove noise for better visualization
    rta = remove_noise(rta, -40)
    
    # Armar matriz de datos en base a la respuesta
    X, Y, Z = dict_to_arr(freqs, rta)
    
    # Crear el gráfico de contorno
    matplotlib.rcParams.update({'font.size': 12})
    fig, ax = plt.subplots()
    contour = ax.contourf(X, Y, Z, levels= [-40, -30, -20, -15, -10, -7.5, -5, -2.5, 0, 2.5, 5], cmap='inferno')

    ax.set_xscale('log')
    ax.set_xlabel('Frecuencia [Hz]')

    octavas = [300, 400, 500, 600, 700, 800, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 7500, 10000, 15000, 20000]
    octavas_str = [str(frec) for frec in octavas]
    ax.set_xticks(octavas, octavas_str)
    ax.set_ylabel('Angulo [grados]')
    ax.set_title(f'Contornos {nombre}')
    
    cbar = fig.colorbar(contour, ax=ax, orientation='vertical', fraction=0.05, pad=0.04)
    cbar.set_label('Nivel [dB]')

    plt.show()
        