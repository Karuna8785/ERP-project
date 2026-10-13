'''Cross-Docking Logistics Dispatch Optimization.'''
class CrossDockingService:
    @staticmethod
    def match_inbound_to_backorders(inbound_item: str, received_qty: int, backorders: list) -> list:
        allocations = []
        rem = received_qty
        for bo in backorders:
            if bo['item'] == inbound_item and rem > 0:
                take = min(rem, bo['needed'])
                allocations.append({'order_id': bo['order_id'], 'allocated': take})
                rem -= take
        return allocations
