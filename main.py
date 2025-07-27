import json

import requests

from orchestrator import Orchestrator
from agents.budget_expert import BudgetExpert
from agents.legal_expert import LegalExpert
from agents.marketing_expert import MarketingExpert

def call_ollama(prompt: str, model="deepseek-r1"):
    """
    Send a prompt to the local Ollama instance and get a natural language response.
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json().get("response", "No response from model.")
    except Exception as e:
        return f"Error connecting to Ollama: {e}"

def main():
    print("Welcome to LaunchyAdvisor")
    ai_option=input("If you want to use Ollama(must be running) press 1 else press 0\n")
    budget_expert = BudgetExpert()
    legal_expert = LegalExpert()
    marketing_expert = MarketingExpert()

    query = input("Ask a question about the company:\n> ")

    print("\nAnalyzing...\n")


    orc = Orchestrator(budget_expert=budget_expert, legal_expert=legal_expert, marketing_expert=marketing_expert)
    result = orc.orchestrate(query)

    #Easier to be understood by the ollama model
    structured_json = json.dumps(result, indent=2)
    natural_prompt = (
        "Please summarize the following structured information in a friendly and easy-to-understand way, "
        "for someone without technical knowledge. Only mention areas that are actually present in the data. "
        "Do not add extra explanations or assumptions. Be concise but clear.\n\n"
        f"{structured_json}"
    )

    natural_response = call_ollama(natural_prompt)

    print("Answer:\n")
    from pprint import pprint
    pprint(result)

    if ai_option == "1":
        print("Natural laguage prompt:")
        print("-------")
        print(natural_response)



if __name__ == "__main__":
    main()
