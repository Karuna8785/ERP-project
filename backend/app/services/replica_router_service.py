'''Database Read Replica Session Router.'''
class ReplicaRouterService:
    @staticmethod
    def route_operation(is_write: bool) -> str:
        return "PRIMARY_MASTER" if is_write else "READ_REPLICA_POOL"
