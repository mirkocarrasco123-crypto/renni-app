from PIL import Image, ImageDraw, ImageFont

def make_icon(size, path):
    img = Image.new('RGBA', (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)
    r = size // 8
    d.rounded_rectangle([0,0,size-1,size-1], radius=r, fill=(31,56,100,255))
    cx, cy = size//2, size//2
    text_size = int(size * 0.38)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", text_size)
    except:
        font = ImageFont.load_default()
    bbox = d.textbbox((0,0), "R", font=font)
    tw = bbox[2]-bbox[0]; th = bbox[3]-bbox[1]
    tx = cx-tw//2-bbox[0]; ty = cy-th//2-bbox[1]-int(size*0.04)
    d.text((tx, ty), "R", fill=(255,255,255,255), font=font)
    accent_y = cy+int(size*0.22)
    accent_w = int(size*0.45); accent_h = int(size*0.055)
    d.rounded_rectangle([cx-accent_w//2, accent_y, cx+accent_w//2, accent_y+accent_h],
                        radius=accent_h//2, fill=(46,117,182,255))
    img.save(path)
    print(f"✓ {size}x{size}")

make_icon(192, '/home/claude/kame-pwa/icon-192.png')
make_icon(512, '/home/claude/kame-pwa/icon-512.png')
