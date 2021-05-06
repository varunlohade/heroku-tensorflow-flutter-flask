import base64
from . import cartoonize
 
def convert(imagedata):
    model_path ='/v1/image/cartoongan/saved_models'
    data = base64.b64decode(imgdata)
    cartoon_img_data = cartoonize.cartoonize(data, model_path)

    return base64.b64encode(cartoon_img_data)