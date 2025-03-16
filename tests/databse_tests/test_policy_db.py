from utils.db_utils import get_policy_details


def test_policy_in_db():
    policy_dtails = get_policy_details(1)
    assert policy_dtails is not None
    assert policy_dtails[1] == "Health Insurance"
