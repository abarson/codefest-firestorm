from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import atexit
import cf_deployment_tracker
import os
import json
import back.file_conversion.file_convert as fc
from back.api.watson_apis import Translator, ToneAnalysis

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

db_name = 'mydb'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/speechtotext', methods=['POST'])
def s2t():
    return render_template('s2t.html')

@app.route('/pdftotext')
def pdf2t():
    return render_template('pdf2text.html')

@app.route('/api', methods=['POST'])
def fetch_pdf():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print(fc.getPDFcontent(f.filename))
        return fc.getPDFcontent(f.filename)


@app.route('/translate', methods=['POST'])
def translate():
    if request.method == "POST":
        #out = "<!doctype html>\n"
        #out += "<div id="backgroundTop">
        
        #out += "<div id=\"header\">StudyBuddy</div>\n"
        #out += "<div id=\"description\"> A suite of tools for increasing study productivity </div><br>"
        #out += "</div>"


        return ""
        f = request.files['file']
        f.save(secure_filename(f.filename))
        text = fc.getPDFcontent(f.filename)
        translator = Translator()
        json = translator.translate(text, 'Spanish')
        return json['translations'][0]['translation']

        pass


@app.route('/tone_analysis', methods=['POST'])
def tone_analysis():
    if request.method == "POST":
        pass
        #f =



# /* Endpoint to greet and add a new visitor to database.
# * Send a POST request to localhost:8000/api/visitors with body
# * {
# *     "name": "Bob"
# * }
# */
@app.route('/api/visitors', methods=['GET'])
def get_visitor():
    if client:
        return jsonify(list(map(lambda doc: doc['name'], db)))
    else:
        print('No database')
        return jsonify([])

# /**
#  * Endpoint to get a JSON array of all the visitors in the database
#  * REST API example:
#  * <code>
#  * GET http://localhost:8000/api/visitors
#  * </code>
#  *
#  * Response:
#  * [ "Bob", "Jane" ]
#  * @return An array of all the visitor names
#  */
@app.route('/api/visitors', methods=['POST'])
def put_visitor():
    user = request.json['name']
    if client:
        data = {'name':user}
        db.create_document(data)
        return 'Hello %s! I added you to the database.' % user
    else:
        print('No database')
        return 'Hello %s!' % user

@atexit.register
def shutdown():
    if client:
        client.disconnect()

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
