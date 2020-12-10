from pydantic import BaseModel

class ComputeFactorialRequest(BaseModel):
    n: int

class ComputeFactorialResponse(BaseModel):
    input_n: int
    factorial_val: int
    time_taken: str

class CheckPrimeRequest(BaseModel):
    n: int

class CheckPrimeResponse(BaseModel):
    input_n: int
    is_prime: str
    time_taken: str

class RemoveDuplicateRequest(BaseModel):
    text: str

class RemoveDuplicateResponse(BaseModel):
    input_text: str
    result: str
    time_taken: str
