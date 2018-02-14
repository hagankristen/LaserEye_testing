def test_max_diff():

    from calculate_stuff import max_diff
    import numpy as np
    import pytest

    max_value1 = max_diff([1, 2, 3, 4, 5])
    max_value2 = max_diff([9.0, 1.5, 3.2])
    max_value3 = max_diff([-5, -7, 5, -2, 12, 15])

    assert(np.isclose(max_value1, 1))
    assert(np.isclose(max_value2, 7.5))
    assert(np.isclose(max_value3, 14))

    with pytest.raises(TypeError):
        max_diff(['a', 'b', 'c'])

    with pytest.raises(ValueError):
        max_diff(7)

    with pytest.raises(ValueError):
        max_diff([7])

    with pytest.raises(ValueError):
        max_diff([4, 5, float('nan')])
