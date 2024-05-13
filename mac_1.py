from flask import Flask, jsonify, request
import os
from multiFrame_integrated import analyzeFrame

# test
# from important_stuff import real_functionality
app = Flask(__name__)
print("Hi")
things = {}


# app.config['UPLOAD_FOLDER'] = './pictures2/'


@app.route('/api/send', methods=['POST'])
def index():
    file = request.files['file']
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    file.save(file.filename)
    things[1] = file.filename
    return jsonify({'result': 'success'})


def do_stuff(file):
    #todo: finish this method
    analysis = analyzeFrame(file)
    print(analysis)
    return analysis


@app.route('/api/get_data', methods=['GET'])
def yay():
    output = do_stuff(things[1])
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='3000', debug=True)




