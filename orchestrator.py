
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

        # Remove duplicates
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

        # Extract info from each expert, with fallback in case there's no response
        budget_resp = responses.get("budget", {})
        legal_resp = responses.get("legal", {})
        marketing_resp = responses.get("marketing", {})

        # Build partial summaries
        budget_summary = "Budget is sufficient." if budget_resp.get("feasible", False) else "Budget is insufficient."
        if "reason" in budget_resp:
            budget_summary += f" ({budget_resp['reason']})"

        legal_summary = "Legally compliant." if legal_resp.get("compliant", False) else "Legal issues detected."
        if "issues" in legal_resp and legal_resp["issues"]:
            legal_summary += " Issues found: " + ", ".join(legal_resp["issues"])

        marketing_summary = "Marketing strategy is adequate." if marketing_resp.get("strategy_fit", False) else "Marketing strategy needs review."
        if "recommended_channels" in marketing_resp:
            channels = ", ".join(marketing_resp["recommended_channels"])
            marketing_summary += f" Recommended channels: {channels}."

        # Build overall summary (can be improved using an LLM for natural language)
        summary = (
            f"Financial analysis: {budget_summary}\n"
            f"Legal aspects: {legal_summary}\n"
            f"Marketing strategy: {marketing_summary}\n"
        )

        # Return JSON structured response
        return {
            "summary": summary,
            "details": responses
        }
