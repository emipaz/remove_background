import os
from datetime import datetime
from rembg import remove

class RemoveBackground:
    def __init__(self, input_path, output):
        """
        Inicializa una instancia de RemoveBackground.

        :param input_path: Ruta de entrada para los archivos.
        :param output: Ruta de salida para los archivos procesados.
        """
        self.input = input_path
        self.output = output

    def procesar_carpetas(self):
        """
        Procesa las carpetas de archivos.

        Crea una carpeta con la fecha actual en la ruta de entrada.
        Recorre los archivos en la ruta de entrada y realiza las operaciones necesarias.
        """
        fecha = datetime.now().strftime("%Y%m%d-%H%M%S")
        carpeta = os.path.join(self.input, fecha)
        os.makedirs(carpeta, exist_ok=True)
        for archivo in os.listdir(self.input):
            if archivo.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")):
                input_path = os.path.join(self.input, archivo)
                output_path = os.path.join(carpeta, archivo)
                self._remover_fondo(input_path, output_path)
                self._mover_originales(input_path, output_path)

    def _remover_fondo(self, input_path, archivo):
        """
        Remueve el fondo de una imagen.

        :param input_path: Ruta de entrada de la imagen.
        :param archivo: Ruta de salida para la imagen procesada.
        """
        with open(input_path, "rb") as f, open(archivo, "wb") as f_out:
            f_out.write(remove(f.read()))

    def _mover_originales(self, input_path, output_path):
        """
        Mueve los archivos originales a una carpeta específica.

        :param input_path: Ruta de entrada del archivo original.
        :param output_path: Ruta de salida para el archivo original.
        """
        original = os.path.join(self.input, "originales")
        os.makedirs(original, exist_ok=True)
        filename = os.path.basename(input_path)
        new_path = os.path.join(original, filename)
        os.rename(input_path, new_path)
        
if __name__ == "__main__":
    input_path = "imagenes_procesar"
    output_path = "imagenes_procesadas"
    remove_background = RemoveBackground(input_path, output_path)
    remove_background.procesar_carpetas()