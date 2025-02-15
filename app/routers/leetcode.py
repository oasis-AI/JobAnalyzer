from fastapi import APIRouter

router = APIRouter()


@router.post("/solve")
async def solve_leetcode_problem(problem_id: int, code: str):
    # 处理 LeetCode 解题逻辑
    return {"problem_id": problem_id, "code": code, "status": "solved"}
