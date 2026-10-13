'''Purchase Requisition Authorization & Delegation Hierarchy.'''
class PurchaseRequisitionService:
    @staticmethod
    def determine_approval_levels(total_amount: float) -> list:
        if total_amount < 50000:
            return ["DEPARTMENT_HEAD"]
        elif total_amount < 250000:
            return ["DEPARTMENT_HEAD", "FINANCE_CONTROLLER"]
        return ["DEPARTMENT_HEAD", "FINANCE_CONTROLLER", "EXECUTIVE_DIRECTOR"]
