from common.check import check_password, check_mobile


def test_check_password():
    test_cases = [
        {"name": "1", "input": "wsx123", "expect": False},
        {"name": "2", "input": "wsx12333", "expect": False},
        {"name": "3", "input": "wsx12333ssss", "expect": False},
        {"name": "4", "input": "wsx123AA", "expect": True},
        {"name": "5", "input": "wsx12AA", "expect": True},
        {"name": "6", "input": "wsx123Z*", "expect": True},
        {"name": "7", "input": "wsx123AA*&^%$#", "expect": True},
        {"name": "8", "input": "wsx123AAfajsdf", "expect": True},
    ]
    for case in test_cases:
        assert check_password(case["input"]) == case["expect"], case["name"]


def test_check_mobile():
    test_cases = [
        {"name": "1", "input": "1581111444", "expect": False},
        {"name": "2", "input": "1581111444x", "expect": False},
        {"name": "3", "input": "12581111444", "expect": False},
        {"name": "4", "input": "15811114444", "expect": True},
        {"name": "5", "input": "13811114444", "expect": True},
        {"name": "6", "input": "14811114444", "expect": True},
        {"name": "7", "input": "16811114444", "expect": True},
        {"name": "8", "input": "17811114444", "expect": True},
        {"name": "9", "input": "18811114444", "expect": True},
        {"name": "10", "input": "19811114444", "expect": True},
    ]
    for case in test_cases:
        assert check_mobile(case["input"]) == case["expect"], case["name"]
