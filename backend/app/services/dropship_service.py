'''Direct Dropship Order Routing & Dispatch Engine.'''
class DropshipService:
    @staticmethod
    def route_to_supplier(sales_order_id: int, items: list, preferred_supplier_id: int) -> dict:
        return {
            "sales_order_id": sales_order_id,
            "supplier_id": preferred_supplier_id,
            "mode": "DROPSHIP_DIRECT",
            "items_count": len(items),
            "status": "QUEUED_FOR_DISPATCH"
        }
