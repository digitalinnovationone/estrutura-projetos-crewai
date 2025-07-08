from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ConfiguracaoTarefasPapeisCrewai():
    """ConfiguracaoTarefasPapeisCrewai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def agente_especialista_didatico(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_especialista_didatico'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def agente_criador_exercicios(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_criador_exercicios'],  # type: ignore[index]
            verbose=True
        )

    @task
    def tarefa_criar_resumo_didatico(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_criar_resumo_didatico'],  # type: ignore[index]
        )

    @task
    def tarefa_gerar_exercicios(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_gerar_exercicios'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ConfiguracaoTarefasPapeisCrewai crew"""
        return Crew(
            agents=self.agents,    # Automatically created by the @agent decorator
            tasks=self.tasks,      # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
