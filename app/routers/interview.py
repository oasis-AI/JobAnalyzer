from fastapi import APIRouter

router = APIRouter()


@router.post("/simulate")
async def simulate_interview(candidate_id: int, questions: list):
    # 处理模拟面试逻辑
    return {
        "candidate_id": candidate_id,
        "questions": questions,
        "status": "interview simulated",
    }
