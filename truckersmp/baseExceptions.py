class BaseExceptions(Exception):
    def __init__(self):
        super().__init__()
        
    def __str__(self) -> str:
        return super().__str__()
    
class ConnectionError(BaseExceptions):
    def __init__(self):
        self.message = "Connection Error. This could be due to your internet connection or the API being unavailable."
        super().__init__()
        
        
    def __str__(self) -> str:
        return self.message

class RateLimitError(BaseExceptions):
    def __init__(self):
        self.message = "Rate Limit Error. You are sending too many requests to the API!"
        super().__init__()
        
        
    def __str__(self) -> str:
        return self.message       