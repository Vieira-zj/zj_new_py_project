import torch


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


if __name__ == "__main__":
    # test_torch_tensor()
    # test_torch_calculation()
    test_torch_build_in()
