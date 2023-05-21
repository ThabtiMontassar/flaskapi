from flask import Flask, jsonify, request
import requests
import xmltodict
import json

app = Flask(__name__)


@app.route('/bamboo_montassar_json', methods=['GET'])
def get_json_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({'error': 'Both start_date and end_date are required'}), 400

    url = "https://cd200f995baa75c237dce15a731e104a8532e6e0:x@api.bamboohr.com/api/gateway.php/novelus/v1/time_off/whos_out/?start="+start_date+"&end="+end_date
    response = requests.get(url)
    xml_dict = xmltodict.parse(response.content)

    # Convert the ordered dictionary to JSON
    json_data = json.dumps(xml_dict)

    return jsonify(json_data)


@app.route('/bamboo_montassar_local', methods=['GET'])
def get_json_data_local():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    data = [start_date, end_date]

    # Convert the ordered dictionary to JSON
    json_data = json.dumps(data)

    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=False, port=5555, host="0.0.0.0")
