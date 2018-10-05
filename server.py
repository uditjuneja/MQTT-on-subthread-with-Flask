# Threading Module
import threading
# Flask Module
from flask import Flask, request
# MQTT Module
import paho.mqtt.client as mqtt
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

# Flask configuration
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    return """MQTT on sub thread"""

def flask_app(app):
    app.run(debug=True)


# MQTT finctions
def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    msg = msg.payload
    write_csv(msg)

def write_csv(msg):
    print msg

# MQTT Server Launch
def launch():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)
    client.loop_forever()

def main(app):
    t1 = threading.Thread(target=launch, args=())
    t1.start()
    flask_app(app)

if __name__ == "__main__":
    main(app)
