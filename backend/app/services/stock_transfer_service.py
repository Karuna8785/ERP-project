'''Inter-Warehouse Stock Transfer Order (STO) Manager.'''
class StockTransferService:
    @staticmethod
    def initiate_transfer(item_sku: str, qty: int, src_wh: int, dst_wh: int) -> dict:
        return {"sku": item_sku, "quantity": qty, "from_warehouse": src_wh, "to_warehouse": dst_wh, "status": "IN_TRANSIT"}
