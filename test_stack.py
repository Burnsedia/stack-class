import stack_exm

def test_stack():
    s = stack_exm.stack()
    s.push("a")
    s.push("b")
    try:
        assert s.stack_index("a")

    except:
        assert s.stack_index("b")
    
    finally:
        return s.get_stack()

