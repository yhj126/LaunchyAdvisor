class LegalExpert:
    def __init__(self, context=None):
        """
        Simulated context about legal expert
        """
        self.context = context or {
            "gdpr_countries": ["Germany", "France", "Spain", "UK", "EU"],
            "restricted_regions": ["China", "Russia"],
            "data_storage_restrictions": {
                "EU": ["EU"],
                "US": ["No EU data allowed"],
            },
            "licenses_required": {
                "Canada": ["business_license", "data_handling_certification"],
                "Germany": ["business_license"],
            },
            "cookie_regulations": {
                "Spain": {"third_party_cookies": False},
                "US": {"third_party_cookies": True},
            }
        }

    def analyze(self, query: str) -> dict:
        query_lower = query.lower()

        # Default: the query can not be analyzed
        return {
            "compliant": False,
            "reason": "Query not recognized."
        }
