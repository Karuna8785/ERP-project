'''Fixed Asset Depreciation Calculation Engine.'''
class AssetDepreciationService:
    @staticmethod
    def straight_line_schedule(cost: float, salvage_value: float, useful_years: int) -> list:
        depreciable_base = cost - salvage_value
        annual_dep = depreciable_base / useful_years if useful_years > 0 else 0
        schedule = []
        book_val = cost
        for year in range(1, useful_years + 1):
            book_val = max(salvage_value, book_val - annual_dep)
            schedule.append({"year": year, "depreciation": round(annual_dep, 2), "book_value": round(book_val, 2)})
        return schedule
