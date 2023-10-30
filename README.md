<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SSH Honeypot Documentation</title>
</head>

<body>

    <h1>SSH Honeypot with Telegram Notifications</h1>

    <p>This project implements a simple SSH honeypot in Python. A honeypot is a security mechanism designed to simulate and monitor attacks on a specific service or network.</p>

    <h2>Features</h2>

    <ul>
        <li>Monitoring of SSH login attempts</li>
        <li>Telegram notifications for login attempts</li>
    </ul>

    <h2>Configuration</h2>

    <p>The behavior of the honeypot can be customized through configuration variables. These are located at the beginning of the <code>honeypot.py</code> file:</p>

    <ul>
        <li><code>HONEYPOT_PORT</code>: The port on which the honeypot listens (default: 22).</li>
        <li><code>HOST_KEY_FILE</code>: Path to the RSA host key file.</li>
        <li><code>USERNAME</code> and <code>PASSWORD</code>: Username and password for login attempts.</li>
        <li><code>TELEGRAM_TOKEN</code>: Token for the Telegram bot.</li>
        <li><code>TELEGRAM_CHAT_ID</code>: Chat ID for notifications.</li>
    </ul>

    <h2>Usage</h2>

    <ol>
        <li><strong>Clone the repository:</strong></li>
        <pre><code>git clone https://github.com/yourusername/honeypot.git</code></pre>

        <li><strong>Install required dependencies:</strong></li>
        <pre><code>pip install paramiko python-telegram-bot</code></pre>

        <li><strong>Adjust configuration:</strong></li>
        <p>Edit the values in the <code>honeypot.py</code> file as needed.</p>

        <li><strong>Start the honeypot:</strong></li>
        <pre><code>python honeypot.py /path/to/host_key.pem</code></pre>

        <li><strong>Monitor notifications:</strong></li>
        <p>Monitor your Telegram chat for notifications about login attempts.</p>
    </ol>

    <h2>Security Note</h2>

    <p>Ensure that the honeypot is operated in an isolated environment to minimize the risk of attacks. Use in compliance with applicable laws.</p>

    <h2>Contribution and Development</h2>

    <p>The repository is open for contributions and development. Users can submit suggestions, report issues, or create forks to make improvements.</p>

    <h2>License</h2>

    <p>The honeypot code is available under an open license (e.g., MIT License). See the <code>LICENSE</code> file for more information.</p>

    <h2>Support</h2>

    <p>For questions or support, you can create an issue in the GitHub repository.</p>

    <h2>Important Note</h2>

    <p>The honeypot should only be used in a controlled environment. Unauthorized attraction of attacks may violate the terms of service of internet service providers or laws.</p>

</body>

</html>
