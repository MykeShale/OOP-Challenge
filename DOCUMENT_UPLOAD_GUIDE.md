# 📁 Document Upload Guide - Pet Simulator

This guide explains how to upload, manage, and organize documents in the Pet Simulator application.

## 🚀 Quick Start

### Through the Main Application
1. Run the Pet Simulator: `python main.py`
2. Create or select your pet
3. Choose option **7** (Upload a document)
4. Select document type and provide file path
5. Your document will be uploaded and organized automatically

### Programmatically
```python
import pet

# Create a pet
my_pet = pet.Pet("Fluffy")

# Upload a document
my_pet.upload_document("path/to/file.txt", "general")

# List uploaded documents
my_pet.list_documents()
```

## 📂 Document Types

The system supports four main document categories:

| Type | Description | Examples |
|------|-------------|----------|
| **profile** | Pet profile pictures | Photos, avatars |
| **medical** | Health and medical records | Vet records, vaccination cards |
| **training** | Training certificates and records | Obedience certificates, training logs |
| **general** | Any other documents | Notes, care instructions, misc files |

## 🗂️ File Organization

Documents are automatically organized in the following structure:

```
pet_data/
└── {pet_name}/
    ├── images/          # Profile pictures and other images
    │   └── profile.jpg  # Special: pet's profile picture
    ├── documents/       # All other document types
    │   ├── medical_records.pdf
    │   ├── training_cert.jpg
    │   └── care_notes.txt
    └── pet_data.json   # Pet metadata and document index
```

## 📋 Supported File Types

### Images
- `.jpg`, `.jpeg` - JPEG images
- `.png` - PNG images  
- `.gif` - GIF images
- `.bmp` - Bitmap images

### Documents
- `.pdf` - PDF documents
- `.txt` - Text files
- `.doc`, `.docx` - Word documents
- Any other file type (up to 10MB)

## ⚙️ Features

### ✅ Upload Documents
```python
# Basic upload
pet.upload_document("file.txt", "general")

# Upload profile picture
pet.upload_document("photo.jpg", "profile")

# Upload medical record
pet.upload_document("vet_record.pdf", "medical")
```

### 📋 List Documents
```python
# Show all uploaded documents with details
pet.list_documents()
```

### 🗑️ Delete Documents
```python
# Delete by filename
pet.delete_document("old_photo.jpg")
```

### 💾 Automatic Saving
- Pet data and document metadata are automatically saved
- Documents are safely copied to pet's directory
- Original files remain untouched

## 🔧 Advanced Usage

### Custom Document Organization
```python
# Create multiple pets with separate document stores
pet1 = pet.Pet("Fluffy")
pet2 = pet.Pet("Max")

# Each pet has independent document storage
pet1.upload_document("fluffy_photo.jpg", "profile")
pet2.upload_document("max_photo.jpg", "profile")
```

### Batch Upload Example
```python
documents = [
    ("medical_record.pdf", "medical"),
    ("training_cert.jpg", "training"),
    ("care_notes.txt", "general")
]

for file_path, doc_type in documents:
    my_pet.upload_document(file_path, doc_type)
```

### Document Metadata
Each uploaded document stores:
- Original filename
- File size
- Upload timestamp
- Document type
- Storage location
- File extension

## 🚦 Limitations

- **File Size**: Maximum 10MB per file
- **Storage**: Limited by available disk space
- **File Names**: Duplicate names are handled automatically
- **Security**: Files are copied, not moved (originals preserved)

## 🔍 Troubleshooting

### Common Issues

**File Not Found**
```
❌ Error: File 'document.pdf' not found.
```
- **Solution**: Check file path and ensure file exists

**File Too Large**
```
❌ Error: File too large. Maximum size is 10MB.
```
- **Solution**: Compress file or use smaller file

**Permission Error**
```
❌ Error uploading document: [Errno 13] Permission denied
```
- **Solution**: Check file permissions and disk space

### Checking Upload Status
```python
# Verify upload success
success = my_pet.upload_document("file.txt", "general")
if success:
    print("Upload successful!")
else:
    print("Upload failed - check error messages")
```

## 🎯 Best Practices

1. **Organize by Type**: Use appropriate document types for better organization
2. **Meaningful Names**: Use descriptive filenames
3. **Regular Cleanup**: Remove old/unnecessary documents
4. **Size Management**: Keep files under 10MB
5. **Backup Important**: Keep backups of critical documents

## 🧪 Testing the Feature

Run the demo script to test document upload functionality:

```bash
python document_upload_demo.py
```

This will:
- Create sample documents
- Demonstrate upload process
- Show document management features
- Clean up test files

## 📞 Integration Examples

### With Main Pet Simulator
The document upload is fully integrated into the main application menu:
- Option 7: Upload document
- Option 8: View documents  
- Option 9: Delete document

### Standalone Usage
```python
from pet import Pet

# Create pet and upload documents independently
my_pet = Pet("Rex")
my_pet.upload_document("important_doc.pdf", "medical")
```

---

*This guide covers all aspects of document management in the Pet Simulator. For additional help, refer to the demo script or examine the source code in `pet.py`.*