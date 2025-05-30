import json
import stomper as stomper
import websocket
import socket

def connect(txt):
    print("m")
    # websocket.enableTrace(True)

    # name_host = socket.gethostname()
    # adress_ip = socket.gethostbyname(name_host)
  
    # try:
        
    #     ws = websocket.create_connection("ws://192.168.50.42:90/api/ws")

    #     bot_model= {
    #             "ip" : adress_ip,
    #             "status" : txt
    #         }

    #     ws.send(stomper.send("/app/monitoring", json.dumps(bot_model)))

    #     ws.close()

    # except Exception as e:
    #     print("Error al conectar al WebSocket", e)