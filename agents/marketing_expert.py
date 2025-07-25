from agents.interface_base_expert import BaseExpert


class MarketingExpert(BaseExpert):
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

        # Query about audience
        for audience, channels in self.context["audience_preferences"].items():
            if audience.lower() in query_lower:
                return {
                    "recommendation": f"Focus on channels: {', '.join(channels)}",
                    "reason": f"Target audience '{audience}' prefers those channels."
                }

        # Query about region
        for region, channels in self.context["channels_by_region"].items():
            if region.lower() in query_lower:
                return {
                    "recommendation": f"Prioritize channels in {region}: {', '.join(channels)}",
                    "reason": f"Popular channels in {region} based on past campaigns."
                }

        # Query about tagline
        if "tagline" in query_lower or "slogan" in query_lower:
            return {
                "recommendation": "Try something like: 'Your data, your rules – analytics with privacy in mind.'",
                "reason": "Taglines should reflect core value proposition and differentiation."
            }

        # Query about localization
        if "launch" in query_lower or "go-to-market" in query_lower or "localize" in query_lower:
            return {
                "recommendation": "Adapt messaging and onboarding to local culture and language.",
                "reason": "Localization improves engagement and trust in regional markets."
            }

        # Default: the query can not be analyzed
        return {
            "recommendation": "Not analyzed",
            "reason": "Query not recognized."
        }
