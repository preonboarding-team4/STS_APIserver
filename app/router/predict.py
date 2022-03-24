from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app.basemodels import SentenceInfo
from app.utils import data_preproc, load_models

router = APIRouter(prefix="/sts")


@router.post("/krbert")
def predict(sentence: SentenceInfo):
    """2개의 문장을 입력받아 유사도를 예측하여 반환합니다.

    ### Args: \n
        sentence: sentence1, sentence2

    ### Returns: \n
        semilarity: label, real label, binary label

    ### Notes:\n
        real label -> 예측의 실수 값

        label -> real label을 소수 둘째자리에서 반올림한 값

        binary label -> 3을 기준으로 0과 1로 이진분류한 값
                        0 = [0, 3)
                        1 = [3, 5]
    """
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
