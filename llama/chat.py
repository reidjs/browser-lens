import requests
import argparse


url = "http://localhost:11434/api/chat"
page_context = ""
page_url = ""
url_path = "llama/url.txt"
file_path = "llama/url.txt"


def load_url():
    global page_url
    with open(url_path, "r") as file:
        page_url = file.read()


def load_page():
    global page_context
    with open(url_path, "r") as file:
        page_context = file.read()


def initialize_conversation_with_page_url():
    return [
        {
            "role": "user",
            "content": f"I am going to ask you questions based on this URL: '{page_url}', please ONLY respond with information from the given page.",
        },
    ]


def initialize_conversation_with_page_context():
    return [
        {
            "role": "user",
            "content": f"I am going to ask you questions based on this URL: '{page_context}', please ONLY respond with information from the given page.",
        },
    ]


# Function to handle a single interaction
def llama3_with_url(prompt):
    # Reset the conversation history for each new prompt
    conversation_history = initialize_conversation_with_page_url()
    conversation_history.append({"role": "user", "content": prompt})

    data = {
        "model": "llama3",
        "messages": conversation_history,
        "stream": False,
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)

    model_reply = response.json()["message"]["content"]

    return model_reply


def llama3_with_page_context(prompt):
    conversation_history = initialize_conversation_with_page_context()
    conversation_history.append({"role": "user", "content": prompt})

    data = {
        "model": "llama3",
        "messages": conversation_history,
        "stream": False,
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)

    model_reply = response.json()["message"]["content"]

    return model_reply


load_url()
load_page()


def prompt(prompt, use_url):
    if use_url:
        print(f"Querying current page URL: {page_url}\n")
        print(f"Ollama: {llama3_with_url(prompt)}")
    else:
        print(f"Querying the current page context for: {page_url}\n")
        print(f"Ollama: {llama3_with_page_context(prompt)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ollama on your chrome context")
    parser.add_argument("prompt", type=str, help="your prompt.")
    parser.add_argument(
        "-u",
        "--url",
        action="store_true",
        help="Use the URL directly",
    )

    args = parser.parse_args()
    prompt(args.prompt, args.url)
