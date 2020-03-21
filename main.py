from dotenv import load_dotenv
import os

from flask import Flask, request, send_file
import qrcode
import io

load_dotenv()

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def index():
    qr = qrcode.QRCode(
        version = int(request.args.get("version", 3)),
        error_correction = int(request.args.get("error_correction", qrcode.constants.ERROR_CORRECT_H)),
        box_size = int(request.args.get("box_size", 2)),
        border = int(request.args.get("border", 0)),
    )

    qr.add_data(request.args["text"])
    qr.make(fit = True)
    qr_img = qr.make_image(fill_color = request.args.get("fill_color", "black"), back_color = request.args.get("back_color", "white"))

    out = io.BytesIO()
    qr_img.save(out, 'PNG')
    out.seek(0)

    return send_file(
        out,
        attachment_filename = 'qr.png',
        mimetype = 'image/png',
    ), 200, {'Server': "QrGenerate"}


if __name__ == "__main__":
    app.run(host = os.getenv('HTTP_HOST'), port = os.getenv('HTTP_PORT'))  # debug=True
