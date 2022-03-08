
import math
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/seleccionar',methods=['GET'])
def getSeleccionar():
    operacion = request.args.get('operacion')

    if(operacion == "formulaGeneral"):
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        c = float(request.args.get('c'))
        resultado = (-(b) + ((math.sqrt(b*b)-(4*a*c))))/2*a
        resultado2 = (-(b) - ((math.sqrt(b*b)-(4*a*c))))/2*a

    elif(operacion =="segundaLey"):
        masa= float(request.args.get('masa'))
        aceleracion= float(request.args.get('aceleracion'))
        resultado = (masa*aceleracion)
       
    return jsonify ({"resultado":resultado,"resultado2":resultado2})
if __name__ == '__main__':
    app.run(debug=True, port=4000)
