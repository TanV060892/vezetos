from fastapi import APIRouter
from utils import common

#api call starts from here
router = APIRouter()

background_tasks = []

'''
 * Get List of all running tasks
 * @route GET /tasks
 * @returns JSON Object 200 - Ok
 * @returns JSON Object 500 - Internal server error
'''
@router.get("/tasks")
def list_tasks():
    return common.process_success_response({"tasks": background_tasks})

'''
 * Cancel Task from Task ID
 * @route POST /tasks/cancel
 * @returns JSON Object 200 - Ok
 * @returns JSON Object 422 - Unprocessable Entity
 * @returns JSON Object 500 - Internal server error
'''
@router.post("/tasks/cancel")
def cancel_task(task_id: int):
    return common.process_success_response({"action":"Cancel","message": "Task cancelled"})
