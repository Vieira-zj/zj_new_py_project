import torch
from torch import nn


# ==========================================
# 1. Config
# ==========================================
class QdogBabyLearnConfig:
    def __init__(self):
        self.model_name: str = "qdogbabylearn"
        self.version: str = "1.0.0"

        self.num_hidden_layers: int = 16  # 盖多少层楼 (Transformer Block的数量)
        self.num_heads: int = 8  # 雇多少个专家同时看 (多头注意力的头数)
        self.emb_dim: int = 512  # 词向量的宽度 (每个词包含多少信息量)
        self.dropout: float = 0.0  # 随机扔掉多少神经元 (防止死记硬背)
        self.context_size: int = 512  # 一次能看多长的文章 (上下文窗口大小)
        self.vocab_size: int = 6400  # 字典里有多少个字 (词表大小)


# ==========================================
# 2. LLM Model
# ==========================================


# ==========================================
# 3. Transformer Block
# ==========================================
class TransformerBlock(nn.Module):
    pass


# ==========================================
# 4. Multi Head Attention
# ==========================================


class MultiHeadAttention(nn.Module):
    def __init__(self, emb_dim: int, num_heads: int, dropout: float, context_size: int):
        super().__init__()
        self.emb_dim = emb_dim
        self.num_heads = num_heads
        self.head_dim = emb_dim // num_heads  # 每个 head 负责的维度 (512/8 = 64)

        # 定义 Q,K,V 映射层
        self.W_querys = nn.Linear(emb_dim, emb_dim)  # 我要啥
        self.W_keys = nn.Linear(emb_dim, emb_dim)  # 你有啥
        self.W_values = nn.Linear(emb_dim, emb_dim)  # 我是啥

        self.out = nn.Linear(emb_dim, emb_dim)  # 信息汇总
        self.dropout = nn.Dropout(dropout)

        self.register_buffer("mask", torch.tril(torch.ones(context_size, context_size)))


# ==========================================
# 5. 前馈网络 (发散思维 -> 收敛总结)
# ==========================================


class FeedForward(nn.Module):
    pass
