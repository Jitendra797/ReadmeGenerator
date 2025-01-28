import os
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
)
from crewai import Agent
from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    verbose = True,
    temperature = 0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY")
    
)

print(llm)

# file_reader = Agent(
#     role="File System Accessor",
#     goal="Efficiently and accurately read files from the local system.",
#     backstory="I am a seasoned system administrator with expertise in file system navigation and data retrieval.",
#     llm=llm, 
#     verbose=True, 
#     memory=True, 
#     tools=[], 
#     allow_delegation=False, 
# )


# readme_generator = Agent(
#     role="Documentation Writer",
#     goal="Generate comprehensive and informative README files that effectively communicate project information to users.",
#     backstory="I am an experienced technical writer with a deep understanding of software development best practices and documentation standards.",
#     llm=llm, 
#     verbose=True, 
#     memory=True, 
#     tools=[CodeReviewTool(), FileReadTool(), MarkdownTool()], 
#     allow_delegation=True, 
# )