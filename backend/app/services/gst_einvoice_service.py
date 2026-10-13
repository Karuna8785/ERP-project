'''GST E-Invoicing and B2B QR Code Generation Engine.'''
import hashlib
import json
from typing import Dict, Any

class GSTEInvoiceService:
    @staticmethod
    def generate_irn(supplier_gstin: str, doc_type: str, doc_num: str, fin_year: str) -> str:
        raw = f"{supplier_gstin.upper()}{doc_type.upper()}{doc_num.upper()}{fin_year}"
        return hashlib.sha256(raw.encode('utf-8')).hexdigest()

    @staticmethod
    def generate_signed_qr_payload(irn: str, supplier_gst: str, buyer_gst: str, total_value: float) -> Dict[str, Any]:
        return {
            "irn": irn,
            "seller_gstin": supplier_gst,
            "buyer_gstin": buyer_gst,
            "total_value": total_value,
            "status": "GENERATED"
        }
