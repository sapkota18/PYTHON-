import json


def load_data():
    try:
        with open("youtube.txt", 'r') as file:
            test= json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" *70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name:{video['name']},Duration:{video['time']}")
    print("*" *70)

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter a video number to update:"))
    if 1 <=index <=len(videos):
        name = input("Enter New Video Name: ")
        time = input("Enter New Video Time: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Video Number")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter a video number to delete: "))
    if 1 <=index <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video Number")

def main():
    videos = load_data()
    while True:
        print("YouTube Manager | Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter a choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
