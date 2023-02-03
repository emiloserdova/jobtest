import random

from fastapi.responses import JSONResponse

from app.helpers import generate_people

people = generate_people()


def get_people(age_from: int, age_to: int) -> JSONResponse:
    fail_number = random.randint(1, 100)
    if fail_number % 3 == 0:
        return JSONResponse(
            content={"success": False, "error": "surprise - sometimes request is failed :) Try again."},
            status_code=500,
        )

    age_range_people = [person for person in people if age_from <= person["age"] <= age_to]

    return JSONResponse(content={"people": age_range_people, "success": True}, status_code=200)
