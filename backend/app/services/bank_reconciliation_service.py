'''Automated Bank Statement Ledger Reconciliation.'''
class BankReconciliationService:
    @staticmethod
    def match_transactions(bank_txns: list, ledger_txns: list) -> dict:
        matched = []
        unmatched_bank = []
        unmatched_ledger = list(ledger_txns)
        for b in bank_txns:
            found = False
            for l in unmatched_ledger:
                if abs(b['amount'] - l['amount']) < 0.01 and b.get('reference') == l.get('reference'):
                    matched.append({'bank': b, 'ledger': l})
                    unmatched_ledger.remove(l)
                    found = True
                    break
            if not found:
                unmatched_bank.append(b)
        return {'matched': matched, 'unmatched_bank': unmatched_bank, 'unmatched_ledger': unmatched_ledger}
