from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Convert file to NumPy array
    nparr = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    detector = cv2.barcode_BarcodeDetector()
    ok, decoded_info, _, _ = detector.detectAndDecode(image)

    if not ok or not decoded_info or decoded_info[0] == '':
        return jsonify({"result": "No barcode found"}), 200

    return jsonify({"result": decoded_info})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
