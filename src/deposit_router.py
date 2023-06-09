import calendar
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from validation import InputDepositData

router = APIRouter()


@router.post('/deposit/calculation')
async def deposit_calculation(input_data: InputDepositData):
    try:
        rate_by_month = (input_data.rate / 100) / 12
        returned_json_obj = {}
        first_input_month = int(input_data.date.split(".")[1])
        first_input_year = int(input_data.date.split(".")[2])
        last_input_day_by_month = calendar.monthrange(month=first_input_month, year=first_input_year)[1]
        date_data = f"{last_input_day_by_month}.{input_data.date.split('.')[1]}.{input_data.date.split('.')[2]}"
        for period in range(input_data.periods):
            month = int(date_data.split(".")[1])
            year = int(date_data.split(".")[2])
            if returned_json_obj:
                last_key = list(returned_json_obj)[-1]
                returned_json_obj[date_data] = round(
                    (returned_json_obj[last_key] * rate_by_month) + returned_json_obj[last_key], 2)
            else:
                returned_json_obj[date_data] = round((input_data.amount * rate_by_month) + input_data.amount, 2)

            if month == 12:
                date_data_buffer = calendar.monthrange(month=1, year=year + 1)
                date_data = f"{date_data_buffer[1]}.01.{year + 1}"
            else:
                date_data_buffer = calendar.monthrange(month=month + 1,
                                                       year=year)
                if month + 1 < 10:
                    date_data = f"{date_data_buffer[1]}.0{month + 1}.{year}"
                else:
                    date_data = f"{date_data_buffer[1]}.{month + 1}.{year}"
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error")
    return JSONResponse(returned_json_obj)
