from fastapi import HTTPException
from pydantic import BaseModel, validator


class InputDepositData(BaseModel):
    date: str
    periods: int
    amount: int
    rate: float

    @validator("date")
    def date_validator(cls, date):
        if "." not in date:
            raise HTTPException(status_code=400, detail="Incorrect format. Date format must be dd.mm.YYYY")
        else:
            split_data = list(map(int, date.split(".")))
            if split_data[0] > 31 or split_data[0] < 1:
                raise HTTPException(status_code=400, detail="Incorrect date day")
            elif split_data[1] > 12 or split_data[1] < 1:
                raise HTTPException(status_code=400, detail="Incorrect date month")
            elif split_data[2] < 1:
                raise HTTPException(status_code=400, detail="Incorrect date year")
        return date

    @validator("periods")
    def periods_validator(cls, periods):
        if periods < 1 or periods > 60:
            raise HTTPException(status_code=400,
                                detail="Incorrect periods. Periods must be in range 1 - 60")
        return periods

    @validator("amount")
    def amount_validator(cls, amount):
        if amount < 10000 or amount > 3000000:
            raise HTTPException(status_code=400, detail="Incorrect amount. Amount must be in range 10 000 - 3 000 000")
        return amount

    @validator("rate")
    def rate_validator(cls, rate):
        if rate < 1 or rate > 8:
            raise HTTPException(status_code=400, detail="Incorrect rate. Rate must be in range 1 - 8")
        return rate
