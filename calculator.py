"""极简计算器：目前提供基础除法功能。

只使用 Python 标准库，可直接运行本文件查看示例输出。
"""


def divide(a, b):
    """返回 a 除以 b 的商。

    参数:
        a: 被除数，int 或 float。
        b: 除数，int 或 float。

    返回:
        float，即 a / b 的结果。
    """
    return a / b


def main():
    """运行一个简单的演示。"""
    a, b = 10, 4
    print(f"{a} / {b} = {divide(a, b)}")


if __name__ == "__main__":
    main()
