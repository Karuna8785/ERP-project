'''Retail Point-of-Sale (POS) Terminal Sync Engine.'''
class POSSyncService:
    @staticmethod
    def resolve_conflicts(server_stock: int, pos_sold_qty: int) -> int:
        return max(0, server_stock - pos_sold_qty)
