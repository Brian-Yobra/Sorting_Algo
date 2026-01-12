
import random


def main():
    iterations = 0
    with open('dataset.txt', 'w') as f:
        while iterations < 1000000000:
            iterations += 1
            value = random.randint(0, 10000000)
            string = str(value)
            f.write(string+ "\n")

    
    
    
if __name__ == "__main__":
    main()