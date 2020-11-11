from threading import Thread
import requests

URL_LIST = [
    "https://images.pexels.com/photos/60597/dahlia-red-blossom-bloom-60597.jpeg",
    "https://images.pexels.com/photos/65894/peacock-pen-alluring-yet-lure-65894.jpeg",
    "https://images.pexels.com/photos/909/flowers-garden-colorful-colourful.jpg",
    "https://images.pexels.com/photos/863963/pexels-photo-863963.jpeg",
    "https://images.pexels.com/photos/15239/flower-roses-red-roses-bloom.jpg",
    "https://images.pexels.com/photos/1214259/pexels-photo-1214259.jpeg",
    "https://images.pexels.com/photos/1212693/pexels-photo-1212693.jpeg",
    "https://images.pexels.com/photos/1212693/pexels-photo-1212693.jpeg",
    "https://images.pexels.com/photos/1563355/pexels-photo-1563355.jpeg",
    "https://images.pexels.com/photos/1366630/pexels-photo-1366630.jpeg"]


def run_threads(is_daemon):

    def inner_run_threads(func):

        def wrapper(*args):
            t = Thread(target=func, args=args, daemon=is_daemon)
            t.start()
            return t

        return wrapper

    return inner_run_threads


@run_threads(is_daemon=False)
def download_file_by_url(url_, file_name):
    print(f"Downloading from: {url_} --- started")
    r = requests.get(url_)
    with open(file_name, 'wb') as f:
        f.write(r.content)
    print(f"Downloading from: {url_} --- finished")


for index, url in enumerate(URL_LIST):
    download_file_by_url(url, str(index + 1) + ".jpg")
