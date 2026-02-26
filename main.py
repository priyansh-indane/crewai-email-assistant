import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# 1. Load your API keys from the .env file
load_dotenv()

# 2. Define the Gemini Model
# Ensure your .env has GEMINI_API_KEY=your_key_here
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7
)

# 3. Define the Agent
email_assistant = Agent(
    role="Email Assistant Agent",
    goal="Improve emails and make them sound clear and professional",
    backstory="You are a highly experienced specialist in corporate communication and professional writing.",
    verbose=True,
    llm=gemini_llm
)

# 4. Define the Task
original_email = "hello just wanted to tell that there is still some work left iam working on it thank you."

email_task = Task(
    description=f"Take the following email and rewrite it into a professional version: {original_email}",
    agent=email_assistant,
    expected_output="A professionally written email with proper formatting and a clear subject line."
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
