# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, Extra


class Balances(BaseModel):
    class Config:
        extra = Extra.forbid

    approvals: Dict[str, str]
    balance: str


class TokenMetadata(BaseModel):
    class Config:
        extra = Extra.forbid

    token_id: str
    token_info: Dict[str, str]


class PlentyFa12Storage(BaseModel):
    class Config:
        extra = Extra.forbid

    administrator: str
    balances: Dict[str, Balances]
    lastUpdate: str
    metadata: Dict[str, str]
    paused: bool
    token_metadata: Dict[str, TokenMetadata]
    tokensPerBlock: str
    totalSupply: str