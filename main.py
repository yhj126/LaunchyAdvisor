from orchestrator import Orchestrator
from agents.budget_expert import BudgetExpert
from agents.legal_expert import LegalExpert
from agents.marketing_expert import MarketingExpert


def main():
    print("Welcome to LaunchyAdvisor")
    #TODO Incorporate ollama to answer the questions with the proper prompt
    #ai_option=input("If you want to use Ollama(must be running) press 1 else press 0")
    budget_expert = BudgetExpert()
    legal_expert = LegalExpert()
    marketing_expert = MarketingExpert()

    query = input("Ask a question about the company:\n> ")

    print("\nAnalyzing...\n")


    orc = Orchestrator(budget_expert=budget_expert, legal_expert=legal_expert, marketing_expert=marketing_expert)
    result = orc.orchestrate(query)

    print("Answer:\n")
    from pprint import pprint
    pprint(result)

if __name__ == "__main__":
    main()
