from .JPEGconverter import jpegConverter
from .PNGconverter  import pngConverter
from .GIFconverter  import gifConverter 

class ConvertFactory:
    def create_converter(self, format):
        self.image_converters = {
            "jpeg" : jpegConverter,
            "png"  : pngConverter,
            "gif"  : gifConverter
        }

        converter_class = self.image_converters.get(format.lower())
        

        return converter_class(format)


