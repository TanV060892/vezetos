from fastapi import APIRouter, BackgroundTasks
from tasks import sync_crm_data, sync_marketing_data
from utils import common

router = APIRouter()

'''
 * Trigger synchronization for a specific data source
 * @route GET /sync/{source}
 * @returns JSON Object 200 - Ok
 * @returns JSON Object 422 - Unprocessable Entity
 * @returns JSON Object 500 - Internal server error
'''
@router.get("/sync/{source}")
async def sync_data(source: str, background_tasks: BackgroundTasks):
    if source == "crm":
        background_tasks.add_task(sync_crm_data)
    elif source == "marketing":
        background_tasks.add_task(sync_marketing_data)
    else:
        return common.process_error_response('VZ422')
    
    return common.process_success_response({"message": "Sync task started"})
