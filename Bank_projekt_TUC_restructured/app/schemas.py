from pydantic import BaseModel, field_validator, constr, condecimal
from typing import Optional
from decimal import Decimal
import datetime

class TransactionIn(BaseModel):
    tx_id: constr(min_length=1)
    from_account: Optional[str]
    to_account: Optional[str]
    amount: condecimal(gt=0)
    currency: Optional[str] = "SEK"
    timestamp: Optional[datetime.datetime] = None

    @field_validator('timestamp', mode='before')
    def set_timestamp(cls, v):
        if v is None:
            return datetime.datetime.now(datetime.timezone.utc)
        return v

    @field_validator('from_account', 'to_account')
    def acct_len_or_none(cls, v):
        if v is None:
            return v
        if len(v) < 4:
            raise ValueError("Kontonummer för kort")
        return v


