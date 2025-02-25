from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM
import os
from dotenv import load_dotenv

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ContentAgent():
	"""ContentAgent crew for content creation"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self):
		# Load environment variables
		load_dotenv()
		
		# Initialize LLM configurations
		
		# 1. OpenAI (commented out)
		# self.llm = LLM(
		#     model="gpt-4o-mini",
		#     api_key=os.getenv("OPENAI_API_KEY")
		# )

		# 2. OpenRouter (commented out)
		# self.llm = LLM(
		#     model="deepseek/deepseek-r1:free",
		#     base_url="https://openrouter.ai/api/v1",
		#     api_key=os.getenv("OPENROUTER_API_KEY")
		# )

		# 3. Local Ollama configuration
		self.llm = LLM(
			model="ollama/deepseek-r1:8b",
			base_url="http://localhost:11434"
		)

	@agent
	def content_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['content_creator'],
			verbose=True,
			llm=self.llm
		)

	@agent
	def editor(self) -> Agent:
		return Agent(
			config=self.agents_config['editor'],
			verbose=True,
			llm=self.llm
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def content_creation_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_creation_task']
		)

	@task
	def editing_task(self) -> Task:
		return Task(
			config=self.tasks_config['editing_task'],
			context=[self.content_creation_task()]  # Fixed: Call the method to get the task
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ContentAgent crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
