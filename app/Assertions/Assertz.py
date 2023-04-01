class Assertz:
    def __init__(self, obj):
        self.obj = obj

    def is_equal_to(self, obj):
        assert self.obj == obj


def assert_that(obj):
    return Assertz(obj)
