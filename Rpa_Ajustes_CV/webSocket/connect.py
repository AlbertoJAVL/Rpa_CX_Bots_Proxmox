import json
import stomper as stomper
import websocket
import time
import asyncio
import threading
import socket

last_activity_time = time.time()

websocket.enableTrace(True)

try:
    name_host = socket.gethostname()
    adress_ip = socket.gethostbyname(name_host)
    
    status_global="Conectado"

    ws = websocket.create_connection("ws://192.168.50.42:90/api/ws")

    def send_message(status):
        
        global last_activity_time 
        global status_global

        status_global = status
        last_activity_time = time.time()

        bot_model= {
            "ip" : adress_ip,
            "status" : status
        }

        ws.send(stomper.send("/app/monitoring", json.dumps(bot_model)))

    async def send():
        while True:
            if time.time() - last_activity_time > 60:
                send_message(status_global)

    def run_loop():
        asyncio.run(send())

    thread = threading.Thread(target=run_loop)
    thread.start()

except Exception as e:
    ws.close()
    print("Error al conectar al WebSocket", e)