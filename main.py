import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from email_tool import MyCustomTool  
# 1. Load your API keys from the .env file
load_dotenv()

# 2. Define the Gemini Model
gemini_llm = LLM(
    model="gpt-4o-mini",
    temperature=0.7
)

email_tool = MyCustomTool()  

# 3. Define the Agent
email_assistant = Agent(
    role="Email Assistant Agent",
    goal="Improve emails and make them sound clear and professional",
    backstory="You are a highly experienced specialist in corporate communication and professional writing.",
    verbose=True,
    llm=gemini_llm,
    tools=[email_tool]  
)

# 4. Define the Task
original_email = "hello just wanted to tell that there is still some work left iam working on it thank you."

email_task = Task(
    description=f"Take the following email and rewrite it into a professional version: {original_email}. "
                f"After rewriting, use the email sender tool to send the rewritten email.",  
    agent=email_assistant,
    expected_output="A professionally written email with proper formatting and a clear subject line. "
                    "Confirm that the email was sent successfully."
)

# 5. Assemble the Crew
crew = Crew(
    agents=[email_assistant],
    tasks=[email_task],
    verbose=True
)

# 6. Kickoff the process
if __name__ == "__main__":
    print("## Crew is starting the task...")
    result = crew.kickoff()
    
    print("\n\n########################")
    print("## HERE IS YOUR REWRITTEN EMAIL:")
    print("########################\n")
    print(result)

    email_tool.run(str(result))  
    print("Email sent successfully!")