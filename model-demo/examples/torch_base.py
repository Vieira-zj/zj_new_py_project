import torch
from torch import Tensor

# example: torch


def test_torch_tensor():
    print(f"torch.tensor default as: {torch.tensor(1).dtype}")

    t1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float64)
    print(t1)
    t2 = torch.ones((2, 2))
    print(t2)


def test_torch_calculation():
    # 逐元素相乘
    a = torch.tensor([[1, 2], [3, 4]])
    b = torch.tensor([[1, 2], [3, 4]])
    c1 = a * b
    print(c1)

    # 矩阵乘法
    c2 = torch.mm(a, b)
    print(c2)


def test_torch_build_in():
    a = torch.tensor([-1.1, 0.5, 0.501, 0.99])
    print(f"round:\n{torch.round(a)}")

    print(f"arange:\n{torch.arange(5)}")

    print(f"rand:\n{torch.rand(3, 3)}")
    print(f"randn:\n{torch.randn(3, 3)}")


def test_torch_slice():
    pass


# example: attention


def test_token_attention():
    inputs = torch.tensor(
        [
            [0.43, 0.15, 0.89],  # Your     (x^1) - 第 1 个 token 嵌入向量
            [0.55, 0.87, 0.66],  # journey  (x^2) - 第 2 个 token 嵌入向量
            [0.57, 0.85, 0.64],  # starts   (x^3) - 第 3 个 token 嵌入向量
            [0.22, 0.58, 0.33],  # with     (x^4) - 第 4 个 token 嵌入向量
            [0.77, 0.25, 0.10],  # one      (x^5) - 第 5 个 token 嵌入向量
            [0.05, 0.80, 0.55],  # step     (x^6) - 第 6 个 token 嵌入向量
        ]
    )

    dim = inputs.shape[1]
    print("dim:", dim)

    # inputs 形状: [seq_len, dim]
    # inputs.T 形状: [dim, seq_len]
    # 结果 attn_scores 形状: [seq_len, seq_len] -> 得到了一个 N*N 的关系矩阵
    attn_scores = inputs @ inputs.T  # query @ key
    print("attation scores:", attn_scores)

    # Softmax: 将分数转化为概率 (权重), 相当于分配注意力比例
    # 比如：[0.1, 0.8, 0.1] 表示主要关注中间那个词
    attn_weight = torch.softmax(attn_scores, dim=-1)

    # MatMul: 根据权重, 提取并融合信息
    # 权重大的向量会被更多地 "吸取" 进来, 权重小的则被忽略
    context_vec = attn_weight @ inputs
    print("result:", context_vec)


def my_attn_scores(inputs: Tensor) -> Tensor:
    attn_scores = torch.empty(6, 6)

    # 计算注意力分数矩阵: 遍历所有 token 对, 计算它们之间的点积相似度
    # 外层循环: 遍历每个 token 作为查询 (query)
    for i, x_i in enumerate(inputs):
        # 内层循环: 遍历每个 token 作为键 (key)
        for j, x_j in enumerate(inputs):
            # 注意这里的 token 是一个多维度的向量，所以要展开计算
            dot_product = 0.0
            # 遍历向量的每个维度进行计算
            for k, _ in enumerate(x_i):
                dot_product += x_i[k] * x_j[k]

            attn_scores[i, j] = dot_product

    return attn_scores


if __name__ == "__main__":
    # test_torch_tensor()
    # test_torch_calculation()
    # test_torch_build_in()

    test_token_attention()
