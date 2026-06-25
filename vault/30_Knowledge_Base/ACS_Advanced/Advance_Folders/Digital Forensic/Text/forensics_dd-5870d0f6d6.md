---
title: "forensics_dd"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-backend-main\\forensics_dd.py"
source_size_bytes: 8724
source_modified: 2025-11-30T14:49:53
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# forensics_dd

- Source: [forensics_dd.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-backend-main/forensics_dd.py)

## Content

```py
"""
forensics_dd.py

Utility functions for doing basic disk forensics on raw `.dd` images.

This module is designed to be integrated into other Python files in the
project. It uses `pytsk3` (SleuthKit Python bindings) to read partitions
and file systems from a raw image. If `pytsk3` is not available, the
module will raise a clear ImportError with installation instructions.

Functions / classes provided:
- DiskForensics: high-level class to open image, list partitions, list
  files, extract files, and compute hashes.

Notes:
- This script expects sector size 512 when calculating partition offsets.
- Installing `pytsk3` on Windows may require building wheels or using
  prebuilt binaries; see project README for instructions if necessary.
"""
from __future__ import annotations

import hashlib
import os
from typing import List, Dict, Optional

try:
    import pytsk3
except Exception as e:
    raise ImportError(
        "pytsk3 is required for forensics_dd.py. Install it (e.g. `pip install pytsk3`) "
        "or follow platform-specific instructions: https://github.com/py4n6/pytsk" 
    ) from e


class DiskForensics:
    """Class to perform basic operations on a raw `.dd` disk image.

    Usage:
    df = DiskForensics('image.dd')
    df.open_image()
    partitions = df.list_partitions()
    files = df.list_files(partition_index=1, path='/')
    df.extract_file(partition_index=1, file_path='/etc/passwd', dest_path='passwd.dump')
    """

    def __init__(self, image_path: str, sector_size: int = 512):
        self.image_path = image_path
        self.sector_size = sector_size
        self.img: Optional[pytsk3.Img_Info] = None

    def open_image(self) -> None:
        """Open the raw image for use by other methods."""
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image not found: {self.image_path}")
        self.img = pytsk3.Img_Info(self.image_path)

    def list_partitions(self) -> List[Dict]:
        """Return a list of partitions detected in the image.

        Each partition dict contains: index, start (sectors), length (sectors),
        start_byte, description
        """
        if self.img is None:
            self.open_image()

        # Try to read a partition table. If the image has no partition table
        # (for example it is a raw filesystem image rather than a whole-disk
        # image), pytsk3.Volume_Info may raise OSError. In that case we
        # provide a single "virtual" partition starting at sector 0 so callers
        # can still open the filesystem at offset 0.
        parts = []
        try:
            vol = pytsk3.Volume_Info(self.img)
        except OSError:
            # Fallback: treat entire image as a single filesystem starting at 0
            try:
                total_bytes = os.path.getsize(self.image_path)
            except Exception:
                total_bytes = 0
            total_sectors = int(total_bytes // self.sector_size) if self.sector_size else 0
            parts.append({
                'index': 0,
                'start': 0,
                'length': total_sectors,
                'start_byte': 0,
                'description': 'no partition table - raw filesystem',
            })
            return parts

        for i, part in enumerate(vol):
            # Some partitions may be unallocated or metadata-only
            try:
                start = int(part.start)
                length = int(part.len)
            except Exception:
                start = getattr(part, 'start', 0)
                length = getattr(part, 'len', 0)
            parts.append(
                {
                    'index': i,
                    'start': start,
                    'length': length,
                    'start_byte': start * self.sector_size,
                    'description': part.desc.decode('utf-8', errors='ignore') if isinstance(part.desc, bytes) else str(part.desc),
                }
            )
        return parts

    def _open_fs_for_partition(self, partition_index: int) -> pytsk3.FS_Info:
        if self.img is None:
            self.open_image()

        # Attempt to open partition table; if it fails assume a raw
        # filesystem and use offset 0. If partition table exists, use the
        # requested partition index to compute the offset.
        try:
            vol = pytsk3.Volume_Info(self.img)
            part = list(vol)[partition_index]
            offset = int(part.start) * self.sector_size
        except Exception:
            # Fallback to offset 0 (raw filesystem image)
            offset = 0

        fs = pytsk3.FS_Info(self.img, offset=offset)
        return fs

    def list_files(self, partition_index: int = 0, path: str = '/') -> List[Dict]:
        """List entries in a directory at `path` on the given partition.

        Returns list of dicts with `name`, `meta_addr`, `size`, and `type`.
        """
        fs = self._open_fs_for_partition(partition_index)
        try:
            directory = fs.open_dir(path)
        except Exception as e:
            raise FileNotFoundError(f"Cannot open path {path} on partition {partition_index}: {e}")
        entries = []
        for entry in directory:
            name = entry.info.name.name.decode('utf-8', errors='ignore') if isinstance(entry.info.name.name, bytes) else str(entry.info.name.name)
            if name in ['.', '..']:
                continue
            meta = entry.info.meta
            size = getattr(meta, 'size', None) if meta else None
            ftype = getattr(meta, 'type', None) if meta else None
            entries.append({'name': name, 'meta_addr': getattr(meta, 'addr', None), 'size': size, 'type': ftype})
        return entries

    def extract_file(self, partition_index: int, file_path: str, dest_path: str, chunk_size: int = 1024 * 1024) -> None:
        """Extract a file from the image and write it to `dest_path`.

        `file_path` should be the path inside the mounted filesystem (e.g. '/etc/passwd').
        """
        fs = self._open_fs_for_partition(partition_index)
        try:
            file_obj = fs.open(file_path)
        except Exception as e:
            raise FileNotFoundError(f"File not found inside image: {file_path} ({e})")
        meta = file_obj.info.meta
        if not meta:
            raise IOError("No metadata for file; cannot determine size")
        size = meta.size
        with open(dest_path, 'wb') as out_f:
            offset = 0
            while offset < size:
                to_read = min(chunk_size, size - offset)
                data = file_obj.read_random(offset, to_read)
                if not data:
                    break
                out_f.write(data)
                offset += len(data)

    @staticmethod
    def compute_hash(file_path: str, algo: str = 'sha256') -> str:
        """Compute hash of a local file using the specified algorithm.

        Supported algos: any algorithm available in hashlib (e.g., 'md5', 'sha1', 'sha256').
        Returns hex digest string.
        """
        h = hashlib.new(algo)
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                h.update(chunk)
        return h.hexdigest()


def _demo_cli():
    import argparse
    parser = argparse.ArgumentParser(description='Basic `.dd` forensics helper (demo)')
    parser.add_argument('image', help='Path to raw .dd image')
    sub = parser.add_subparsers(dest='cmd')
    sub.add_parser('partitions', help='List partitions')
    lf = sub.add_parser('list', help='List files in directory')
    lf.add_argument('--part', type=int, default=0)
    lf.add_argument('--path', default='/')
    ex = sub.add_parser('extract', help='Extract a file')
    ex.add_argument('--part', type=int, default=0)
    ex.add_argument('--src', required=True, help='Source path inside image')
    ex.add_argument('--dest', required=True, help='Destination path on host')

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return

    df = DiskForensics(args.image)
    if args.cmd == 'partitions':
        for p in df.list_partitions():
            print(f"Index: {p['index']}, start: {p['start']} sectors, len: {p['length']} sectors, start_byte: {p['start_byte']}, desc: {p['description']}")
    elif args.cmd == 'list':
        for e in df.list_files(partition_index=args.part, path=args.path):
            print(f"{e['name']}	{e['size']}")
    elif args.cmd == 'extract':
        print(f"Extracting {args.src} from partition {args.part} to {args.dest}...")
        df.extract_file(partition_index=args.part, file_path=args.src, dest_path=args.dest)
        print('Done.')


if __name__ == '__main__':
    _demo_cli()
```
