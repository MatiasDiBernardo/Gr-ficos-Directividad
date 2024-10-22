import numpy as np
import os   

def load_basta(path_basta):
    frecs = []
    system_response = []
    driver = []
    vent_ex = []
    rta_imp = []

    with open(path_basta, 'r') as fh:
        for lines in fh:
            lines = lines.replace("\n", "")
            values = lines.split("\t")
            if values[0][0] != "f":
                frecs.append(float(values[0]))
                system_response.append(float(values[1]))
                driver.append(float(values[2]))
                vent_ex.append(float(values[3]))
                rta_imp.append(float(values[4]))
    
    return np.array(frecs), np.array(system_response), np.array(driver), np.array(vent_ex), np.array(rta_imp)

def load_basta2(path_basta):
    frecs = []
    system_response = []
    imp = []

    with open(path_basta, 'r') as fh:
        for lines in fh:
            lines = lines.replace("\n", "")
            values = lines.split("\t")
            if values[0][0] != "f":
                frecs.append(float(values[0]))
                system_response.append(float(values[1]))
                imp.append(float(values[2]))
    
    return np.array(frecs), np.array(system_response), np.array(imp)

def load_rew(path_rew):
    freqs_rew = []
    rta_imp_rew = []

    with open(path_rew, 'r') as fh:
        for lines in fh:
            values = lines.split(" ")
            if values[0][0] != "f":
                freqs_rew.append(float(values[0]))
                rta_imp_rew.append(float(values[1]))
    
    return np.array(freqs_rew), np.array(rta_imp_rew)

def load_arta(path_arta):
    frecs = []
    system_response = []

    with open(path_arta, 'r') as fh:
        for lines in fh:
            lines = lines.replace("\n", "")
            values = lines.split("\t")
            
            if len(values) == 2:
                f = values[0].replace(" ", "")
                mag = values[1].replace(" ", "")
                
                frecs.append(float(f))
                system_response.append(float(mag))
    
    return np.array(frecs), np.array(system_response) 

def load_data_directivity(path_base):
    """Le das el path donde están las mediciones y te devuelve un array de frecuencias
    y un diccionario que tiene como llave el ángulo (numero entero) y como valor la
    magnitud de la medición (np.array).

    Args:
        path_base (str): Path base de la medición
    
    Return:
        freqs (np.array): Eje de frecuencia
        rta (dicc)[int][np.array]: Diccionario con la respuesta por ángulo
    """
    
    list_rtas = os.listdir(path_base)
    rta = {}

    for r in list_rtas:
        freqs, mag = load_arta(os.path.join(path_base, r))
        angle = r.split(".")[0].split("_")[-1]
        rta[int(angle)] = mag
    
    return freqs, rta