import os
import re
import unicodedata

import torch
from transformers import BertTokenizer

base_dir = os.path.dirname(os.path.abspath(__file__))


def data_preproc(paragrahp: str) -> str:
    """
    데이터 전처리를 위한 함수입니다.

    Args:
        paragrahp (str): raw data

    Returns:
        paragraph (str): 전처리된 데이터
    """
    paragrahp = re.sub(r"\(.*\)", "", paragrahp)
    patten = r"[^ .,·?!:'”%/()A-Za-z0-9가-힣+]"
    paragrahp = re.sub(patten, " ", paragrahp)
    paragrahp = " ".join(paragrahp.split())
    paragrahp = unicodedata.normalize("NFKD", paragrahp)
    paragrahp = re.sub(
        "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",  # noqa: E501
        "",
        paragrahp,
    )
    paragrahp = re.sub(
        "'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'", "", paragrahp
    )

    return paragrahp


def load_models():
    """
    사전학습된 모델과 토크나이저를 불러옵니다.

    Returns:
        model: pytorch model
        tokenizer: pytorch tokenizer
    """
    model_dir = f"{base_dir}/torch_models"
    model = torch.jit.load(f"{model_dir}/torch_model.pt")
    tokenizer = BertTokenizer.from_pretrained(
        f"{model_dir}/vocab_snu_subchar12367.txt"
    )

    return model, tokenizer
