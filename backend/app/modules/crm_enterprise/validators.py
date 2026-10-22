"""
Enterprise CRM & Account Management - Enterprise Business Rule Validators
"""
import re
from typing import Optional, List, Dict, Any

class CrmEnterpriseValidator:
    """Validation engine ensuring compliance with business integrity constraints."""

    @staticmethod
    def validate_leadaccount_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate LeadAccount domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_contactperson_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate ContactPerson domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_opportunitydeal_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate OpportunityDeal domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_salespipelinestage_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate SalesPipelineStage domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_quoteproposal_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate QuoteProposal domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_territoryregion_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate TerritoryRegion domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_salesquotatarget_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate SalesQuotaTarget domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_competitoranalysis_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate CompetitorAnalysis domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_customertouchpoint_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate CustomerTouchpoint domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_campaigntracking_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate CampaignTracking domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_leadscoremetric_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate LeadScoreMetric domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_dealcommission_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate DealCommission domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_customerchurnrisk_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate CustomerChurnRisk domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_meetingtranscript_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate MeetingTranscript domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_referralsource_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate ReferralSource domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

    @staticmethod
    def validate_partnerchannel_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate PartnerChannel domain constraints, returning validation flag and error messages."""
        errors = []
        code = payload.get("code", "")
        if not code or len(code.strip()) < 2:
            errors.append("Field 'code' must be at least 2 characters")
        elif not re.match(r"^[A-Z0-9_\-]+$", code):
            errors.append("Field 'code' must contain only uppercase alphanumeric characters, dashes, or underscores")
        title = payload.get("title", "")
        if not title or len(title.strip()) < 3:
            errors.append("Field 'title' must be at least 3 characters")
        amount = payload.get("amount", 0.0)
        if amount is not None and amount < 0:
            errors.append("Field 'amount' cannot be negative")
        quantity = payload.get("quantity", 0.0)
        if quantity is not None and quantity < 0:
            errors.append("Field 'quantity' cannot be negative")
        return len(errors) == 0, errors

