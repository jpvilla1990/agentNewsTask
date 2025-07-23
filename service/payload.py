from pydantic import BaseModel, Field

class Payload(BaseModel):
    """
    Represents the payload for the agent news task.
    """
    email: str = Field(..., description="Email address to send the report to")
    topic: str = Field(..., description="Topic of the news to search for")