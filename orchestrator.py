
class Orchestrator:
    def __init__(self, budget_expert, legal_expert, marketing_expert):
        self.budget_expert = budget_expert
        self.legal_expert = legal_expert
        self.marketing_expert = marketing_expert

    def analyze_query(self, query: str) -> list:
        query_lower = query.lower()
        experts = []

        # Keywords BudgetExpert
        budget_keywords = [
            "budget", "cost", "afford", "invest", "roi", "hire", "reduce", "minimal budget",
            "consolidate", "save costs", "growth move", "funds", "money", "pay", "expense"
        ]
        # Keywords LegalExpert
        legal_keywords = [
            "legal", "compliant", "compliance", "privacy", "gdpr", "regulation", "regulations",
            "license", "blockers", "law", "store customer data", "data protection", "privacy-first",
            "us", "eu", "canada", "brazil", "germany", "france", "uk", "india"
        ]
        # Keywords MarketingExpert
        marketing_keywords = [
            "marketing", "launch", "channel", "position", "message", "tagline", "social media",
            "campaign", "go-to-market", "gtm", "onboarding", "localize", "b2b", "saas",
            "announcement", "growth", "dual-brand", "freemium", "outsource", "southeast asia",
            "healthcare", "fintech"
        ]

        # Detect BudgetExpert need
        if any(kw in query_lower for kw in budget_keywords):
            experts.append("budget")

        # Detect LegalExpert need
        if any(kw in query_lower for kw in legal_keywords):
            experts.append("legal")

        # Detect MarketingExpert need
        if any(kw in query_lower for kw in marketing_keywords):
            experts.append("marketing")

        # If there is no expert call them all by default
        if not experts:
            experts = ["budget", "legal", "marketing"]

        # Evitar duplicados (por si acaso)
        return list(set(experts))


    def orchestrate(self, query: str) -> dict:
        experts = self.analyze_query(query)

        responses = {}

        if 'budget' in experts:
            responses['budget'] = self.budget_expert.analyze(query)
        if 'legal' in experts:
            responses['legal'] = self.legal_expert.analyze(query)
        if 'marketing' in experts:
            responses['marketing'] = self.marketing_expert.analyze(query)

        final_response = self.synthesize_responses(responses)
        return final_response

    def synthesize_responses(self, responses: dict) -> dict:

        # Extract info from each expert, con fallback por si no viene respuesta
        budget_resp = responses.get("budget", {})
        legal_resp = responses.get("legal", {})
        marketing_resp = responses.get("marketing", {})

        # Construir mensajes parciales
        budget_summary = "Presupuesto suficiente." if budget_resp.get("feasible",
                                                                      False) else "Presupuesto insuficiente."
        if "reason" in budget_resp:
            budget_summary += f" ({budget_resp['reason']})"

        legal_summary = "Cumple con regulaciones legales." if legal_resp.get("compliant",
                                                                             False) else "Existen problemas legales."
        if "issues" in legal_resp and legal_resp["issues"]:
            legal_summary += " Problemas detectados: " + ", ".join(legal_resp["issues"])

        marketing_summary = "La estrategia de marketing es adecuada." if marketing_resp.get("strategy_fit",
                                                                                            False) else "La estrategia de marketing necesita revisión."
        if "recommended_channels" in marketing_resp:
            channels = ", ".join(marketing_resp["recommended_channels"])
            marketing_summary += f" Canales recomendados: {channels}."

        # Crear resumen general (puedes mejorarlo con un LLM para texto natural)
        summary = (
            f"Análisis financiero: {budget_summary}\n"
            f"Aspectos legales: {legal_summary}\n"
            f"Estrategia de marketing: {marketing_summary}\n"
        )

        # Devolver JSON con resumen y detalles
        return {
            "summary": summary,
            "details": responses
        }
