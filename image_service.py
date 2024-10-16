import os
import time

images_folder = "images"
images = [f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

def main():
    while True:
        # Check if image-service.txt exists and contains a random number
        if os.path.exists("image-service.txt"):
            with open("image-service.txt", "r") as f:
                try:
                    random_number = int(f.read().strip())
                except ValueError:
                    time.sleep(1)
                    continue

            # Calculate the image path based on the random number
            image_path = os.path.join(images_folder, images[random_number % len(images)])

            # Write the image path back to image-service.txt
            with open("image-service.txt", "w") as f:
                f.write(image_path)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
