from classes.converterFactory import ConvertFactory

def convert_image(input_format, output_format):
    factory = ConvertFactory()
    converter = factory.create_converter(output_format)
    
    if converter:
        converter.convert(input_format)
    else:
        print(f"No converter found for format: {output_format}")

pic1 = convert_image('gif', 'png')
pic2 = convert_image('jpeg', 'gif')
pic3 = convert_image('png', 'jpeg')