"""Custom exceptions for My.app"""


class MyAppException(Exception):
    """Base exception for My.app"""
    pass


class AgentException(MyAppException):
    """Agent-related exceptions"""
    pass


class LLMProviderException(MyAppException):
    """LLM provider exceptions"""
    pass


class ConfigurationException(MyAppException):
    """Configuration exceptions"""
    pass


class DatabaseException(MyAppException):
    """Database exceptions"""
    pass


class ValidationException(MyAppException):
    """Validation exceptions"""
    pass


class NotFoundError(MyAppException):
    """Resource not found"""
    pass


class UnauthorizedError(MyAppException):
    """Unauthorized access"""
    pass


class ConflictError(MyAppException):
    """Resource conflict"""
    pass


class RateLimitError(MyAppException):
    """Rate limit exceeded"""
    pass
