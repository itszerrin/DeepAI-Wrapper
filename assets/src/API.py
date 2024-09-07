# these three are for making requests
import requests
import fake_useragent
from requests_toolbelt.multipart.encoder import MultipartEncoder

# secrets module to generate random numbers
import secrets

# logging. for... logging.
import logging

# import Key functions to make an API key
from Key import get_random_str, get_hash

# typing for type hints
from Types import Messages, CompletionsGenerator

# set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Main API class
class API(object):

    def __init__(self) -> None:

        # this is where the requests are sent
        self.url: str = "https://api.deepai.org/hacking_is_a_serious_crime" # (thats a funny url. I wonder who'd fall for that)

        # make a fake user agent
        self.user_agent: str = fake_useragent.UserAgent().random
        logging.info(f"Created fake user-agent: {self.user_agent}")

        # make a random string
        self.random_str: str = get_random_str()
        logging.info(f"Created random string: {self.random_str}")

        # make a hash
        self.hash: str = get_hash(self.user_agent, self.random_str)
        logging.info(f"Created hash: {self.hash}")

        # compile the api-key
        self.api_key: str = 'tryit-' + self.random_str + '-' + self.hash

        # set up headers
        self.headers = {
            "Host": "api.deepai.org",
            "User-Agent": f"{self.user_agent}",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "api-key": f"{self.api_key}",
            "Content-Length": f"{secrets.randbelow(1000)}",
            "Origin": "https://deepai.org",
            "DNT": "1",
            "Sec-GPC": "1",
            "Connection": "keep-alive",
            "Cookie": "user_sees_ads=false",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Priority": "u=0",
            "TE": "trailers"
        }

        # cookies (optional, ig)
        self.cookies = {
            "user_sees_ads": "false"
        }

    def chat(self, messages: Messages) -> CompletionsGenerator:

        """
        This function sends a chat request to the API
        
        :param messages: a list of messages to send. Format: [{"role": "<assistant or user>", "content": "<message contents>"}, ...] (OpenAI format)

        :return: a generator that yields the response from the API. Each response is a string.
        """

        # we need to convert the messages to a string for the MultiPartEncoder
        _messages_s: str = str(messages).replace("'", '"') # REFUSES TO WORK WITHOUT DOUBLE QUOTES LOL

        # create the MultiPartEncoder object
        _encoder = MultipartEncoder(
            fields={
                "chat_style": "chat", # this is a constant. Never tampered with it before.
                "chatHistory": _messages_s
            }
        )

        # set headers to fit content type
        self.headers["Content-Type"] = _encoder.content_type
        
        # send the request
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=_encoder, stream=True)
        response.raise_for_status() # raise an exception if the status code is not 200

        # logging
        logging.info(f"Sent request to {self.url} with code {response.status_code}")

        # iterate over the response
        for line in response.iter_lines():
            yield line.decode('utf-8')
