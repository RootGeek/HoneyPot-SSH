import paramiko
import threading
import socket
import sys
import asyncio
from telegram import Bot

# Honeypot-Einstellungen
HONEYPOT_PORT = 22
HOST_KEY_FILE = "/home/kali/Desktop/honey/host_key.pem"

# Paramiko-Einstellungen
USERNAME = "fakeuser"
PASSWORD = "fakepassword"

# Telegram-Bot-Einstellungen
TELEGRAM_TOKEN = "Here_Your_Token"
TELEGRAM_CHAT_ID = Here_Your_Chat_ID

# Honeypot-Klasse
class FakeSSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        message = f"Login attempt with username: {username}, password: {password}"
        asyncio.run(send_telegram_message(message))  # Hier asyncio.run verwenden
        print(message)
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"

# Telegram-Funktionen
async def send_telegram_message(message):
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(TELEGRAM_CHAT_ID, message)
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

# Honeypot-Thread
async def start_honeypot():
    await send_telegram_message("Honeypot started and ready.")

    host_key = paramiko.RSAKey(filename=HOST_KEY_FILE)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", HONEYPOT_PORT))
    server.listen(100)

    print(f"Honeypot listening on port {HONEYPOT_PORT}...")

    while True:
        client, addr = server.accept()
        transport = paramiko.Transport(client)
        transport.add_server_key(host_key)
        server_instance = FakeSSHServer()
        transport.start_server(server=server_instance)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <host_key_file>")
        sys.exit(1)

    HOST_KEY_FILE = sys.argv[1]

    try:
        asyncio.run(start_honeypot())
    except Exception as e:
        print(f"Error: {e}")
