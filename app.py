#!/usr/bin/python3
from flask import Flask, render_template, request
import socket
import pyfiglet
from termcolor import colored

app = Flask(__name__)

# Banner
banner = pyfiglet.figlet_format("Domain to IP Easily")

@app.route('/')
def home():
    # Display the home page with the banner
    return render_template('index.html', banner=banner)

@app.route('/get_ip', methods=['POST'])
def get_ip():
    try:
        # Get the domain from the form
        domain = request.form.get('domain')
        ip = socket.gethostbyname(domain)
        return render_template('index.html', banner=banner, domain=domain, ip=ip, success=True)
    except Exception as e:
        # Handle any errors
        return render_template('index.html', banner=banner, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
