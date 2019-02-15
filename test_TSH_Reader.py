import pytest


@pytest.mark.parametrize("TSH_Values, expected", [
                            ([1.2, 1.0, 3.0, 3.9], 'normal thyroid function'),
                            ([4.5, 3.0, 1.3], 'hyperthyroidism'),
                            ([0.8, 1.2, 4.0], 'hypothyroidism'),
])
def test_Diagnose_TSH(TSH_Values, expected):
    from TSH_Reader import Diagnose_TSH
    answer = Diagnose_TSH(TSH_Values)
    assert answer == expected
