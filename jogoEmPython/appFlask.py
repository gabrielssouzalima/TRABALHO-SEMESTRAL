from flask import Flask, redirect, send_from_directory, jsonify, render_template, url_for
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Nível de log: DEBUG, INFO, WARNING, ERROR
    # Formato das mensagens
    format='%(asctime)s - %(levelname)s - %(message)s',
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chamadaJogoPython.html')

@app.route('/dist', methods=['GET'])
def download_jogo():
    try:
        download_folder = os.path.join(os.path.dirname(__file__), 'dist')
        arquivo = 'forca.exe'
        caminho_completo = os.path.join(download_folder, arquivo)
        
        if caminho_completo.exists():
            return redirect(url_for(caminho_completo))

        logging.debug(f"Tentando acessar arquivo em: {caminho_completo}")

        if not os.path.exists(caminho_completo):
            logging.error(f"Arquivo não encontrado: {caminho_completo}")
            return jsonify({'status': 'erro', 'mensagem': 'Arquivo não encontrado'}), 404

        return send_from_directory(directory=download_folder, path=arquivo, as_attachment=True)
    except Exception as e:
        logging.exception("Erro ao servir o arquivo")
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080, debug=True)