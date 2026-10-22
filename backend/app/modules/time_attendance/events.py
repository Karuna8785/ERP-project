"""
Time, Attendance & Workforce Scheduling - Asynchronous Domain Events & Webhook Dispatchers
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, List, Callable
import uuid

@dataclass
class DomainEvent:
    """Represents an immutable enterprise domain event."""
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str = ""
    module: str = "time_attendance"
    payload: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)

class TimeAttendanceEventDispatcher:
    """Central event broker for dispatching domain notifications in Time, Attendance & Workforce Scheduling."""

    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}
        self._event_history: List[DomainEvent] = []

    def subscribe(self, event_type: str, handler: Callable):
        """Register callback subscriber for specific event topic."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    def publish(self, event_type: str, payload: Dict[str, Any]) -> DomainEvent:
        """Publish new domain event and invoke registered listeners."""
        event = DomainEvent(event_type=event_type, payload=payload)
        self._event_history.append(event)
        handlers = self._subscribers.get(event_type, [])
        for h in handlers:
            try:
                h(event)
            except Exception as e:
                pass
        return event

    def get_event_history(self) -> List[DomainEvent]:
        """Retrieve chronological event dispatch log."""
        return self._event_history

