import os
from zipfile import ZipFile, ZIP_STORED, ZIP_DEFLATED
from PIL import Image


def compress_image(input_path, output_path, quality=60, max_width=1200):
    with Image.open(input_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        if img.width > max_width:
            ratio = max_width / img.width
            new_size = (max_width, int(img.height * ratio))
            img = img.resize(new_size, Image.ANTIALIAS)
        img.save(output_path, format='JPEG', quality=quality, optimize=True)


def optimize_epub(epub_file_path, output_epub_path):
    import tempfile
    import shutil

    with tempfile.TemporaryDirectory() as temp_dir:
        extract_path = os.path.join(temp_dir, "extracted")
        os.makedirs(extract_path, exist_ok=True)

        with ZipFile(epub_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        # Optimize images
        for root, _, files in os.walk(extract_path):
            for file in files:
                if file.lower().endswith(".jpg"):
                    full_path = os.path.join(root, file)
                    compress_image(full_path, full_path)

        # Create optimized EPUB
        with ZipFile(output_epub_path, 'w') as new_epub:
            mimetype_path = os.path.join(extract_path, 'mimetype')
            new_epub.write(mimetype_path, arcname='mimetype', compress_type=ZIP_STORED)

            for foldername, _, filenames in os.walk(extract_path):
                for filename in filenames:
                    full_path = os.path.join(foldername, filename)
                    rel_path = os.path.relpath(full_path, extract_path)
                    if rel_path == 'mimetype':
                        continue
                    new_epub.write(full_path, arcname=rel_path, compress_type=ZIP_DEFLATED)


# Example usage:
# optimize_epub("/path/to/original.epub", "/path/to/optimized.epub")
