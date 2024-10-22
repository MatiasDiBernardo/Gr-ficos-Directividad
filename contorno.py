import matplotlib.pyplot as plt

from load_rta import load_data_directivity
from ventana_temporal import ventaneo_f, dict_to_arr, normalizacion, normalizacion_amplitud, remove_noise

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
    fig, ax = plt.subplots()
    contour = ax.contourf(X, Y, Z, levels= [-40, -30, -20, -15, -10, -7.5, -5, -2.5, 0, 2.5, 5], cmap='inferno')

    ax.set_xscale('log')
    ax.set_xlabel('Frecuencia [Hz]')
    octavas = [ 320, 640, 1250, 2500, 5000, 10000, 20000]
    ax.set_xticks(octavas, ["320", "640", "1250", "2500", "5000", "10000", "20000"])
    ax.set_ylabel('Angulo [grados]')
    ax.set_title(f'Contornos {nombre}')
    
    cbar = fig.colorbar(contour, ax=ax, orientation='vertical', fraction=0.05, pad=0.04)
    cbar.set_label('Nivel [dB]')

    plt.show()
        