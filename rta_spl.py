import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from load_rta import load_data_directivity
from calc_aux import funcion_green, ventaneo_f, normalizacion_amplitud

# Importamos las respuestas
path_medios_h = r'Mediciones Directividad\HFD horizontal\txt_3-9_ms'
freqs_m_h, rtas_m_h = load_data_directivity(path_medios_h)
rtas_m_h = normalizacion_amplitud(rtas_m_h)

path_medios_v = r'Mediciones Directividad\HFD vertical\txt_3-9_ms'
freqs_m_v, rtas_m_v = load_data_directivity(path_medios_v)
rtas_m_v = normalizacion_amplitud(rtas_m_v)

path_iso_h = r'Mediciones Directividad\Buffer horizontal\txt_3-9_ms'
freqs_i_h, rtas_i_h  = load_data_directivity(path_iso_h)
rtas_i_h = normalizacion_amplitud(rtas_i_h)

path_iso_v = r'Mediciones Directividad\Buffer vertical\txt_3-9_ms'
freqs_i_v, rtas_i_v = load_data_directivity(path_iso_v)
rtas_i_v = normalizacion_amplitud(rtas_i_v)

#-------------------------------------Recortamos-------------------------------------

d_m = 1.2 
h_m = 1.08 #altura y distancia directa
f_m = 256
freqs_m_h, rtas_m_h = ventaneo_f(freqs_m_h, rtas_m_h, f_m)
freqs_m_v, rtas_m_v = ventaneo_f(freqs_m_v, rtas_m_v, f_m)

d_i = 1.2 
h_i = 1.08 #altura y distancia directa 
f_i = 256 
freqs_i_h, rtas_i_h = ventaneo_f(freqs_i_h, rtas_i_h, f_i)
freqs_i_v, rtas_i_v = ventaneo_f(freqs_i_v, rtas_i_v, f_i)

# Crear la figura y los dos subplots distribuidos verticalmente
matplotlib.rcParams.update({'font.size': 12})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
plt.suptitle('Respuesta en Frecuencia HFD', fontsize=14)

# Graficar la primera subfigura (ax1)
for ang, mag in rtas_m_h.items():
    if ang in [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150 , 165, 180]:
        cte_color = ang/180
        if ang in [0, 90, 180]:
            ax1.plot(freqs_m_h, rtas_m_h[ang], label=f"Angulo {str(ang)}°", color = (1-cte_color, funcion_green(ang), cte_color))
        else:
            ax1.plot(freqs_m_h, rtas_m_h[ang], color = (1-cte_color, funcion_green(ang), cte_color))

ax1.set_xscale('log')
handles, labels = ax1.get_legend_handles_labels()
handles[1], handles[2] = handles[2], handles[1]
labels[1], labels[2] = labels[2], labels[1]
ax1.legend(handles, labels)
ax1.grid()
ax1.set_ylabel('Nivel [dB]')
ax1.set_title('Rotación Horizontal')
ax1.set_ylim(-50, 5.5)
octavas = np.array([300, 400, 500, 600, 700, 800, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 7500, 10000, 15000, 20000])
ax1.set_xticks(octavas)
ax1.set_xlim([min(freqs_m_h), max(freqs_m_h)])
ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter()) 

# Graficar la segunda subfigura (ax2)
for ang, mag in rtas_m_v.items():
    if ang in [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150 ,165,180]:
        cte_color = ang/180
        if ang in [0, 90, 180]:
            ax2.plot(freqs_m_v, rtas_m_v[ang], label=f"Angulo {str(ang)}°", color = (1-cte_color, funcion_green(ang), cte_color))
        else:
            ax2.plot(freqs_m_v, rtas_m_v[ang], color = (1-cte_color, funcion_green(ang), cte_color))

ax2.set_xscale('log')
handles, labels = ax2.get_legend_handles_labels()
handles[1], handles[2] = handles[2], handles[1]
labels[1], labels[2] = labels[2], labels[1]
ax2.legend(handles, labels)
ax2.grid()
ax2.set_ylim(-50, 5.5)
ax2.set_ylabel('Nivel [dB]')
ax2.set_title('Rotación Vertical')
ax2.set_xlim([min(freqs_m_v), max(freqs_m_v)])
ax2.set_xticks(octavas)
ax2.get_xaxis().set_major_formatter(plt.ScalarFormatter()) 
ax2.set_xlabel('Frecuencia [Hz]')
# Mostrar la figura con las dos subfiguras
plt.tight_layout()
plt.show()


# Crear la figura y los dos subplots distribuidos verticalmente
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
plt.suptitle('Respuesta en Frecuencia LFD', fontsize=14)

# Graficar la primera subfigura (ax1)
for ang, mag in rtas_i_h.items():
    if ang in [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150 , 165, 180]:
        cte_color = ang/180
        if ang in [0, 90, 180]:
            ax1.plot(freqs_i_h, rtas_i_h[ang], label=f"Angulo {str(ang)}°", color = (1-cte_color, funcion_green(ang), cte_color))
        else:
            ax1.plot(freqs_i_h, rtas_i_h[ang], color = (1-cte_color, funcion_green(ang), cte_color))

ax1.set_xscale('log')
handles, labels = ax1.get_legend_handles_labels()
handles[1], handles[2] = handles[2], handles[1]
labels[1], labels[2] = labels[2], labels[1]
ax1.legend(handles, labels)
ax1.grid()
ax1.set_ylim(-50, 5.5)
ax1.set_xlabel('Nivel [dB]')
ax1.set_xlim([min(freqs_i_h), max(freqs_i_h)])
ax1.set_title('Rotacion Horizontal')
ax1.set_xticks(octavas)
ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter()) 

# Graficar la segunda subfigura (ax2)
for ang, mag in rtas_i_v.items():
    if ang in [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150 ,165,180]:
        cte_color = ang/180
        if ang in [0, 90, 180]:
            ax2.plot(freqs_i_v, rtas_i_v[ang], label=f"Angulo {str(ang)}°", color = (1-cte_color, funcion_green(ang), cte_color))
        else:
            ax2.plot(freqs_i_v, rtas_i_v[ang], color = (1-cte_color, funcion_green(ang), cte_color))

ax2.set_xlim([min(freqs_i_v), max(freqs_i_v)])
ax2.set_xscale('log')
handles, labels = ax2.get_legend_handles_labels()
handles[1], handles[2] = handles[2], handles[1]
labels[1], labels[2] = labels[2], labels[1]
ax2.legend(handles, labels)
ax2.grid()
ax2.set_ylim(-50, 5.5)
ax2.set_title('Rotacion Vertical')
ax2.set_xticks(octavas)
ax2.get_xaxis().set_major_formatter(plt.ScalarFormatter()) 
ax2.set_xlabel('Frecuencia [Hz]')
ax2.set_ylabel('Nivel [dB]')
# Mostrar la figura con las dos subfiguras
plt.tight_layout()
plt.show()