import random
import time
import os

def main():
    while True:
        if os.path.exists("prng-service.txt"):
            with open("prng-service.txt", "r") as f:
                command = f.read().strip()
            if command == "run":
                # Generate a random number
                random_number = random.randint(0, 100)
                # Overwrite the command file with the random number
                with open("prng-service.txt", "w") as f:
                    f.write(str(random_number))
        time.sleep(1)

if __name__ == "__main__":
    main()
