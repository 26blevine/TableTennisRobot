from flask import Flask, jsonify, request
import os

# from important_stuff import real_functionality
app = Flask(__name__)
print("Hi")
app.config['UPLOAD_FOLDER'] = '/Users/benjylevine/Documents/GitHub/TableTennisRobot/files'


@app.route('/api/send', methods=['POST'])
def index():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "wow.jpg"))
    return jsonify({'result': 'success'})


def do_stuff(file):
    # do stuff
    # yay!
    return 'yay'


@app.route('/api/get_data', methods=['GET'])
def yay():
    output = do_stuff()
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)




