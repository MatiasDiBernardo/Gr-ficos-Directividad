import os
from contorno import grafico_contorno

t_win = 3.9 * 10**-3  # Tiempo de ventaneo en milisegundos

data_lfd_h = os.path.join("Mediciones Directividad", "Buffer horizontal", "txt_3-9_ms")
grafico_contorno(data_lfd_h, "LFD Horizontal", t_win)

data_lfd_v = os.path.join("Mediciones Directividad", "Buffer vertical", "txt_3-9_ms")
grafico_contorno(data_lfd_v, "LFD Vertical", t_win)

data_hfd_h = os.path.join("Mediciones Directividad", "HFD horizontal", "txt_3-9_ms")
grafico_contorno(data_hfd_h, "HFD Horizontal", t_win)

data_hfd_v = os.path.join("Mediciones Directividad", "HFD vertical", "txt_3-9_ms")
grafico_contorno(data_hfd_v, "HFD Vertical", t_win)