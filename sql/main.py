from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from datasource import datasource
app = Flask(__name__)
app.config['SECRET_KEY'] ='WER212'

@app.route('/')
def index():

    return render_template('index.html')
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    posts = [["this", "shit"]]
    if request.method == 'POST':
        name = request.form.get('file')
        surname= request.form.get('file1')
        email=request.form.get('file2')
        querry = {}
        if name is not None:
            querry["name"] = name
        if surname is not None:
            querry["surname"] = surname
        if email is not None:
            querry["email"] = email
        result = datasource.query(querry)
        posts=[[name, value] for name, value in result.items()]
    print(posts)
    return render_template('index2.html',posts=posts)
if __name__ == '__main__':
    app.run(debug=True,port=8015)