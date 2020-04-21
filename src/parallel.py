from multiprocessing import Pool 
def f(x):
    return x*x
if __name__=='__main__':
    with Pool(processes=4) as pool:
        print(pool.map(f, range(10)))
        for i in pool.imap(f, range(10)):
            print(i)
