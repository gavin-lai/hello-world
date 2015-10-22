"""Cloud Foundry test"""
from flask import Flask
import os

app = Flask(__name__)

# On CF, get the port number from the environment variable VCAP_APP_PORT and server address with CF_INSTANCE_IP
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))
address = (os.getenv('CF_INSTANCE_IP'))

@app.route('/')
def hello_world():
    return 'Hello from Appfog World! I am running on address:port ' + str(address) + str (':') + str(port)

     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
