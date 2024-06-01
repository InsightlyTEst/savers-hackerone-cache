from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

# Define the headers
headers = {
    "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.savers.co.uk/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Connection": "close"
}


@app.route('/make_request', methods=['GET'])
def make_request():
    url = request.args.get('url', None)
    if url is None:
        return "Error: URL not provided in request."

    response = requests.get(url, headers=headers)
    # Step 4: Extract lines containing "gaSessionId:"
    filtered_lines = [line for line in response.text.split('\n') if "gaSessionId:" in line]

    # Step 5: Return the filtered lines
    return jsonify(filtered_lines)

if __name__ == "__main__":
    app.run(debug=True)
