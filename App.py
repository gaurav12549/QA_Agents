import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
from dotenv import load_dotenv

# Disable CrewAI telemetry for faster execution
os.environ["CROWD_DISABLE_TRACING"] = "true"

from crewai import Agent, Task, Crew, Process
from crewai_tools import TavilySearchTool
import pyttsx3

# Load env
load_dotenv()

# Create output folder
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Clean output folder before each run
for file in os.listdir(output_folder):
    file_path = os.path.join(output_folder, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"Error cleaning {file_path}: {e}")

# Tool
search_tool = TavilySearchTool(
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)

# Agent 1: Research Agent
researcher = Agent(
    role='AI News Scout',
    goal='Use tavily_search tool to find and report the latest AI testing news',
    backstory='Use the tavily_search tool to search the web. Never fabricate results.',
    tools=[search_tool],
    llm="ollama/llama3.1",
    verbose=False
)

# Agent 2: Podcast Writer Agent
podcast_writer = Agent(
    role='Podcast Script Writer',
    goal='Transform AI news into engaging podcast scripts using ONLY the provided news data',
    backstory='You are an experienced podcast scriptwriter. Convert ONLY the news data provided by the researcher into a conversational podcast script. Do NOT invent any news stories.',
    llm="ollama/llama3.1",
    verbose=False
)

# Task 1: Research News
research_task = Task(
    description="Use tavily_search tool to find 5 latest AI testing news articles. Return the EXACT results from the search - do not add, modify, or invent any news items.",
    expected_output="Raw list of 5 AI testing news items with titles, sources, and dates from the search tool only",
    agent=researcher,
    timeout=240
)

# Task 2: Create Podcast Script
podcast_task = Task(
    description="Take the raw research results from the previous task and convert them into a podcast script. Use EXACTLY the news items provided - do not add new stories or modify the facts.",
    expected_output="A podcast script using ONLY the 5 news items from the researcher",
    agent=podcast_writer,
    context=[research_task],
    timeout=240
)

# Crew with sequential process
crew = Crew(
    agents=[researcher, podcast_writer],
    tasks=[research_task, podcast_task],
    process=Process.sequential
)

# Function to convert text to audio
def text_to_audio(script, output_path):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 1.0)  # Volume
    engine.save_to_file(script, output_path)
    engine.runAndWait()
    print(f"Audio saved to: {output_path}")

# Run
if __name__ == "__main__":
    print("Running research and script generation...")
    result = crew.kickoff()

    # Convert script to audio
    print("\nConverting script to audio...")
    audio_path = os.path.join(output_folder, "podcast_audio.mp3")
    text_to_audio(str(result), audio_path)

    print("\n=== PROCESS COMPLETE ===")
    print(f"Audio saved to: {audio_path}")