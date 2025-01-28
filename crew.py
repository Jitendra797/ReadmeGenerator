from agents import file_reader
from tasks import file_reader_task
from crewai import Crew,Process


crew = Crew(
    agents=[file_reader],
    tasks=[file_reader_task],
    process=Process.sequential
)

crew.kickoff()
