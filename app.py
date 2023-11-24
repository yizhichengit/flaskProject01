from flask import Flask, request

app = Flask(__name__)

def c_to_f(celsius):
    return celsius * 9.0 / 5 + 32

def f_to_c(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

@app.route('/convert_temperature', methods=['GET'])
def convert_temperature():
    temp_type = request.args.get('type')
    value = float(request.args.get('value'))

    if temp_type == 'C':
        return {'fahrenheit': c_to_f(value)}
    elif temp_type == 'F':
        return {'celsius': f_to_c(value)}
    else:
        return {'error': 'Invalid temperature type'}

if __name__ == '__main__':
    app.run()

