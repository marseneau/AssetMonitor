from dataclasses import dataclass
from typing import Optional

@dataclass
class Asset:
    #Populated from input json
    account: str
    symbol: str
    quantity: float

    #Populated with api data
    latest_price: Optional[float] = None
    previous_price: Optional[float] = None
    change: Optional[float] = None
    percent_change: Optional[float] = None
