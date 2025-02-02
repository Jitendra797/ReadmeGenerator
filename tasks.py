from crewai import Task
from agents import file_reader


file_reader_task = Task(
        description="Generate a basic README for the Hello world project.",
        agent=file_reader,
        expected_output="A basic README file for the Hello world project.",
       
    )

readme_generator_task  = Task(
    name="",
    description="",
    agent=readme_generator,
    expected_output="",
    tools= []
)
