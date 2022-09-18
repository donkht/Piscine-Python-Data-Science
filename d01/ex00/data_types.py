def data_types():
    v_int = 42
    v_str = "42"
    v_float = 4.2
    v_bool = True
    v_list = set()
    v_dict = dict()
    v_tuple = tuple()
    v_set = set()
    objects = [v_int, v_str, v_float, v_bool, v_list, v_dict, v_tuple, v_set]
    types4print = []
    for x in objects:
        types4print.append(str(type(x).__name__))
    print(str(types4print).replace("'", ""))

if __name__ == '__main__':
    data_types()