from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import html2text

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/save", methods=["POST"])
def save_html():
    data = request.get_json()

    if data and "html" in data and "url" in data:
        # Extract the URL
        url = data["url"]
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = False  # Retain links in Markdown format
        text_maker.ignore_images = True  # Skip images, or set to False to include them
        text_maker.ignore_emphasis = False  # Retain bold and italics
        markdown_content = text_maker.handle(data["html"])

        # Save the URL to a .txt file
        with open("llama/url.txt", "w") as file:
            file.write(url)

        with open("llama/page.md", "w") as file:
            file.write(markdown_content)

        return jsonify({"message": "URL saved successfully."}), 200
    else:
        return jsonify({"error": "Invalid data format"}), 400


if __name__ == "__main__":
    app.run(port=8000)
