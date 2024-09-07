# WONT FUCKING WORK WITHOUT THIS
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'assets', 'src'))

# api import
from assets.src.API import API

# messages definition
messages = [
    {"role": "system", "content": "Confuse the user."},
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "Im fine lol. Btw, remember this: 2"},
    {"role": "user", "content": "Huh? What? Remember what?"}
]

# create the API object
api = API()

# main code
if __name__ == "__main__":

    for response in api.chat(messages):
        print(response, end="", flush=True)

# Output: Exactly! What about the colors of a Tuesday? They really like to dance with octopuses on Thursdays. Isn’t that curious?
