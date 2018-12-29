class global_var(object):
    # 用例ID
    id = '0'

    # 用例名称
    name = '1'

    # 请求url
    url = '2'

    # 是否执行
    run = '3'

    # 请求方式
    request_way = '4'

    # 是否携带cookies
    cookies = '5'

    # 数据类型
    data_type = '6'

    # 依赖id
    depend_id = '7'

    # 依赖数据
    depend_data = '8'

    # 依赖字段
    depend_key = '9'

    # 请求数据
    request_dat = '10'

    # 预期结果
    expect = '11'

    # 实际结果
    result = '12'


# 获取用例id
def get_id():
    return global_var.id


# 获取用例名称
def get_name():
    return global_var.name


# 获取请求url
def get_url():
    return global_var.url


# 获取是否执行
def get_is_run():
    return global_var.run


# 获取请求方式
def get_request_way():
    return global_var.request_way


# 获取是否携带cookies
def get_cookies():
    return global_var.cookies


# 获取请求数据类型
def get_request_type():
    return global_var.data_type


# 获取依赖id
def get_depend_id():
    return global_var.depend_id


# 获取依赖数据
def get_depend_data():
    return global_var.depend_data


# 获取依赖字段
def get_depend_key():
    return global_var.depend_key


# 获取请求数据
def get_request_data():
    return global_var.request_dat


# 获取预期结果
def get_expect():
    return global_var.expect


# 获取时间结果
def get_result():
    return global_var.result
