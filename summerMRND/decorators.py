from time import perf_counter

def callTimer(includeRecursive=False):
    def outer(func):
        func.level=0
        def inner(*args,**kwargs):
            if (not includeRecursive) and func.level>0:
                return func(*args,**kwargs)
            else:

                func.level+=1
                start=perf_counter()
                result=func(*args,**kwargs)
                end=perf_counter()
                func.level-=1
                inner.times.append('{0}:{1}'.format(func.__name__+str(args),end-start))
                return result
        inner.times=[]
        return inner
    return outer
def callCounter(countRecursive=False):
    def outer(func):
        func.level=0
        def inner(*args,**kwargs):
            if (not countRecursive) and func.level>0:
                return func(*args,**kwargs)
            else:
                inner.count += 1
                func.level+=1
                result=func(*args,**kwargs)
                func.level=-1
                return result
        inner.count=0
        inner.times=func.times
        return inner
    return outer

@callCounter(countRecursive=True)
@callTimer(includeRecursive=True)
def fib(num):
    if(num==1 or num==0):
        return 1
    else:
        return fib(num-1)+fib(num-2)


if  __name__=="__main__":
    print(fib(2),fib.count)
    print(fib.times)