import time
import concurrent.futures
import os
from PIL import Image, ImageFilter

img_names = [
    '/Users/welldev/Code/self-development/python/photo-1516117172878-fd2c41f4a759.jpg',
    '/Users/welldev/Code/self-development/python/photo-1532009324734-20a7a5813719.jpg',
    '/Users/welldev/Code/self-development/python/photo-1524429656589-6633a470097c.jpg',
    '/Users/welldev/Code/self-development/python/photo-1530224264768-7ff8c1789d79.jpg',
    '/Users/welldev/Code/self-development/python/photo-1564135624576-c5c88640f235.jpg',
    '/Users/welldev/Code/self-development/python/photo-1541698444083-023c97d3f4b6.jpg',
    '/Users/welldev/Code/self-development/python/photo-1522364723953-452d3431c267.jpg',
    '/Users/welldev/Code/self-development/python/photo-1493976040374-85c8e12f0c0e.jpg',
    '/Users/welldev/Code/self-development/python/photo-1530122037265-a5f1f91d3b99.jpg',
    '/Users/welldev/Code/self-development/python/photo-1516972810927-80185027ca84.jpg',
    '/Users/welldev/Code/self-development/python/photo-1550439062-609e1531270e.jpg',
    '/Users/welldev/Code/self-development/python/photo-1549692520-acc6669e2f0c.jpg'
]

size = (1200, 1200)

def process_image(img_name):
    img = Image.open(img_name)
    
    img = img.filter(ImageFilter.GaussianBlur(15))
    
    img.thumbnail(size)
    
    # Extract just the filename from the full path
    filename = os.path.basename(img_name)
    
    # Save with just the filename in the processed directory
    output_path = f'/Users/welldev/Code/self-development/python/processed/{filename}'
    img.save(output_path)
    
    print(f'{filename} was processed...')
    return filename

if __name__ == '__main__':
    # Create output directory if it doesn't exist
    output_dir = '/Users/welldev/Code/self-development/python/processed'
    os.makedirs(output_dir, exist_ok=True)
    
    t1 = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # IMPORTANT: Must consume the iterator for map() to execute
        results = list(executor.map(process_image, img_names))
    
    t2 = time.perf_counter()
    
    print(f'\nFinished processing {len(results)} images in {round(t2-t1, 2)} seconds')