'''Multi-Tenant Isolation Guard.'''
class TenantIsolationService:
    @staticmethod
    def validate_tenant_access(user_tenant_id: str, resource_tenant_id: str) -> bool:
        return user_tenant_id == resource_tenant_id
