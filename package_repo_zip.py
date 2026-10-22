"""
Build a clean, complete repository zip including .git, excluding venv, node_modules, and uncommitted .env
"""
import zipfile
import os
import time

zip_filename = "SmartERP_Enterprise_v1.1.0.zip"
print(f"Creating {zip_filename}...")

# Remove previous zip if exists
if os.path.exists(zip_filename):
    os.remove(zip_filename)

ignored_dirs = {
    ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", "dist", "build"
}
ignored_files = {
    ".env", zip_filename, "smarterp.db", "test_smarterp.db"
}

total_files = 0
total_bytes = 0

with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
    for root, dirs, files in os.walk("."):
        # Filter directories in-place
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        
        for f in files:
            if f in ignored_files or f.endswith(".pyc") or f.endswith(".zip"):
                continue
            
            full_path = os.path.join(root, f)
            arcname = os.path.relpath(full_path, ".")
            
            # Double check no .env files slip into root or backend
            if f == ".env" or f == ".env.example":
                continue

            try:
                zf.write(full_path, arcname)
                total_files += 1
                total_bytes += os.path.getsize(full_path)
            except Exception as e:
                print(f"Skipping {full_path}: {e}")

st = os.stat(zip_filename)
print(f"Zip created successfully!")
print(f"Files included: {total_files}")
print(f"Uncompressed size: {total_bytes / (1024*1024):.2f} MB")
print(f"Compressed zip size: {st.st_size / (1024*1024):.2f} MB")
