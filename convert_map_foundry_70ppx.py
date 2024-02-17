from tkinter import Tk, filedialog, simpledialog
from PIL import Image
import os

def get_image_path():
    Tk().withdraw()
    return filedialog.askopenfilename(title="Selecione uma imagem")


def get_dimensions_gui():
    root = Tk()
    root.withdraw()
    dimensions = simpledialog.askstring("Dimensions", "width x height (WxH):")
    if dimensions: 
        width, height = dimensions.split('x')
        return int(width), int(height)
    else:
        return None, None  
    
def optimize_and_convert_image(input_path, target_width, target_height):
    new_width = target_width * 70
    new_height = target_height * 70

    with Image.open(input_path) as img:
        img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)
        img_optimized = img_resized.convert("RGB")

        base, ext = os.path.splitext(input_path)
        new_filename = f"{base}-ok.webp"
        img_optimized.save(new_filename, "WEBP", quality=80)

        print(f"Optimized and Converted: {new_filename}")




    
if __name__ == "__main__":
    path = get_image_path()
    if path:
        width, height = get_dimensions_gui()
        optimize_and_convert_image(path, width, height)
    else:
        print("Nenhuma imagem selecionada.")
