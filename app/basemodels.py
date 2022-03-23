from pydantic import BaseModel


class SentenceInfo(BaseModel):
    """
    두개의 문장 유사도 측정 API의 입력 값 검증 클래스입니다.

    Attributes:
        sentence1(List[str])
        sentence2(List[str])
    """

    sentence1: str
    sentence2: str

    class Config:
        schema_extra = {
            "example": {
                "sentence1": "숙소 위치는 찾기 쉽고 일반적인 한국의 반지하 숙소입니다.",
                "sentence2": "숙박시설의 위치는 쉽게 찾을 수 있고 한국의 대표적인 반지하 숙박시설입니다.",
            }
        }
