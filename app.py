from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>DevOps Student Portal</title>
    </head>
    <body style="font-family: Arial; text-align: center;
                 margin-top: 100px;">

        <h1>Welcome to DevOps Student Portal</h1>

        <h2>Docker and Kubernetes Assignment</h2>

        <p>Application successfully deployed!</p>

        <p>Running using Python Flask, Docker and Kubernetes.</p>

    </body>
    </html>
    """

@app.route('/healthz')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
