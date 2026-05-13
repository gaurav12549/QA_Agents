from setuptools import setup, find_packages

setup(
    name="qa-agents",
    version="0.1.0",
    description="AI-powered QA news research agent with podcast generation",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "crewai>=0.30.0",
        "crewai-tools>=0.1.0",
        "python-dotenv>=1.0.0",
        "langchain-community>=0.2.0",
        "langchain-ollama>=0.1.0",
        "tavily-python>=0.3.0",
        "pyttsx3>=2.90.0",
    ],
    entry_points={
        "console_scripts": [
            "qa-podcast=App:main",
        ],
    },
)