import sys

count = 0
def ack(m, n):
    global count 
    count += 1
    # if count % 100 == 0:
    print(m, n)
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

if __name__ == "__main__":
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print(ack(m,n))