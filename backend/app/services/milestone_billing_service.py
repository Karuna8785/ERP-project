'''Contract Milestone Progress Invoicing.'''
class MilestoneBillingService:
    @staticmethod
    def validate_milestone_completion(milestones: list) -> bool:
        return sum(m.get("billing_percentage", 0) for m in milestones) == 100.0
