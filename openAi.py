import asyncio

import aiohttp
import backoff
import openai


class OpenAi:
    """
    OpenAIAPI class that uses the OpenAI API to generate explanations.
    """

    def __init__(self, api_key):
        """
        Constructor for OpenAIAPI class.
        :param api_key: OpenAI API key
        """
        self.api_key = api_key
        self.messages = [
            {"role": "system", "content": "Please summarize the slides and provide additional information."}
        ]

    async def generate_explanations(self, slides):
        """
        Generates explanations for the given slides. Uses the OpenAI API to generate explanations.
        :param slides: list of slides
        :return: list of explanations
        """
        async with self.get_openai_session() as session:
            responses = await asyncio.gather(
                *[self.get_response(session, slide) for slide in slides]
            )
        explanations = [response.choices[0].text.strip() for response in responses]
        return explanations

    async def get_openai_session(self):
        """
        Create an async session with the OpenAI API.
        :return: aiohttp.ClientSession
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with aiohttp.ClientSession(headers=headers) as session:
            yield session

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    async def get_response(self, session, slide):
        """
        Send a request to the OpenAI Chat API to get a response for the given slide.
        :param session: aiohttp.ClientSession
        :param slide: Slide object from the PowerPoint presentation.
        :return: explanation
        """
        messages = self.messages + [{"role": "user", "content": slide}]
        data = {
            "engine": "text-davinci-003",
            "prompt_messages": messages,
            "max_tokens": 50,
            "n": 1,
            "stop": None,
            "temperature": 0.7,
            "timeout": 60,
        }
        async with session.post("https://api.openai.com/v1/engines/davinci/completions", json=data) as response:
            response_data = await response.json()
        explanation = response_data["choices"][0]["text"].strip()
        return explanation
