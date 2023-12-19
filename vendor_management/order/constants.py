from enum import StrEnum

class OrderStatus(StrEnum):
    """Status for Order using string enumeration"""
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    @classmethod
    def is_valid_status(cls, status):
        return status.lower() in [i.name.lower() for i in cls]
