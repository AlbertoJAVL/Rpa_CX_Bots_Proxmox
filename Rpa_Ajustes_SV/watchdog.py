import os, time, smtplib, subprocess, psutil
from email.message import EmailMessage

CMD          = ["python", "main.py"]
CHECK_EVERY  = 30      # segundos
MEM_LIMIT    = 85      # %
ALERT_EVERY  = 600     # segundos

MAIL_USER = os.getenv("MAIL_USER")   # defínelos en .env
MAIL_PASS = os.getenv("MAIL_PASS")
RECIPIENT = os.getenv("MAIL_TO")

def send_alert(subject, body):
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = MAIL_USER, RECIPIENT, subject
    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com") as s:
        s.login(MAIL_USER, MAIL_PASS)
        s.send_message(msg)

def main():
    last_alert = 0
    proc = subprocess.Popen(CMD)
    while True:
        if proc.poll() is not None:                 # El bot murió
            send_alert("RPA DETENIDO", "Proceso finalizado inesperadamente")
            proc = subprocess.Popen(CMD)

        mem = psutil.virtual_memory().percent
        if mem > MEM_LIMIT and time.time() - last_alert > ALERT_EVERY:
            send_alert("RPA – memoria alta", f"RAM al {mem}% – se reinicia bot")
            proc.terminate()
            proc = subprocess.Popen(CMD)
            last_alert = time.time()

        time.sleep(CHECK_EVERY)

if __name__ == "__main__":
    main()
