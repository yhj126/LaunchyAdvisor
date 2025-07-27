from agents.interface_base_expert import BaseExpert


class BudgetExpert(BaseExpert):
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
        expected_costs = self.context["expected_costs"]
        available_budget = self.context["total_budget"] - self.context["allocated_budget"]

        matched_cost = None
        estimated_cost = 0

        #Expected cost
        for cost_name, cost_value in expected_costs.items():
            if cost_name.replace("_", " ") in query_lower:
                matched_cost = cost_name
                estimated_cost = cost_value
                break

        if matched_cost:
            if estimated_cost <= available_budget:
                return {
                    "feasible": True,
                    "reason": f"The cost for '{matched_cost}' ({estimated_cost}) fits in the available budget ({available_budget})."
                }
            else:
                return {
                    "feasible": False,
                    "reason": f"The cost for '{matched_cost}' ({estimated_cost}) exceeds the available budget ({available_budget})."
                }

        # Default: the query can not be analyzed
        return {
            "feasible": False,
            "reason": "Query not recognized."
        }
