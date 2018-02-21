import numpy as np
import pytest
from calculate_stuff import CalculateStuff

def test_calculate_stuff:

    alist1 = CalculateStuff([1, 2, 3, 4, 5])
    assert(np.isclose(alist1.sum_nums(), 15))
    assert(np.isclose(alist1.max_diff(), 1))
    assert(alist1.min_max() == (1, 5))

    alist2 = CalculateStuff([9.0, 1.5, 3.2])
    assert(np.isclose(alist2.sum_nums(), 13.7))
    assert(np.isclose(alist2.max_diff(), 7.5))
    assert(alist2.min_max() == (1.5, 9.0))

    alist3 = CalculateStuff([-5, -7, 5, -2, 12, 15])
    assert(np.isclose(alist3.sum_nums(), 18))
    assert(np.isclose(alist3.max_diff(), 14))
    assert(alist3.min_max() == (-7, 15))

    alist4 = CalculateStuff([9,'h', 8])
    with pytest.raises(TypeError):
        alist4.max_diff()
    with pytest.raises(TypeError):
        alist4.sum_nums()
    with pytest.raises(TypeError):
        alist4.min_max()

    with pytest.raises(ImportError):
        import random

    alist5 = CalculateStuff([])
    with pytest.raises(ValueError):
        alist5.sum_nums();
    with pytest.raises(ValueError):
        alist5.max_diff();
    with pytest.raises(ValueError):
        alist5.min_max();        
