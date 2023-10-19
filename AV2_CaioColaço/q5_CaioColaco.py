from flask import Flask, request, jsonify
from PIL import Image, ImageEnhance
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

# Refatorando questão 3:
@app.route("/images", methods=["POST"])
def images():
    try:
        input_image = request.form["path"]

        brightness_factor = float(request.form["percent"])

        # Abra a imagem e aplique o ajuste de brilho
        input_image = Image.open(input_image)
        output_image = ImageEnhance.Brightness(input_image).enhance(brightness_factor)

        # Salve a imagem ajustada em um buffer de bytes
        output_buffer = io.BytesIO()
        output_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)

        # Retorne a imagem como resposta
        return jsonify(image=output_buffer.read().decode("latin-1"))

    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run(debug=True)
