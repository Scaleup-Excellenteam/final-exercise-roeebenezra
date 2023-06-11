import asyncio
import backoff
import openai


class OpenAIAPI:
    """
    OpenAIAPI class that uses the OpenAI API to generate explanations.
    """

    def __init__(self, api_key):
        '''
        Constructor for OpenAIAPI class.
        :param api_key: OpenAI API key
        '''
        openai.api_key = api_key
        self.messages = [
            {"role": "system", "content": "Please summarize the slides and provide additional information."}
        ]

    async def generate_explanations(self, slides):
        """
        Generates explanations for the given slides. Uses the OpenAI API to generate explanations.
        :param slides: list of slides
        :return: list of explanations
        """
        explanations = await asyncio.gather(*[self.get_response(slide) for slide in slides])
        return explanations

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    async def get_response(self, slide):
        """
        Send a request to the OpenAI Chat API to get a response for the given slide.
        :param slide: Slide object from the PowerPoint presentation.
        :return: explanation
        """
        messages = self.messages + [{"role": "user", "content": slide}]
        response = await openai.Completion.create(
            engine="text-davinci-003",
            prompt_messages=messages,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
            timeout=60,
        )
        explanation = response.choices[0].text.strip()
        return explanation
