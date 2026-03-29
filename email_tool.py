import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    body: str = Field(
        ..., 
        description="The professionally rewritten email to be sent to the receiver"
    )


class MyCustomTool(BaseTool):
    name: str = "email sender tool"
    description: str = (
        "Sends the rewritten professional email to the receiver. "
        "Use this tool after rewriting the email."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, body: str) -> str:
        sender = "lakesun552@gmail.com"
        receiver = "indanepriyansh@gmail.com"
        password = "xryiffmslizzdfom"  

        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = "Rewritten Professional Email"  

        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, msg.as_string())
            return "Email sent successfully!"
        except Exception as e:
            return f"Failed to send email: {str(e)}"