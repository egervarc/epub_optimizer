# EPUB Optimizer

This Python script reduces the file size of `.epub` files by compressing embedded JPEG images and repackaging the EPUB structure correctly.

## Features
- Lossy compression of `.jpg` images using Pillow
- Image resizing to a max width (default: 1200px)
- EPUB unpacking and repacking with correct mimetype placement
- Temporary workspace for safe operations

## Requirements
- Python 3.6+
- Pillow

Install dependencies:
```bash
pip install Pillow
```

## Usage
```python
from epub_optimizer import optimize_epub

optimize_epub("/path/to/original.epub", "/path/to/optimized.epub")
```

## Function Parameters
```python
optimize_epub(epub_file_path, output_epub_path)
```
- `epub_file_path`: Path to the original EPUB file
- `output_epub_path`: Path to save the optimized EPUB file

## Notes
- Only `.jpg` images are compressed
- Image quality is set to 60 by default (adjustable in code)
- Resized images are limited to a width of 1200px

## License
MIT License

---
Developed to help reduce EPUB size for faster downloads and lighter storage.

