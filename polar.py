import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

from load_rta import load_data_directivity
from calc_aux import ventaneo_f, normalizacion_amplitud

def grafico_polar(path_datos, nombre, win_time):
    # Importar resultados en txt (path a carpeta)
    freqs, rta = load_data_directivity(path_datos)

    # Recorte de info según ventaneo
    freqs, rta = ventaneo_f(freqs, rta, 1/win_time)

    # Normalizar amplitud
    rta = normalizacion_amplitud(rta)

    # Definimos las frecuencias de interés
    octavas = np.array([320, 640, 1250, 2500, 5000, 10000, 20000])
    angulos = np.radians([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180])

    # Extender los ángulos para cubrir ambos lados (espejar)
    angulos_completos = np.concatenate((angulos, np.pi + angulos))

    # Crear los colores: degradado entre rojo (bajas), verde (medias) y azul (altas)
    colores = cm.get_cmap('hsv', len(octavas))

    # Crear la figura y los cuatro subplots distribuidos en 2 filas y 2 columnas
    matplotlib.rcParams.update({'font.size': 14})
    fig, axs = plt.subplots(1, 1, subplot_kw={'projection': 'polar'}, figsize=(7,6))
    plt.suptitle(f'Patrón Polar - {nombre}', fontsize=16)

    # Gráfico primeras 4 frecuencias
    for idx, freq in enumerate(octavas): 
        mag_h = [rta[ang][np.abs(freqs - freq).argmin()] for ang in [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]]
        mag_h = np.array(mag_h) - mag_h[0]
        mag_h_completo = np.concatenate((mag_h, mag_h[::-1]))
        axs.plot(angulos_completos, mag_h_completo, label=f"{freq} Hz", color=colores(idx))

    axs.set_theta_direction(-1)
    axs.set_theta_offset(np.pi / 2.0)
    axs.grid(True)

    # Crear leyenda compartida en la parte inferior
    lines_labels = [axs.get_legend_handles_labels()]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    fig.legend(lines, labels, loc='lower center', ncol=4)

    # Ajustar el layout para que no se superpongan los títulos y la leyenda
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.show()
