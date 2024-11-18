
def common_elements():
    return {x for x in range(100) if x % 3 == 0}.intersection({x for x in range(100) if x % 5 == 0})


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
