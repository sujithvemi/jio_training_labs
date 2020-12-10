from fastapi import FastAPI
from factorial import factorial
import time

from training_api import ComputeFactorialRequest, ComputeFactorialResponse

app = FastAPI()
fact = factorial()

@app.post("/compute/factorial/", response_model=ComputeFactorialResponse)
async def computer_factorial(request: ComputeFactorialRequest):
    start = time.time()
    n = request.dict()['n']
    result = fact.compute(n)
    end = time.time()
    response = ComputeFactorialResponse(
        input_n=n,
        factorial_val=result,
        time_taken=str((end-start)*1000) + 'ms'
    )
    
    return response