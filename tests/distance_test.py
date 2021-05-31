# tests/test_lib.py
from mlproject.distance import haversine

def test_haversine():
    assert type(haversine(0,0,0,0)) == float
    assert haversine(0,0,0,0) == 0
    assert round(haversine(48.865, 2.380, 48.235, 2.393)) == 70