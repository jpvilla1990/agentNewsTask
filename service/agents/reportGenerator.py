import json
from openai import OpenAI

class ReportGenerator(OpenAI):
    """
    ReportGenerator class to handle summarization operations.
    """
    def __init__(self):
        """
        Initialize the Summarizer class with the base URL of the OpenAI service.
        """
        super().__init__()

    def generateReport(self, documents: dict) -> str:
        """
        Perform a summarization operation with the given text.
        """
        documentsSerialized = json.dumps(documents, ensure_ascii=False)

        final_prompt = (
            "You are a new report assistant. Create a nice HTML report to send by email based on the following serialized json\n\n"
            f"{documentsSerialized}\n\n"
            "Order putting on top those reports with higher impact, if there are images of videos render them in the report.\n"
            "The report should be a valid HTML document with a title, a header, and a body.\n"
            "The title should be 'Weekly Report', the header should contain the date and a brief description of the report, and the body should contain the content of the reports.\n"
            "Make sure to include all the relevant information in the report, and format it as a valid HTML document.\n"
            "If the document does not contain any relevant information, return an empty HTML document: <html><body></body></html>"
        )

        response = self.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert report generator."},
                {"role": "user", "content": final_prompt}
            ]
        )
        return response.choices[0].message.content