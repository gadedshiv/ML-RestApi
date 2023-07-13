import json
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def home():
    result = '{"customers" : [{"given_name": "Michael","surname": "Jack son","street_number": "MG Road","address_1": "","address_2": "Pune","suburb": "","postcode": 411045,"state": "MH","mobile": "9756656656","email": "abc@gmail.com","bankname":"HDFC","account": "6545646546564","IBAN": "HDFC566565","confidence":0.99765},{"given_name": "Michael","surname": "Jack son","street_number": "","address_1": "","address_2": "","suburb": "","postcode": 411045,"state": "MH","mobile": "9756656656","email": "xyz@gmail.com","bankname":"HDFC","account": "56445645646","IBAN": "HDFC26155","confidence":0.98765}]}'
    y = json.loads(result)
    return jsonify(y["customers"][0])

if __name__ == '__main__':
  
    app.run(host="0.0.0.0")
