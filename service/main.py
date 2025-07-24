import datetime
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from api.search import Search
from api.scrape import Scrape
from agents.summarizer import Summarizer
from agents.reportGenerator import ReportGenerator
from emailService.smtp import EmailService
from config import Settings
from payload import Payload

class Main(object):
    """
    Main class to handle the initialization and execution of the search service.
    """
    def __init__(self):
        """
        Initialize the Main class with the base URL and token for the search service.
        
        :param base_url: The base URL of the search service.
        :param token: The authentication token for the search service.
        """
        load_dotenv() # Load environment variables from a .env file
         # Initialize configuration settings
         # Initialize the search service with the configuration settings
        self.settings = Settings()
        self.search_service = Search(self.settings.SEARCH_URL, self.settings.SEARCH_KEY)
        self.scrape_service = Scrape(self.settings.SCRAPER_URL, self.settings.SCRAPER_KEY)
        self.summarizer_service = Summarizer()
        self.report_generator_service = ReportGenerator()
        self.email_service = EmailService(
            smtp_server=self.settings.SMTP_SERVER,
            smtp_port=int(self.settings.SMTP_PORT),
            username=self.settings.SMTP_USERNAME,
            password=self.settings.SMTP_PASSWORD,
        )
        self.config : dict = {
            "topic" : "News AI Agents",  # Default search topic,
            "email": "jpvilla1990@gmail.com",
        }

    def search(self):
        """
        Run the search operation with the provided query.

        return 'url', 'title', 'content', 'score'
        """
        results : list = []
        day : str = datetime.datetime.now().strftime("%d")
        week : str = datetime.datetime.now().strftime("%W")
        month : str = datetime.datetime.now().strftime("%m")
        year : str = datetime.datetime.now().strftime("%Y")
        for variant in [f"Today {day}-{month}-{year}", f"Week {week} {year}", f"Month {month}-{year}"]:
            results += self.search_service.search(self.config["topic"] + " " + variant)["results"]
        return results
    
    def scrape(self, url: str):
        """
        Run the scrape operation with the provided URL.

        :param url: The URL to scrape.
        :return: The scraped content.
        """
        return self.scrape_service.scrape(url)

    def pipeline(self):
        """
        Execute the search operation and return the results.

        :return: The results of the search operation.
        """
        # Run the search operation and get the results
        searchResults : list = self.search()
        # Scrape the content of each result
        scrapeResults : list = []
        urls : set = set()
        for result in searchResults:
            if "url" in result:
                if result["url"] not in urls:
                    urls.add(result["url"])
                else:
                    continue # Skip duplicate URLs
                # Scrape the content of the result URL
                try:
                    fullContent : str = self.scrape(result["url"])
                    summary : str = self.summarizer_service.summarize({
                        "url": result["url"],
                        "title": result.get("title", ""),
                        "content": result.get("content", ""),
                        "fullContent": fullContent,
                    })
                    scrapeResults.append({
                        "url": result["url"],
                        "title": result.get("title", ""),
                        "content": result.get("content", ""),
                        "score": result.get("score", 0),
                        "summary": summary,
                    })
                except Exception as e:
                    print(f"Error scraping {result['url']}: {e}")
                    continue

        with open("scrapeResults.json", "w", encoding="utf-8") as f:
            json.dump(scrapeResults, f, ensure_ascii=False, indent=4)

        report : str = self.report_generator_service.generateReport(scrapeResults)

        self.email_service.send_email(
            subject=self.config["topic"],
            html=report,
            from_addr=self.config["email"],
            to_addr=self.config["email"],
        )
        return report
    
app = FastAPI()
main = Main()

scheduler : BackgroundScheduler = BackgroundScheduler()

# This is your endpoint logic (refactored as a function)
def weekend_task():
    main.pipeline()

# Schedule the task to run every Saturday at 10:00 AM
scheduler.add_job(weekend_task, 'cron', day_of_week='sat', hour=18, minute=0)
scheduler.start()

@app.get("/")
def read_root():
    return {"message": "Welcome to the News AI Agents service!"}

@app.get("/pipeline", description="Trigger Pipeline to get and send News.")
def run_pipeline():
    """
    Run the main pipeline to search, scrape, summarize, and send the report via email.
    
    :return: The generated report.
    """
    main.pipeline()
    return {"message": "Pipeline executed successfully.", "report": "Report has been sent to the emails."}

@app.post("/config", description="Update configuration settings.")
def update_config(config: Payload):
    """
    Update the configuration settings for the service.
    
    :param config: A dictionary containing the new configuration settings.
    :return: The updated configuration settings.
    """
    main.config = {
        "topic": config.topic,
        "email": config.email
    }
    return {"message": "Configuration updated successfully.", "config": main.config}

if __name__ == "__main__":
    """
    Entry point for the application.
    """
    main = Main()
    result = main.pipeline()
