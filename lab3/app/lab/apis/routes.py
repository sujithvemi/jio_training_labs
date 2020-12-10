from fastapi import APIRouter

from app.lab.services.services import LabService
from app.lab.models.models import ComputeFactorialRequest, ComputeFactorialResponse
from app.lab.models.models import CheckPrimeRequest, CheckPrimeResponse
from app.lab.models.models import RemoveDuplicateRequest, RemoveDuplicateResponse

router = APIRouter()

@router.post("/compute/factorial/", response_model=ComputeFactorialResponse)
async def compute_factorial(request: ComputeFactorialRequest):
    service = LabService()
    n = request.dict()['n']
    result, time_taken = service.compute_factorial(n)
    response = ComputeFactorialResponse(
        input_n=n,
        factorial_val=result,
        time_taken=time_taken
    )
    
    return response

@router.post("/compute/checkPrime/", response_model=CheckPrimeResponse)
async def compute_factorial(request: CheckPrimeRequest):
    service = LabService()
    n = request.dict()['n']
    result, time_taken = service.check_prime(n)
    response = CheckPrimeResponse(
        input_n=n,
        is_prime=result,
        time_taken=time_taken
    )
    
    return response

@router.post("/text/removeDuplicate", response_model=RemoveDuplicateResponse)
async def compute_factorial(request: RemoveDuplicateRequest):
    service = LabService()
    ip_text = request.dict()['text']
    result, time_taken = service.remove_duplicates(ip_text)
    response = RemoveDuplicateResponse(
        input_text=ip_text,
        result=result,
        time_taken=time_taken
    )
    
    return response