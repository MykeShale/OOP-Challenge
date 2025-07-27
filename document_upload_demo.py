#!/usr/bin/env python3
"""
Document Upload Demo for Pet Simulator

This script demonstrates how to upload documents to the Pet Simulator.
It creates sample documents and shows various upload scenarios.
"""

import pet
import os
import time

def create_sample_files():
    """Create sample files for demonstration."""
    print("Creating sample files for demonstration...")
    
    # Create sample documents
    sample_files = {
        "pet_medical_record.txt": """
Pet Medical Record
==================
Pet Name: [To be filled]
Date of Birth: January 1, 2024
Breed: Mixed
Vaccinations:
- Rabies: Up to date
- DHPP: Up to date
Last Checkup: December 2024
Notes: Healthy and active pet
        """.strip(),
        
        "training_certificate.txt": """
Pet Training Certificate
========================
This certifies that [Pet Name] has successfully completed:
- Basic Obedience Training
- House Training
- Social Skills Training

Certified by: Pet Training Academy
Date: December 2024
        """.strip(),
        
        "pet_notes.txt": """
Pet Care Notes
==============
Daily Schedule:
- 7:00 AM: Morning meal
- 12:00 PM: Playtime
- 6:00 PM: Evening meal
- 9:00 PM: Walk

Favorite Activities:
- Playing fetch
- Learning new tricks
- Sleeping in sunny spots

Special Instructions:
- Loves belly rubs
- Responds well to positive reinforcement
        """.strip()
    }
    
    for filename, content in sample_files.items():
        with open(filename, 'w') as f:
            f.write(content)
        print(f"✅ Created: {filename}")
    
    print("Sample files created successfully!\n")
    return list(sample_files.keys())

def demo_document_upload():
    """Demonstrate document upload functionality."""
    print("🐾 Pet Simulator - Document Upload Demo")
    print("=" * 50)
    
    # Create sample files
    sample_files = create_sample_files()
    
    # Create a test pet
    pet_name = "Demo Pet"
    test_pet = pet.Pet(pet_name)
    
    print(f"Created pet: {pet_name}")
    print(f"Pet directory: {test_pet.pet_dir}")
    
    # Demonstrate different types of uploads
    uploads = [
        (sample_files[0], "medical"),
        (sample_files[1], "training"),
        (sample_files[2], "general")
    ]
    
    print("\n📁 Uploading sample documents...")
    for file_path, doc_type in uploads:
        print(f"\nUploading {file_path} as {doc_type} document...")
        success = test_pet.upload_document(file_path, doc_type)
        if success:
            print(f"✅ Upload successful!")
        else:
            print(f"❌ Upload failed!")
        time.sleep(1)
    
    # Show pet status with documents
    print("\n" + "=" * 50)
    test_pet.get_status()
    
    # List all documents
    print("\n" + "=" * 50)
    test_pet.list_documents()
    
    # Demonstrate document deletion
    print("\n" + "=" * 50)
    print("Demonstrating document deletion...")
    print(f"Deleting: {sample_files[2]}")
    test_pet.delete_document(os.path.basename(sample_files[2]))
    
    print("\nDocuments after deletion:")
    test_pet.list_documents()
    
    # Clean up sample files
    print("\n" + "=" * 50)
    print("Cleaning up sample files...")
    for filename in sample_files:
        try:
            os.remove(filename)
            print(f"🗑️  Removed: {filename}")
        except FileNotFoundError:
            pass
    
    print("\n✅ Demo completed!")

def show_usage_examples():
    """Show examples of how to use document upload."""
    print("\n📖 How to Upload Documents - Usage Examples")
    print("=" * 50)
    
    examples = [
        {
            "title": "Upload a Profile Picture",
            "code": """
# Create a pet
my_pet = pet.Pet("Fluffy")

# Upload a profile picture
my_pet.upload_document("path/to/fluffy_photo.jpg", "profile")
            """.strip()
        },
        {
            "title": "Upload Medical Records",
            "code": """
# Upload medical documents
my_pet.upload_document("vet_records.pdf", "medical")
my_pet.upload_document("vaccination_card.jpg", "medical")
            """.strip()
        },
        {
            "title": "Upload Training Certificates",
            "code": """
# Upload training documents
my_pet.upload_document("obedience_certificate.pdf", "training")
my_pet.upload_document("agility_diploma.jpg", "training")
            """.strip()
        },
        {
            "title": "List and Manage Documents",
            "code": """
# List all uploaded documents
my_pet.list_documents()

# Delete a specific document
my_pet.delete_document("old_photo.jpg")

# Check pet status (includes document count)
my_pet.get_status()
            """.strip()
        }
    ]
    
    for example in examples:
        print(f"\n🔹 {example['title']}:")
        print("-" * 30)
        print(example['code'])
    
    print("\n📋 Supported File Types:")
    print("- Images: .jpg, .jpeg, .png, .gif, .bmp")
    print("- Documents: .pdf, .txt, .doc, .docx, etc.")
    print("- Maximum file size: 10MB")
    
    print("\n📁 Document Organization:")
    print("- Profile pictures: pet_data/{pet_name}/images/")
    print("- Other images: pet_data/{pet_name}/images/")
    print("- Documents: pet_data/{pet_name}/documents/")
    print("- Pet data: pet_data/{pet_name}/pet_data.json")

if __name__ == "__main__":
    print("Starting Pet Simulator Document Upload Demo...")
    print("This demo will create sample files and show upload functionality.\n")
    
    choice = input("Choose an option:\n1. Run interactive demo\n2. Show usage examples\n3. Both\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        demo_document_upload()
    elif choice == "2":
        show_usage_examples()
    elif choice == "3":
        demo_document_upload()
        show_usage_examples()
    else:
        print("Invalid choice. Running full demo...")
        demo_document_upload()
        show_usage_examples()