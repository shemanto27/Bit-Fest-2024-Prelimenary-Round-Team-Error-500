from phi.agent import Agent
from phi.model.groq import Groq

# Initialize chatbot agent
agent = Agent(
    model=Groq(id="ollama-3.3-70b-versatile"),
    tools=[],
    instructions=[
        "You are a cooking assistant. Recommend recipes based on the available ingredients and preferences."
    ],
)

def process_chat_input(user_input: str, available_ingredients: list) -> str:
    """Generate a response based on user input and available ingredients."""
    instruction = f"Available ingredients: {', '.join(available_ingredients)}.\n{user_input}"
    response = agent.run(instruction, stream=False)  
    return response
