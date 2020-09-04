from flask import Flask, render_template, jsonify, request
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime
from post import posts
app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/home')
def home_page():    
    #data =request.json['posts'][1]['Author']
    #ata_user = [{'name': Akinsoji}]
    posts.append([{'Author' : 'Akinsoji'}])
    return jsonify(posts)


if __name__ == '__main__':
    app.run(debug= True)