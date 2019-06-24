import paho.mqtt.client as mqtt


speed_index = 0
position_index = 0
tOil_index = 0
th20_index = 0
rpm_index = 0
vbatt_index = 0
gear_index = 0

speed_TRIGGER = 0
position_TRIGGER = 0
tOil_TRIGGER = 2
th20_TRIGGER = 2
rpm_TRIGGER = 5
vbatt_TRIGGER = 10
gear_TRIGGER = 6

def on_message(client, userdata, msg):
    global speed_index
    global position_index
#    print("pos: ", position_index, ", speed: " ,speed_index," ",  msg.topic) 
    if(msg.topic == "data/formatted/speed"):
        speed_index = speed_index + 1
        if(speed_index > speed_TRIGGER):
            speed_index=0
            client_remote.publish( msg.topic, msg.payload.decode("utf-8"))

    if(msg.topic == "data/formatted/position"):
        position_index = position_index + 1
        if(position_index > position_TRIGGER):
            position_index=0
            client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
            
    if(msg.topic == "data/formatted/rpm"):
            rpm_index = rpm_index + 1
            if(rpm_index > rpm_TRIGGER):
                rpm_index=0
                client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
    if(msg.topic == "data/formatted/th20"):
            th20_index = th20_index + 1
            if(th20_index > th20_TRIGGER):
                th20_index=0
                client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
    if(msg.topic == "data/formatted/tOil"):
            tOil_index = tOil_index + 1
            if(tOil_index > tOil_TRIGGER):
                tOil_index=0
                client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
                
    if(msg.topic == "data/formatted/vbatt"):
            vbatt_index = vbatt_index + 1
            if(vbatt_index > vbatt_TRIGGER):
                vbatt_index=0
                client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
    if(msg.topic == "data/formatted/gear"):
            gear_index = gear_index + 1
            if(gear_index > gear_TRIGGER):
                gear_index=0
                client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
                            
# client_remote.publish( msg.topic, msg.payload.decode("utf-8"))



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
