import pytest

from vectors import Vector2, Vector3


def test_sub_vector2():
    v1 = Vector2(-1, -1)
    v2 = Vector2(0, 2)
    assert v2 - v1 == Vector2(1, 3)
    

def test_add_vector2():
    v1 = Vector2(-1, -1)
    v2 = Vector2(0, 2)
    assert v2 + v1 == Vector2(-1, 1)
    
       
def test_sub_vector2():
    v1 = Vector2(-1, -1)
    v2 = Vector2(0, 2)
    assert v2 - v1 == Vector2(1, 3)
    

def test_vector2_is_hashable():
    v1 = Vector2(-1, -1)
    v2 = Vector2(0, 2)
    set([v1, v2])
    

def test_vector2_unary_minus():
    v = Vector2(5, -2)
    assert -v == Vector2(-5, 2)

    
# Vector3


def test_add_vector3():
    v1 = Vector3(-1, -1, 7)
    v2 = Vector3(0, 2, -3)
    assert v2 + v1 == Vector3(-1, 1, 4)
    
    
def test_sub_vector3():
    v1 = Vector3(-1, -1, 8)
    v2 = Vector3(0, 2, -2)
    assert v2 - v1 == Vector3(1, 3, -10)

    
def test_vector3_is_hashable():
    v1 = Vector3(-1, -1, 7)
    v2 = Vector3(0, 2, -3)
    set([v1, v2])
    

def test_vector3_unary_minus():
    v = Vector3(5, -2, 1)
    assert -v == Vector3(-5, 2, -1)
    