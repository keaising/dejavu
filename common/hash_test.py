from common.hash import (
    generate_random_string,
    encrypt_password,
    is_right_password,
)


def test_generate_random_string():
    for i in range(10):
        assert len(generate_random_string(i)) == i, i
    assert len(generate_random_string()) == 10, 10


def test_encrypt_password():
    test_cases = [
        {
            "name": "1",
            "input": "wsx123",
            "salt": "False",
            "expect": "cfbfb0216a2ab50f996ed363346b52b1",
        },
        {
            "name": "2",
            "input": "wsx12333",
            "salt": "False",
            "expect": "d97f164138560ec11d307ad5f9d8e961",
        },
        {
            "name": "3",
            "input": "wsx12333ssss",
            "salt": "False",
            "expect": "8b7f09237afb635543ab48593a48f6db",
        },
        {
            "name": "4",
            "input": "wsx123AA",
            "salt": "True",
            "expect": "0c6b3ab8cc1ac2893ac42f930b290edc",
        },
        {
            "name": "5",
            "input": "wsx12AA",
            "salt": "True",
            "expect": "cae0de93a2bcc8cd304813671ca22000",
        },
        {
            "name": "6",
            "input": "wsx123Z*",
            "salt": "True",
            "expect": "580441c232a6ec99c70d79646e946051",
        },
        {
            "name": "7",
            "input": "wsx123AA*&^%$#",
            "salt": "True",
            "expect": "4740f156aad9ff09dd7f7ea75dc38a6e",
        },
        {
            "name": "8",
            "input": "wsx123AAfajsdf",
            "salt": "True",
            "expect": "9fca8abf110bc583bef51a2683ec250f",
        },
    ]
    for case in test_cases:
        assert (
            encrypt_password(case["input"], case["salt"]) == case["expect"]
        ), case["name"]
