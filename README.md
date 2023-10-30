# **Honeypot-Dokumentation**

## **Beschreibung des Projekts**

Dieses Projekt implementiert einen **einfachen SSH-Honeypot** mithilfe von **Paramiko**. Der Honeypot überwacht den SSH-Port (Standard: 22) und protokolliert alle Anmeldeversuche mit Benutzername und Passwort. Zusätzlich sendet er eine Benachrichtigung über **Telegram** bei jedem Anmeldeversuch.

## **Installation**

Um den Honeypot zu installieren, müssen Sie die folgenden Schritte befolgen:

1. Installieren Sie die erforderlichen **Python-Bibliotheken**:

    ```bash
    pip install **paramiko python-telegram-bot**
    ```

2. Passen Sie die **Konfigurationsvariablen** im Code an (z.B. `HONEYPOT_PORT`, `HOST_KEY_FILE`, `USERNAME`, `PASSWORD`, `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`).

3. Starten Sie den Honeypot mit dem Befehl:

    ```bash
    python honeypot.py <host_key_file>
    ```

## **Verwendete Bibliotheken und Abhängigkeiten**

- [**Paramiko**](https://www.paramiko.org/): Eine Implementierung von SSHv2 für Python.
- [**python-telegram-bot**](https://python-telegram-bot.readthedocs.io/): Eine Python-Bibliothek für die Telegram Bot API.

## **Konfiguration**

Die Konfiguration erfolgt durch Anpassen der entsprechenden Variablen im Quellcode:

- `HONEYPOT_PORT`: Der Überwachungs-SSH-Port.
- `HOST_KEY_FILE`: Der Pfad zur Datei mit dem Hostschlüssel.
- `USERNAME`: Der Benutzername für den Honeypot.
- `PASSWORD`: Das Passwort für den Honeypot.
- `TELEGRAM_TOKEN`: Der Token für den Telegram-Bot.
- `TELEGRAM_CHAT_ID`: Die Chat-ID für die Telegram-Benachrichtigungen.

## **Verwendung**

Der Honeypot überwacht den SSH-Port und sendet Benachrichtigungen über **Telegram** bei Anmeldeversuchen. Das Starten erfolgt durch Ausführen der `start_honeypot`-Funktion im Hauptprogramm.

## **Anpassung und Erweiterung**

Das Projekt kann angepasst werden, um weitere Informationen zu protokollieren oder spezifischere Benachrichtigungen zu senden. Dies kann durch Ändern der `FakeSSHServer`-Klasse oder der Telegram-Funktion erfolgen.

## **Lizenzinformationen**

Dieses Projekt steht unter der [**MIT-Lizenz**](LICENSE).
