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
            "You are a research assistant. Summarize the key points from the following webpages.\n\n"
            f"{text}\n\n"
            "Give me a concise summary of the major themes, facts, and insights."
        )

        response = self.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert summarizer."},
                {"role": "user", "content": final_prompt}
            ]
        )
        return response.choices[0].message.content
