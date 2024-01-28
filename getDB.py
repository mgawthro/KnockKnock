import sys
from firebase_admin import credentials, db, initialize_app
import json
input = sys.argv[1]

@app.route('/getDB.py/<input>')
def hitDB():
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("privKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://knockknock-b4d72-default-rtdb.firebaseio.com/'
    })

    # Get a reference to the root of your database
    root_ref = db.reference()

    # Query users with userName equal to "Nick123"
    query_result = root_ref.child("users").order_by_child("userName").equal_to(input).get()

    return json.dumps(query_result)