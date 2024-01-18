# def out_func(nout):
#     def inner_func(nin):
#         return nin*nin
#
#     return out_func(nout)
# print(out_func(5))

def out_func(nout):
    def inner_func():
        return nout*nout

    return inner_func()
print(out_func(5))
#크로저는 바깥 함수의 매개변수와 자신의주소 또한 가지고 있다.?