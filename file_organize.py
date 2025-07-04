import os
import shutil


source_dir = r"C:\Users\karti\Downloads"  


file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Executables": [".exe", ".msi"]
}


for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)
    
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        ext = ext.lower()
        
        moved = False
        for category, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(source_dir, category)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved: {file} → {category}")
                moved = True
                break
        
        if not moved:
            other_path = os.path.join(source_dir, "Others")
            os.makedirs(other_path, exist_ok=True)
            shutil.move(file_path, os.path.join(other_path, file))
            print(f"Moved: {file} → Others")

print("✅ Organizing Complete.")
