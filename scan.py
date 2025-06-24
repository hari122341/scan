from flask import Flask, request, jsonify
from pyzbar.pyzbar import decode
from PIL import Image
import io

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_barcode():
    file = request.files['file']
    image = Image.open(file.stream)
    barcodes = decode(image)
    if not barcodes:
        return jsonify({"result": "No barcode found"}), 400
    data = [b.data.decode('utf-8') for b in barcodes]
    return jsonify({"result": data})

if __name__ == '__main__':
    app.run(debug=True)
