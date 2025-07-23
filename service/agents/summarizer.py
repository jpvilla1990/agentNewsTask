from openai import OpenAI

class Summarizer(OpenAI):
    """
    Summarizer class to handle summarization operations.
    """
    def __init__(self):
        """
        Initialize the Summarizer class with the base URL of the OpenAI service.
        """
        super().__init__()

    def summarize(self, document: dict) -> str:
        """
        Perform a summarization operation with the given text.
        """
        title : str = document.get("title", "")
        summary : str = document.get("content", "")
        html = document.get("fullContent", "")

        text = f"URL: {document['url']}\nTitle: {title}\nSummary: {summary}\nHTML Content:\n{html[:2000]}..."  # truncate HTML

        final_prompt = (
            "You are a reporter assistant. Summarize the key points from the following webpages, put the title, source, link, date\n\n"
            f"{text}\n\n"
            "Give me a concise summary of the major themes, facts, and insights, but do not make it too short that important facts are lost.\n"
            "do not talk in third person, just narrate the same story"
            "if there are images or videos extract the links in a list, if not just do not mention them"
            "the output should be a json with the following structure:\n"
            "{\n"
            "  'title': 'Title of the document',\n"
            "  'source': 'Source of the document',\n"
            "  'link': 'Link to the document',\n"
            "  'date': 'Date of the document',\n"
            "  'summary': 'Concise summary of the document',\n"
            "  'media': ['List of media links if any']\n"
            "}\n\n"
            "Make sure to include all the relevant information in the summary, and format it as a JSON object.\n"
            "If the document does not contain any relevant information, return an empty JSON object: {}"
        )

        response = self.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert summarizer."},
                {"role": "user", "content": final_prompt}
            ]
        )
        return response.choices[0].message.content
