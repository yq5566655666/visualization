from flask import Flask, request, render_template
from getdata import get_data

app = Flask(__name__)

@app.route('/query/', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        code = request.form.get('name')
        dict_return = get_data(code)
        return render_template('query.html', dict_return = dict_return)
    else:
        dict_return = get_data('601318')
        return render_template('query.html', dict_return = dict_return)

if __name__ == '__main__':
    app.run(host= '127.0.0.1',port=3001,debug = True)