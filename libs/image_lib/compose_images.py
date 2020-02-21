from PIL import Image

def join(top_path, bottom_path, left=None, top=None):
    top_image, bottom_image = Image.open(top_path), Image.open(bottom_path)
    top_size, bottom_size = top_image.size, bottom_image.size

    if left is None:
        left = int(bottom_size[0] / 2) - int(top_size[0] / 2)
    if top is None:
        top = int(bottom_size[1] / 2) - int(top_size[1] / 2)

    joint = Image.new('RGB', (bottom_size[0], bottom_size[1]))
    joint.paste(bottom_image, (0, 0))
    joint.paste(top_image, (left, top))
    joint.save('./out.png')

if __name__ == '__main__':
    join('./qrcode.jpeg', '../assets/full.png')