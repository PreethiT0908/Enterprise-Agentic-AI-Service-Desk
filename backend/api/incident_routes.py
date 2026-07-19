from fastapi import APIRouter

from workflow import run_workflow


router = APIRouter()


@router.post("/incidents")
def create_incident(data: dict):

    issue = data["description"]

    result = run_workflow(issue)

    return {
        "status": "success",
        "result": result
    }