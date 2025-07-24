class BudgetExpert:
    def __init__(self, context=None):
        """
        Mock with the estimated budget for this agent.
        """
        self.context = context or {
            "total_budget": 100000,
            "allocated_budget": 40000,
            "monthly_expenses": 10000,
            "expected_costs": {
                "paid_campaign_q4": 20000,
                "senior_ml_engineer_monthly": 15000,
                "product_research": 15000,
            }
        }

    def analyze(self, query: str) -> dict:
        """
        Analyze the query.
        """
        query_lower = query.lower()

        # Default: the query can not be analyzed
        return {
            "feasible": False,
            "reason": "Query not recognized."
        }
