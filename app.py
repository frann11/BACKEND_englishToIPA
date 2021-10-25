import eng_to_ipa as ipa
from flask import request, Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=['POST'])
def words_to_ipa():
    data = request.get_json(silent=True)
    response = ipa.convert(data['words'])
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
