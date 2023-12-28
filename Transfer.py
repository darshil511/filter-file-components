import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_files_by_extension(source, destination, extensions):
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        if os.path.isfile(source_path):
            for ext in extensions:
                if filename.endswith(ext):
                    shutil.move(source_path, os.path.join(destination, filename))
                    break

def main():
    source_folder = "D:\Camera"
    images_folder = "D:\Images"
    videos_folder = "D:\Videos"

    create_directory(images_folder)
    create_directory(videos_folder)

    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    video_extensions = [".mp4", ".avi", ".mov"]

    move_files_by_extension(source_folder, images_folder, image_extensions)
    move_files_by_extension(source_folder, videos_folder, video_extensions)

    print("Files moved successfully.")

if __name__ == "__main__":
    main()
