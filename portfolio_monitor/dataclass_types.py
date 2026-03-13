from dataclasses import dataclass

@dataclass
class Asset:
    account: str
    symbol: str
    quantity: float
    
