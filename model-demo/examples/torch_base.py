import torch
from torch import Tensor, nn

# example: torch


def test_torch_device():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device.type)


def test_torch_tensor():
    print(f"torch.tensor default as: {torch.tensor(1).dtype}")

    t1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float64)
    print(f"tensor:\n{t1}")

    t2 = torch.arange(5)
    print(f"arange:\n{t2}")

    t3 = torch.ones((2, 2))
    print(f"ones:\n{t3}")

    t4 = torch.rand(3, 3)
    print(f"rand:\n{t4}")
    t5 = torch.randn(3, 3)
    print(f"randn:\n{t5}")


def test_torch_builtin():
    a = torch.tensor([-1.1, 0.5, 0.501, 0.99])
    print(f"round:\n{torch.round(a)}")

    # 增加维度
    x = torch.randn(3, 4)
    x_unsq = x.unsqueeze(0)
    print(f"unsqueeze:\n{x_unsq.shape}")

    # 减少维度
    x_sq = x_unsq.squeeze(0)
    print(f"squeeze:\n{x_sq.shape}")

    # 转置
    y = x.transpose(0, 1)
    print(f"transpose:\n{y.shape}")


def test_torch_view():
    x = torch.randn(2, 3, 4)
    print("is_contiguous:", x.is_contiguous())
    print(x)

    # 连续使用 view
    y = x.view(6, 4)
    print(y)

    # 转置后变为非连续
    print("\ntranspose:")
    x_t = x.transpose(1, 2)
    print(x_t.is_contiguous())  # false

    # 非连续使用 reshape
    y_t = x_t.reshape(6, 4)
    print(y_t)


def test_torch_calculate():
    # 逐元素相乘
    a = torch.tensor([[1, 2], [3, 4]])
    b = torch.tensor([[1, 2], [3, 4]])
    c1 = a * b
    print(c1)

    # 矩阵乘法
    c2 = torch.mm(a, b)
    print(c2)


def test_torch_grad():
    x = torch.tensor(2.0, requires_grad=True)
    y = x**2 + 2 * x + 2
    # 计算梯度
    y.backward()
    print(f"在 x=2 处的导数: {x.grad}")


def test_torch_regexp():
    x = torch.randn(32, 100)
    dropout = nn.Dropout(p=0.2)  # 丢弃 20% 神经元
    x_dropped = dropout(x)  # 训练时随机置零部分元素
    print(f"dropout: {x_dropped}")


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
    test_torch_device()

    # test_torch_tensor()
    # test_torch_builtin()
    # test_torch_view()
    # test_torch_calculate()

    # test_torch_grad()
    # test_torch_regexp()

    # test_token_attention()
