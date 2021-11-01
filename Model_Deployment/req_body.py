from pydantic import BaseModel
# 2. Class which describes the inputs
class request_body(BaseModel):
    col_0: int
    col_1: int
    col_2: int
    col_3: int
    col_4: int
    col_5: int
    col_6: int
    col_7: int
    account_length: float
    international_plan: int
    voice_mail_plan: int
    number_vmail_messages: float
    total_day_minutes: float
    total_day_calls: float
    total_day_charge: float
    total_eve_minutes: float
    total_eve_calls: float
    total_eve_charge: float
    total_night_minutes: float
    total_night_calls: float
    total_night_charge: float
    total_intl_minutes: float
    total_intl_calls: float
    total_intl_charge: float
    number_customer_service_calls: float
    area_code_408: float
    area_code_415: float
    area_code_510: float