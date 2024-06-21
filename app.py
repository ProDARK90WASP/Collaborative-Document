from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID='AC2285b8a0a1311e0ff5bddc6c56f577a5'
    TWILIO_SYNC_SERVICE_SID='ISdb4e352375546ace1cb0201238f78474'
    TWILIO_API_KEY='SKe04a3118249920c5972c741483daa45c'
    TWILIO_API_SECRET='7FrRKsjnclqmrzoeMJQj52Vvv0h7DIeb'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt())



if __name__ == "__main__":
    app.run(port=5001)

