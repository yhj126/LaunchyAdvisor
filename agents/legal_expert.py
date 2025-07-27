from agents.interface_base_expert import BaseExpert


class LegalExpert(BaseExpert):
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

        # Case 1: Storing EU customer data in the US
        if "store customer data in the us" in query_lower and "eu" in query_lower:
            # Under GDPR, storing EU customer data in US servers is restricted
            # unless proper safeguards (e.g., SCCs) are in place.
            compliant = False
            issues = ["GDPR restricts storing EU customer data in US servers without proper safeguards"]
            return {
                "compliant": compliant,
                "issues": issues,
                "reason": "GDPR restricts data storage outside EU without compliance."
            }

        # Case 2: Legal blockers for launching in Germany
        elif "legal blockers" in query_lower and "germany" in query_lower:
            # Germany follows GDPR and requires specific licenses to operate legally.
            licenses = self.context["licenses_required"].get("Germany", [])
            compliant = True if licenses else False
            issues = []
            if not compliant:
                issues.append("Missing required licenses for Germany.")
            return {
                "compliant": compliant,
                "issues": issues,
                "reason": f"Required licenses: {licenses}"
            }

        # Case 3: Privacy compliance for chatbots in Brazil
        elif "compliant" in query_lower and "privacy regulations in brazil" in query_lower:
            # Assume compliance with LGPD, Brazil's equivalent of GDPR.
            compliant = True
            return {
                "compliant": compliant,
                "issues": [],
                "reason": "Compliant with Brazil's LGPD privacy regulations."
            }

        # Case 4: Third-party cookies on Spanish marketing sites
        elif "third-party cookies" in query_lower and "spanish marketing site" in query_lower:
            allowed = self.context["cookie_regulations"].get("Spain", {}).get("third_party_cookies", False)
            compliant = allowed
            issues = []
            if not allowed:
                issues.append("Third-party cookies are prohibited in Spain without explicit user consent.")
            return {
                "compliant": compliant,
                "issues": issues,
                "reason": "Strict regularion of cookies in Spain."
            }

        # Case 5: License requirements in Canada
        elif "licenses" in query_lower and "canada" in query_lower:
            licenses = self.context["licenses_required"].get("Canada", [])
            compliant = True if licenses else False
            issues = []
            if not compliant:
                issues.append("Missing necessary licenses for operating in Canada.")
            return {
                "compliant": compliant,
                "issues": issues,
                "reason": f"Required licences: {licenses}"
            }

        # Default answer
        return {
            "compliant": False,
            "reason": "Query not recognized."
        }
