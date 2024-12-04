from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import os

app = Flask(__name__)

# Definindo as variáveis de ambiente
API_BASE_URL = "http://backend:8000"

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir o formulário de cadastro
@app.route('/cadastro', methods=['GET'])
def inserir_album_form():
    return render_template('cadastro.html')

# Rota para enviar os dados do formulário de cadastro para a API
@app.route('/inserir', methods=['POST'])
def inserir_album():
    titulo = request.form['titulo']
    cantor = request.form['cantor']
    quantidade = int(request.form['quantidade'])  # Para garantir que é um inteiro
    preco = float(request.form['preco'])          # Para garantir que é um float

    payload = {
        'titulo': titulo,
        'cantor': cantor,
        'quantidade': quantidade,
        'preco': preco
    }

    response = requests.post(f'{API_BASE_URL}/api/v1/albuns/', json=payload)
    
    if response.status_code == 201:
        return redirect(url_for('listar_albuns'))
    else:
        return "Erro ao inserir album", 500

# Rota para listar todos os albuns
@app.route('/estoque', methods=['GET'])
def listar_albuns():
    response = requests.get(f'{API_BASE_URL}/api/v1/albuns/')
    try:
        albuns = response.json()
    except:
        albuns = []
    return render_template('estoque.html', albuns=albuns)

# Rota para exibir o formulário de edição de albuns
@app.route('/atualizar/<int:album_id>', methods=['GET'])
def atualizar_album_form(album_id):
    response = requests.get(f"{API_BASE_URL}/api/v1/albuns/")
    #filtrando apenas o album correspondente ao ID
    albuns = [album for album in response.json() if album['id'] == album_id]
    if len(albuns) == 0:
        return "album não encontrado", 404
    album = albuns[0]
    return render_template('atualizar.html', album=album)

# Rota para enviar os dados do formulário de edição de album para a API
@app.route('/atualizar/<int:album_id>', methods=['POST'])
def atualizar_album(album_id):
    titulo = request.form['titulo']
    cantor = request.form['cantor']
    quantidade = request.form['quantidade']
    preco = request.form['preco']

    payload = {
        'id': album_id,
        'titulo': titulo,
        'cantor': cantor,
        'quantidade': quantidade,
        'preco': preco
    }

    response = requests.patch(f"{API_BASE_URL}/api/v1/albuns/{album_id}", json=payload)
    
    if response.status_code == 200:
        return redirect(url_for('listar_albuns'))
    else:
        return "Erro ao atualizar album", 500

# Rota para exibir o formulário de edição de album
@app.route('/vender/<int:album_id>', methods=['GET'])
def vender_album_form(album_id):
    response = requests.get(f"{API_BASE_URL}/api/v1/albuns/")
    #filtrando apenas o album correspondente ao ID
    albuns = [album for album in response.json() if album['id'] == album_id]
    if len(albuns) == 0:
        return "album não encontrado", 404
    album = albuns[0]
    return render_template('vender.html', album=album)

# Rota para vender um album
@app.route('/vender/<int:album_id>', methods=['POST'])
def vender_album(album_id):
    quantidade = request.form['quantidade']

    payload = {
        'quantidade': quantidade
    }

    response = requests.put(f"{API_BASE_URL}/api/v1/albuns/{album_id}/vender/", json=payload)
    
    if response.status_code == 200:
        return redirect(url_for('listar_albuns'))
    else:
        return "Erro ao vender album", 500

# Rota para listar todas as vendas
@app.route('/vendas', methods=['GET'])
def listar_vendas():
    response = requests.get(f"{API_BASE_URL}/api/v1/vendas/")
    try:
        vendas = response.json()
    except:
        vendas = []
    #salvando nomes dos albuns vendidos
    total_vendas = 0
    for venda in vendas:
        total_vendas += float(venda['valor_venda'])
    return render_template('vendas.html', vendas=vendas, total_vendas=total_vendas)

# Rota para excluir um album
@app.route('/excluir/<int:album_id>', methods=['POST'])
def excluir_album(album_id):
    response = requests.delete(f"{API_BASE_URL}/api/v1/albuns/{album_id}")
    
    if response.status_code == 200  :
        return redirect(url_for('listar_albuns'))
    else:
        return "Erro ao excluir album", 500

#Rota para resetar o database
@app.route('/reset-database', methods=['GET'])
def resetar_database():
    response = requests.delete(f"{API_BASE_URL}/api/v1/albuns/")
    
    if response.status_code == 200  :
        return render_template('confirmacao.html')
    else:
        return "Erro ao resetar o database", 500


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
