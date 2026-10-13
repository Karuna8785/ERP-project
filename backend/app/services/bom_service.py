'''Multi-Level Bill of Materials (BOM) Explosion Engine.'''
class BOMExplosionService:
    @staticmethod
    def explode(bom_tree: dict, quantity: float = 1.0) -> list:
        items = []
        for component, factor in bom_tree.items():
            items.append({"component": component, "required_quantity": round(quantity * factor, 3)})
        return items
