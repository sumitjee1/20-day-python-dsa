#Code to Impliment Fibonaci series using Dynamic Programming
class Fibonacci:
    def __init__(self):
        self.memo = {}

    def fibonacci(self, n):
        if n <= 1:
            return n
        if n not in self.memo:
            self.memo[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return self.memo[n]

if __name__ == "__main__":
    fib = Fibonacci()
    n = 10  # Calculate Fibonacci for n = 10
    print(f"Fibonacci Series up to {n}:")
    for i in range(n + 1):
        print(fib.fibonacci(i), end=" ")
