nome_pagina = 'Calculadora'
 
from flask import Flask, render_template, request
from Calculos import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', titulo = nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['n1'])
    n2 = int(request.args['n2'])

    r_soma = (soma(n1,n2))
    r_subtracao = (subtracao(n1,n2)) 
    r_multiplicacao = (multiplicacao(n1, n2))
    r_div_int = (divisao_inteira(n1,n2))
    r_div_fra = (divisao_fracionada(n1, n2)) 
    r_resto = (resto_divisao(n1, n2))
    r_raiz = (raiz(n1, n2))

    resultados = {
        'soma'          : (r_soma),
        'subtracao'     : (r_subtracao),
        'multiplicacao' : (r_multiplicacao),
        'div_int'       : (r_div_int),
        'div_fra'       : (r_div_fra), 
        'resto'         : (r_resto), 
        'raiz'          : (r_raiz)
    }

    
    return render_template('resultado.html', n1 = n1, n2 = n2, resultado = resultados)

app.run()