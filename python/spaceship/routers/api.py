from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'Fullname': 'Tsaryk Mykola',
        'Sex': 'Male',
        'Nationality': 'Ukr',
        'DocumentID': '12345678',
    }
