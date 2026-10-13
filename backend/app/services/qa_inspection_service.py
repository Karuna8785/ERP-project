'''Quality Assurance Sampling & AQL Verification.'''
class QAInspectionService:
    @staticmethod
    def evaluate_inspection(received_qty: int, sampled_qty: int, defects_found: int, max_allowable_defects: int) -> bool:
        return defects_found <= max_allowable_defects
