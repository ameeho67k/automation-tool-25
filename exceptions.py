class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class NotFoundError(CustomError):
    """Exception raised for not found errors."""
    def __init__(self, item):
        self.item = item
        self.message = f'Item {item} not found'
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f'Validation failed for {field}: {message}')

class DatabaseError(CustomError):
    """Exception raised for database errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AuthenticationError(CustomError):
    """Exception raised for authentication errors."""
    def __init__(self, username):
        self.username = username
        self.message = f'Authentication failed for user {username}'
        super().__init__(self.message)

# Example Usage:
# raise NotFoundError('User')
# raise ValidationError('email', 'Invalid format')
# raise DatabaseError('Connection lost')
# raise AuthenticationError('john_doe')
