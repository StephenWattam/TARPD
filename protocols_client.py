

from requests_oauthlib import OAuth2Session
import json


class ProtocolsClient:

    CLIENT_ID = "pr_live_id_44618af55593f3fcf4500ea8874be16c"
    CLIENT_SECRET = "pr_live_sc_4b69fc14ca0517bb38359eb2d6223637"
    REDIRECT_URL = "https://example.com/protocols_api"

    AUTHORIZE_URL = "https://www.protocols.io/api/v3/oauth/authorize"
    TOKEN_URL = "https://www.protocols.io/api/v3/oauth/token"

    def __init__(self) -> None:

        scope = "readwrite"
        self.oauth = OAuth2Session(ProtocolsClient.CLIENT_ID, redirect_uri="localhost", scope=scope)
        authorization_url, state = self.oauth.authorization_url(ProtocolsClient.AUTHORIZE_URL,
                                                           redirect_url=ProtocolsClient.REDIRECT_URL)

        print('Please go to the following link and log in: %s' % authorization_url)
        authorization_response = input('Enter the full callback URL: ')

        self.oauth.fetch_token(ProtocolsClient.TOKEN_URL, client_secret=ProtocolsClient.CLIENT_SECRET,
                          include_client_id=True, authorization_response=authorization_response)

        # TODO: refreshing of tokens.  This is probably an unnecessary feature for the use-cases
        #       of this proof-of-concept.

    def get_profile(self) -> dict:

        return self.get("https://www.protocols.io/api/v3/session/profile")

        # Now do things with the oauth client
        import code; code.interact(local=locals())

    def get_protocol(self, id: str, format="markdown"):
        """Return a protocol object"""

        return self.get(f"https://www.protocols.io/api/v4/protocols/{id}",
                        params={'last_version': 1, 'content_format': format})

    def get_protocol_steps(self, id: str, format="markdown"):
        """Return a protocol object"""

        return self.get(f"https://www.protocols.io/api/v4/protocols/{id}/steps",
                        params={'last_version': 1, 'content_format': format})

    def get_run(self, id: str) -> dict:

        return self.get(f"https://www.protocols.io/api/v3/records/{id}",
                        params={'with_protocol': 1, 'with_comments': 1, 'as_draft': 1})

    def get(self, *args, **kwargs) -> dict:
        """Get with JSON post-processing"""

        response = self.oauth.get(*args, **kwargs)
        response.raise_for_status()
        return json.loads(response.text)

    def post(self, *args, **kwargs) -> dict:
        """Get with JSON post-processing"""

        response = self.oauth.get(*args, **kwargs)
        response.raise_for_status()
        return json.loads(response.text)