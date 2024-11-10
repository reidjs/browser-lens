Similar to:
https://github.com/andrewnguonly/Lumos

1. load unpacked chrome-extension into chrome
2. install ollama 
3. start virtual envs and install all python dependencies
4. run server `python server/server.py`
5. open chrome tab and make sure extension is active



To run on mac, use ollama
https://www.llama.com/docs/llama-everywhere/running-meta-llama-on-mac/

`ollama run llama3`

seems to always work:
https://example.com
"am i allowed to use this content?"

sending ONLY the URL works for 
https://en.wikipedia.org/wiki/Parthenium_integrifolium
wikipedia is tricky, some stuff it's good at like telling you what the page is about,  but it seems to make up a lot of details

https://www.iana.org/about
"what is the mission statement 

sending ONLY the markdown content works for
"https://www.iana.org/help/example-domains"
"what rfcs are mentioned on this page"

"https://www.iana.org/help/example-domains"
"what rfcs are mentioned on this page"

https://paulgraham.com/simply.html
"summarize this"

Turns out websockets are pretty hard to integrate into a chrome extension. Keeping this focused on the terminal for now. 