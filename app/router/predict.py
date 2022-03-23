from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app.basemodels import SentenceInfo
from app.utils import data_preproc, load_models

router = APIRouter(prefix="/sts")


@router.post("/predict")
def predict(sentence: SentenceInfo):

    try:
        model, tokenizer = load_models()
    except Exception:
        raise HTTPException(
            detail="model is not loaded",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    sentence = sentence.dict()
    preprocess = list(map(data_preproc, sentence.values()))

    tensor = tokenizer(
        [preprocess],
        truncation=True,
        padding="longest",
        max_length=128,
        return_tensors="pt",
    )

    result = model(**tensor)
    result = result.tolist()[0][0]

    label = round(result, 1)
    real_label = result
    binary_label = int(result >= 3)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "label": label,
            "real label": real_label,
            "binary label": binary_label,
        },
    )
