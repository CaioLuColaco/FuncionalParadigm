from PIL import Image, ImageEnhance

input_image = Image.open(
    input("Olá, bem vindo a questão de número 3\nPeço que digite aqui o caminho para o arquivo da imagem que deseja ajustar o brilho: \n")
)

brightness_factor = float(
    input("Em quantos por cento você deseja aumentar o brilho? (por exemplo, 0 para permanecer igual ou 50 para aumentar o brilho em 50%): ")
)

enhance_brightness = lambda image, factor: ImageEnhance.Brightness(image).enhance(
    (factor / 100) + 1
)

output_image = enhance_brightness(input_image, brightness_factor)
output_image.show()
