import torch
from transformers import BertModel, BertPreTrainedModel


class FCLayer(torch.nn.Module):
    def __init__(
        self, input_dim, output_dim, dropout_rate=0.0, use_activation=None
    ):
        super(FCLayer, self).__init__()
        self.use_activation = use_activation
        self.dropout = torch.nn.Dropout(dropout_rate)
        self.linear = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        x = self.dropout(x)
        if self.use_activation:
            x = self.use_activation(x)
        return self.linear(x)


class BertSts(BertPreTrainedModel):
    def __init__(self, config) -> None:
        super(BertSts, self).__init__(config)
        self.bert = BertModel(config)
        self.output_layer = FCLayer(config.hidden_size, 1)

    def forward(
        self, input_ids=None, attention_mask=None, token_type_ids=None
    ):
        bert_outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
        )
        sim_score = self.output_layer(bert_outputs["pooler_output"])
        return sim_score
