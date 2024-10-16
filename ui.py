import os
import time

def clear_files():
    for filename in ["prng-service.txt", "image-service.txt"]:
        with open(filename, "w") as f:
            f.write("")

def main():
    while True:
        command = input("Enter 'run' to get a random image: ")
        if command.strip().lower() == "run":
            clear_files()

            # Notify the PRNG service
            with open("prng-service.txt", "w") as f:
                f.write("run")

            # Wait for the PRNG service to generate the random number
            time.sleep(1)

            # Read the pseudo-random number from prng-service.txt
            while True:
                with open("prng-service.txt", "r") as f:
                    result = f.read().strip()
                try:
                    random_number = int(result)
                    print(f"Generated random number: {random_number}")
                    break 
                except ValueError:
                    print("Waiting for PRNG service to respond...")
                    time.sleep(1)

            # Write the random number to image-service.txt for the Image Service
            with open("image-service.txt", "w") as f:
                f.write(str(random_number))

            # Wait for the Image service to write the image path
            while not os.path.exists("image-service.txt"):
                print("Waiting for Image service to respond...")
                time.sleep(1)


            time.sleep(3)
            
            # Read the image path
            with open("image-service.txt", "r") as f:
                image_path = f.read().strip()
            print(f"Image path: {image_path}")

            # Open the image using the default image viewer
            os.startfile(image_path)

        else:
            print("Invalid command. Please type 'run'.")

if __name__ == "__main__":
    main()
