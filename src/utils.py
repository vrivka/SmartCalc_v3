def get_resource(path):
    i = __file__.rfind('\\')
    return __file__[:i] + '/' + path
