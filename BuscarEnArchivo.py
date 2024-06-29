def buscar_en_archivo(ruta_archivo, texto_a_buscar):
    try:
        with open(ruta_archivo, 'r') as archivo:
            # Iterar sobre cada línea del archivo
            for numero_linea, linea in enumerate(archivo, 1):
                # Verificar si la línea contiene el texto buscado
                if texto_a_buscar in linea:
                    print(f"Se encontró '{texto_a_buscar}' en la línea {numero_linea}:")
                    print(linea)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

# Ejemplo de uso
ruta_archivo = ""  # Cambia esto por la ruta de tu archivo
texto_a_buscar = "- host:"  # Cambia esto por el texto que deseas buscar
buscar_en_archivo(ruta_archivo, texto_a_buscar)