import sys

sys.path.append("../src")

from main import *


def test_creating_an_account_successfully():
    computed = processFile("creating_an_account_successfully.txt", "", False)
    expected = [
        {"accounts": {"activeCard": False, "availableLimit": 750}, "violations": []}
    ]
    assert computed == expected


def test_creating_an_account_that_violates_the_authorizer_logic():
    computed = processFile(
        "creating_an_account_that_violates_the_authorizer_logic.txt", "", False
    )
    expected = [
        {"accounts": {"activeCard": True, "availableLimit": 175}, "violations": []},
        {
            "accounts": {"activeCard": True, "availableLimit": 350},
            "violations": ["account-not-initialized"],
        },
    ]
    assert computed == expected


def test_high_frequency_small_interval():
    computed = processFile("high-frequency-small-interval.txt", "", False)
    expected = [
        {"accounts": {"activeCard": True, "availableLimit": 1000}, "violations": []},
        {
            "accounts": {"activeCard": True, "availableLimit": 1000},
            "violations": ["insufficient-limit"],
        },
        {
            "accounts": {"activeCard": True, "availableLimit": 1000},
            "violations": ["insufficient-limit"],
        },
        {"accounts": {"activeCard": True, "availableLimit": 200}, "violations": []},
        {"accounts": {"activeCard": True, "availableLimit": 120}, "violations": []},
    ]

    assert computed == expected


def test_processing_a_transaction_for_a_not_initialized_account():
    computed = processFile(
        "processing_a_transaction_for_a_not_initialized_account.txt", "", False
    )
    expected = [
        {"accounts": {}, "violations": ["account-not-initialized"]},
        {"accounts": {"activeCard": True, "availableLimit": 225}, "violations": []},
        {"accounts": {"activeCard": True, "availableLimit": 200}, "violations": []},
    ]

    assert computed == expected


def test_processing_a_transaction_successfully():
    computed = processFile("processing_a_transaction_successfully.txt", "", False)
    expected = [
        {"accounts": {"activeCard": True, "availableLimit": 100}, "violations": []},
        {"accounts": {"activeCard": True, "availableLimit": 80}, "violations": []},
    ]

    assert computed == expected


def test_processing_a_transaction_that_violates_the_authorizer_logic():
    computed = processFile(
        "processing_a_transaction_that_violates_the_authorizer_logic.txt", "", False
    )
    expected = [
        {"accounts": {"activeCard": True, "availableLimit": 100}, "violations": []},
        {"accounts": {"activeCard": True, "availableLimit": 80}, "violations": []},
        {"accounts": {"activeCard": True, "availableLimit": 60}, "violations": []},
        {"accounts": {"activeCard": True, "availableLimit": 40}, "violations": []},
        {
            "accounts": {"activeCard": True, "availableLimit": 40},
            "violations": ["high-frequency-small-interval"],
        },
    ]

    assert computed == expected
