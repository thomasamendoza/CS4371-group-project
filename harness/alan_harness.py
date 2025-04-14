import dataclasses
import json

import requests

from constant.prompt_injection import PromptInjection


@dataclasses.dataclass
class WriteSonicHarness:
    name: str = "write_sonic"
    site_url: str = "https://app.writesonic.com/"
    application_document: str = "Writesonic is an AI writer that creates SEO-friendly content for blogs, Facebook ads, Google ads, and Shopify for free."

    def run_harness(self, prompt_injection: PromptInjection):
        url = "https://api.writesonic.com/v1/botsonic/botsonic/generate/780dc6b4-fbe9-4d5e-911c-014c9367ba32/sse"
        params = {
            "data": f'{"question":"{prompt_injection.get_attack_prompt()}","token":"9adac12a-e776-4ddc-8588-26bda6cbcbf0","chat_id":"47acedd6-6c64-4423-8a5a-587af61a2224"}'
        }

        headers = {
            "accept": "text/event-stream",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "Referer": "https://app.writesonic.com/",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        }

        response = requests.get(url, params=params, headers=headers)

        return response.text