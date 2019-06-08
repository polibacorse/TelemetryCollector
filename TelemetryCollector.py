import paho.mqtt.client as mqtt


def on_message(client, userdata, msg):

    client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
        
    


client_local= mqtt.Client("Telemetry_Collector")
client_remote= mqtt.Client("Telemetry_Sender")

client_local.on_message = on_message

client_local.connect("localhost", 1883, 160)
client_remote.connect("tamburodebiano.ddns.net",1883,160)
 #sistema i topic
client_local.subscribe('data/formatted/rpm')
client_local.subscribe('data/formatted/th20')
client_local.subscribe('data/formatted/tOil')
client_local.subscribe('data/formatted/vbatt')
client_local.subscribe('data/formatted/gear')
client_local.subscribe('data/formatted/position')
client_local.subscribe('data/formatted/speed')

client_local.loop_forever()
