from pydantic import BaseModel

class ComputeFactorialRequest(BaseModel):
    n: int

class ComputeFactorialResponse(BaseModel):
    input_n: int
    factorial_val: int
    time_taken: str