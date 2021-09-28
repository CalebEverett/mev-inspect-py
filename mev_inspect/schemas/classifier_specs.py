from typing import Dict, List, Optional

from pydantic import BaseModel

from .classified_traces import Classification, Protocol


class ClassifierSpec(BaseModel):
    abi_name: str
    protocol: Optional[Protocol] = None
    valid_contract_addresses: Optional[List[str]] = None
    classifications: Dict[str, Classification] = {}
