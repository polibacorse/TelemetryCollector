import paho.mqtt.client as mqtt


speed_index = 0
position_index = 0
toil_index = 0
th20_index = 0
rpm_index = 0
vbattdir_index = 0
gear_index = 0
pfuel_index = 0
poil_index = 0
pbrake_front_index = 0
pbrake_rear_index = 0
lambda_index = 0
tps_index = 0
map_index = 0

speed_TRIGGER = 0
position_TRIGGER = 0
toil_TRIGGER = 2
th20_TRIGGER = 2
rpm_TRIGGER = 5
vbattdir_TRIGGER = 10
gear_TRIGGER = 6
pfuel_TRIGGER = 0
poil_TRIGGER = 0
pbrake_front_TRIGGER = 0
pbrake_rear_TRIGGER = 0
lambda_TRIGGER = 0
tps_TRIGGER = 0
map_TRIGGER = 0

def on_message(client, userdata, msg):
    global speed_index
    global position_index
    global rpm_index
    global th20_index
    global toil_index
    global vbattdir_index
    global gear_index
    global pfuel_index
    global poil_index
    global pbrake_front_index
    global pbrake_rear_index
    global lambda_index
    global tps_index
    global map_index
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
    if(msg.topic == "data/formatted/toil"):
            toil_index = toil_index + 1
            if(toil_index > toil_TRIGGER):
                toil_index=0
                client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
                
    if(msg.topic == "data/formatted/vbattdir"):
            vbattdir_index = vbattdir_index + 1
            if(vbattdir_index > vbattdir_TRIGGER):
                vbattdir_index=0
                client_remote.publish( msg.topic, msg.payload.decode("utf-8"))
    if (msg.topic == "data/formatted/gear"):
        gear_index = gear_index + 1
        if (gear_index > gear_TRIGGER):
            gear_index = 0
            client_remote.publish(msg.topic, msg.payload.decode("utf-8"))
    if (msg.topic == "data/formatted/pfuel"):
        pfuel_index = pfuel_index + 1
        if (pfuel_index > pfuel_TRIGGER):
            pfuel_index = 0
            client_remote.publish(msg.topic, msg.payload.decode("utf-8"))
    if (msg.topic == "data/formatted/poil"):
        poil_index = poil_index + 1
        if (poil_index > poil_TRIGGER):
            poil_index = 0
            client_remote.publish(msg.topic, msg.payload.decode("utf-8"))
    if (msg.topic == "data/formatted/pbrake_front"):
        pbrake_front_index = pbrake_front_index + 1
        if (pbrake_front_index > pbrake_front_TRIGGER):
            pbrake_front_index = 0
            client_remote.publish(msg.topic, msg.payload.decode("utf-8"))
    if (msg.topic == "data/formatted/lambda"):
        lambda_index = lambda_index + 1
        if (lambda_index > lambda_TRIGGER):
            lambda_index = 0
            client_remote.publish(msg.topic, msg.payload.decode("utf-8"))
    if (msg.topic == "data/formatted/tps"):
        tps_index = tps_index + 1
        if (tps_index > tps_TRIGGER):
            tps_index = 0
            client_remote.publish(msg.topic, msg.payload.decode("utf-8"))
    if (msg.topic == "data/formatted/map"):
        map_index = map_index + 1
        if (map_index > map_TRIGGER):
            map_index = 0
            client_remote.publish(msg.topic, msg.payload.decode("utf-8"))
                            
# client_remote.publish( msg.topic, msg.payload.decode("utf-8"))



client_local= mqtt.Client("Telemetry_Collector")
client_remote= mqtt.Client("Telemetry_Sender")

client_local.on_message = on_message

client_local.connect("localhost", 1883, 160)
client_remote.connect("tamburodebiano.ddns.net",1883,160)
 #sistema i topic
client_local.subscribe('data/formatted/rpm')
client_local.subscribe('data/formatted/th20')
client_local.subscribe('data/formatted/toil')
client_local.subscribe('data/formatted/vbattdir')
client_local.subscribe('data/formatted/gear')
client_local.subscribe('data/formatted/position')
client_local.subscribe('data/formatted/speed')
client_local.subscribe('data/formatted/pfuel')
client_local.subscribe('data/formatted/poil')
client_local.subscribe('data/formatted/pbrake_front')
client_local.subscribe('data/formatted/pbrake_rear')
client_local.subscribe('data/formatted/lambda')
client_local.subscribe('data/formatted/tps')
client_local.subscribe('data/formatted/map')

client_local.loop_forever()
