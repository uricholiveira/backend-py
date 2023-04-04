from dependency_injector.wiring import inject
from fastapi import APIRouter

router = APIRouter(prefix="/health_check", tags=["Health Check"])


@router.get("/")
@inject
async def health_check():
    return "OK"


# Example of inject on endpoints

# @router.get("/")
# @inject
# async def health_check(
#     health_check_service: HealthCheckService = Depends(Provide[Container.health_check_service]),
# ):
#     result = await health_check_service.get_status()
#     return result