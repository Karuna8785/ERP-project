"""
Fleet Telematics & Route Optimization - Enterprise Business Rule Validators
"""
import re
from typing import Optional, List, Dict, Any

class FleetManagementValidator:
    """Validation engine ensuring compliance with business integrity constraints."""

    @staticmethod
    def validate_fleetvehicle_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate FleetVehicle domain constraints, returning validation flag and error messages."""
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
    def validate_driverprofile_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate DriverProfile domain constraints, returning validation flag and error messages."""
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
    def validate_vehicletelematicslog_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate VehicleTelematicsLog domain constraints, returning validation flag and error messages."""
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
    def validate_odometerreading_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate OdometerReading domain constraints, returning validation flag and error messages."""
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
    def validate_fuelconsumptionlog_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate FuelConsumptionLog domain constraints, returning validation flag and error messages."""
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
    def validate_fleetserviceschedule_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate FleetServiceSchedule domain constraints, returning validation flag and error messages."""
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
    def validate_repairworkorder_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate RepairWorkOrder domain constraints, returning validation flag and error messages."""
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
    def validate_tirewearlog_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate TireWearLog domain constraints, returning validation flag and error messages."""
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
    def validate_inspectionpretrip_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate InspectionPreTrip domain constraints, returning validation flag and error messages."""
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
    def validate_routeoptimizationrun_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate RouteOptimizationRun domain constraints, returning validation flag and error messages."""
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
    def validate_geofencezone_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate GeofenceZone domain constraints, returning validation flag and error messages."""
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
    def validate_speedingviolation_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate SpeedingViolation domain constraints, returning validation flag and error messages."""
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
    def validate_accidentreport_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate AccidentReport domain constraints, returning validation flag and error messages."""
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
    def validate_fleetinsuranceclaim_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate FleetInsuranceClaim domain constraints, returning validation flag and error messages."""
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
    def validate_permitlicenserenewal_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate PermitLicenseRenewal domain constraints, returning validation flag and error messages."""
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
    def validate_depotstation_record(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate DepotStation domain constraints, returning validation flag and error messages."""
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

