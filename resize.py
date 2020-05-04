import glob
from pathlib import Path
from PIL import Image

def resize_all(base_path, save_path):
    files = glob.glob('raw/*/*.png')
    for f in files:
        print(f"resize {f} ...", end="")
        load_img_path = base_path.joinpath(f)
        save_img_path = save_path.joinpath(save_path, f).resolve()
        resize_img(load_img_path, save_img_path)
        print("... finsh!")

def resize_img(load_img_path, save_img_path):
    img = Image.open(load_img_path)
    img_resize = img.resize((int(img.width / 5), int(img.height / 5)))
    save_img_path.parent.mkdir(parents=True, exist_ok=True)
    img_resize.save(save_img_path)

if __name__ == "__main__":
    base_path = Path.cwd()
    save_path = base_path.joinpath("save")
    print(f"save img to {str(save_path)}")
    resize_all(base_path, save_path)
    print("resizing complete!!")

