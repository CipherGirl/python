import time

def fetch_data(param):
    print(f'Do something with {param}')
    time.sleep(param)
    print(f'Done with {param}')
    return f'Result of {param}'


def main():
    result1 = fetch_data(1)
    print("Fetching result1 completed")

    result2 = fetch_data(2)
    print("Fetching result2 completed")

    return [result1, result2]

t1 = time.perf_counter()
results = main()
t2 = time.perf_counter()

print(f"Total time: {t2-t1:.2f}")