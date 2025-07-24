class MarketingExpert:
    def __init__(self, context=None):
        """
        Simulated context about marketing expert
        """
        self.context = context or {
            "channels_by_region": {
                "Europe": ["LinkedIn", "Twitter", "Email"],
                "APAC": ["WeChat", "LINE", "Facebook"],
                "LATAM": ["Instagram", "Facebook", "WhatsApp"],
            },
            "audience_preferences": {
                "B2B SaaS founders": ["LinkedIn", "Tech blogs"],
                "HR teams": ["LinkedIn", "Webinars"],
                "Healthcare sector": ["Facebook", "Instagram"],
                "Fintech sector": ["LinkedIn", "Twitter"],
            },
            "budget": 30000
        }

    def analyze(self, query: str) -> dict:
        query_lower = query.lower()

        # Default: the query can not be analyzed
        return {
            "recommendation": "Not analyzed",
            "reason": "Query not recognized."
        }
