from pysat.solvers import Solver
import argparse
# default 
N = 4

def encode(i, j, isNeg=False):
    ret= (i-1) * N + j 
    if isNeg:
        return -(ret)
    return ret

def solve():
    
    cnf = []
     
    for i in range(1, N+1):
        disj = []
        for j in range(1, N+1):
            disj.append(encode(i, j))
        cnf.append(disj)    
    for i in range(1, N+1):
        for j in range(1, N+1):
            disj = []
            
            # ROW
            offset = 1            
            jj = j + offset
            while jj < N + 1:
                cnf.append([encode(i, j,isNeg=True),encode(i, jj, isNeg=True)])
                jj += offset
            
            offset = 1
            jj = j - offset
            while jj > 0:
                cnf.append([encode(i, j,isNeg=True),encode(i, jj, isNeg=True)])
                jj -= offset
            # COL
            offset = 1
            ii = i + offset
            while ii < N + 1:
                cnf.append([encode(i, j,isNeg=True), encode(ii, j, isNeg=True)])                
                ii += offset
            offset = 1
            ii = i - offset
            while ii > 0:
                cnf.append([encode(i, j,isNeg=True), encode(ii, j, isNeg=True)])
                ii -= offset

            # incline
            offset = 1
            ii = i + offset
            jj = j + offset            
            while ii < N+1 and jj < N+1:
                cnf.append([encode(i, j,isNeg=True), encode(ii, jj, isNeg=True)])
                ii += offset
                jj += offset
                    

            offset = 1
            ii = i - offset 
            jj = j + offset 
            while ii > 0 and jj < N+1:
                cnf.append([encode(i, j,isNeg=True), encode(ii, jj, isNeg=True)])
                ii -= offset
                jj += offset

            offset = 1
            ii = i + offset 
            jj = j - offset 
            while ii < N+1 and jj > 0:
                cnf.append([encode(i, j,isNeg=True), encode(ii, jj, isNeg=True)])
                ii += offset
                jj -= offset
    
            offset = 1
            ii = i - offset 
            jj = j - offset 
            while ii > 0 and jj > 0:
                cnf.append([encode(i, j,isNeg=True), encode(ii, jj, isNeg=True)])
                ii -= offset
                jj -= offset

            
    solver = Solver(bootstrap_with=cnf)
    ret = solver.solve()
    count = 0
    for model in solver.enum_models():
        count += 1
    return count 
def main():
    print("{}-Queen Problem".format(N))
    n_sol = solve()
    print("There are {} solutions for {} Queen Problem".format(n_sol, N))
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a N-Queen SAT Solver")
    parser.add_argument("--n", type=int,default=4, help="please input an integer N")
    args = parser.parse_args()    
    N = args.n
    main()