import json
import os
import shutil
from datetime import datetime
from typing import List, Dict, Any

class Pet:
    def __init__(self, name: str):
        """Initialize a new pet with given name."""
        self.name = name
        self.health = 100
        self.happiness = 100
        self.energy = 100
        self.tricks = []
        self.documents = {}  # Store uploaded documents
        self.profile_picture = None
        self.creation_date = datetime.now().isoformat()
        
        # Create pet's document directory
        self.pet_dir = f"pet_data/{self.name.replace(' ', '_')}"
        os.makedirs(self.pet_dir, exist_ok=True)
        os.makedirs(f"{self.pet_dir}/images", exist_ok=True)
        os.makedirs(f"{self.pet_dir}/documents", exist_ok=True)
    
    def eat(self):
        """Feed the pet to increase health and happiness."""
        if self.health < 100:
            self.health = min(100, self.health + 20)
            self.happiness = min(100, self.happiness + 10)
            print(f"🍖 {self.name} enjoyed the meal! Health and happiness increased.")
        else:
            print(f"🍖 {self.name} is already well-fed!")
    
    def play(self):
        """Play with the pet to increase happiness but decrease energy."""
        if self.energy > 20:
            self.happiness = min(100, self.happiness + 25)
            self.energy = max(0, self.energy - 20)
            print(f"⚽ {self.name} had a great time playing! Happiness increased.")
        else:
            print(f"😴 {self.name} is too tired to play. Let them rest first!")
    
    def train(self, trick: str):
        """Teach the pet a new trick."""
        if trick.lower() not in [t.lower() for t in self.tricks]:
            self.tricks.append(trick)
            self.happiness = min(100, self.happiness + 15)
            self.energy = max(0, self.energy - 10)
            print(f"🎓 {self.name} learned a new trick: {trick}!")
        else:
            print(f"🎓 {self.name} already knows this trick!")
    
    def sleep(self):
        """Let the pet sleep to restore energy."""
        self.energy = 100
        self.health = min(100, self.health + 10)
        print(f"😴 {self.name} had a good rest! Energy restored.")
    
    def get_status(self):
        """Display the pet's current status."""
        print(f"\n📊 {self.name}'s Status:")
        print(f"   Health: {self.health}/100")
        print(f"   Happiness: {self.happiness}/100")
        print(f"   Energy: {self.energy}/100")
        print(f"   Tricks Known: {len(self.tricks)}")
        if self.profile_picture:
            print(f"   Profile Picture: {self.profile_picture}")
        if self.documents:
            print(f"   Documents: {len(self.documents)} uploaded")
    
    def show_tricks(self):
        """Display all tricks the pet knows."""
        if self.tricks:
            print(f"🎭 {self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"   {i}. {trick}")
        else:
            print(f"🎭 {self.name} doesn't know any tricks yet.")
    
    def upload_document(self, file_path: str, document_type: str = "general") -> bool:
        """
        Upload a document for the pet.
        
        Args:
            file_path (str): Path to the file to upload
            document_type (str): Type of document (profile, medical, training, general)
            
        Returns:
            bool: True if upload successful, False otherwise
        """
        try:
            if not os.path.exists(file_path):
                print(f"❌ Error: File '{file_path}' not found.")
                return False
            
            # Get file info
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_extension = os.path.splitext(file_name)[1].lower()
            
            # Check file size (limit to 10MB)
            if file_size > 10 * 1024 * 1024:
                print(f"❌ Error: File too large. Maximum size is 10MB.")
                return False
            
            # Determine destination directory
            if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                dest_dir = f"{self.pet_dir}/images"
                if document_type == "profile":
                    # Special handling for profile pictures
                    dest_path = f"{dest_dir}/profile{file_extension}"
                    self.profile_picture = dest_path
                else:
                    dest_path = f"{dest_dir}/{file_name}"
            else:
                dest_dir = f"{self.pet_dir}/documents"
                dest_path = f"{dest_dir}/{file_name}"
            
            # Copy the file
            shutil.copy2(file_path, dest_path)
            
            # Store document metadata
            doc_id = f"{document_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            self.documents[doc_id] = {
                "original_name": file_name,
                "stored_path": dest_path,
                "document_type": document_type,
                "file_size": file_size,
                "upload_date": datetime.now().isoformat(),
                "file_extension": file_extension
            }
            
            print(f"✅ Successfully uploaded '{file_name}' as {document_type} document.")
            self.save_pet_data()
            return True
            
        except Exception as e:
            print(f"❌ Error uploading document: {str(e)}")
            return False
    
    def list_documents(self):
        """List all uploaded documents for the pet."""
        if not self.documents:
            print(f"📁 No documents uploaded for {self.name} yet.")
            return
        
        print(f"📁 Documents for {self.name}:")
        for doc_id, doc_info in self.documents.items():
            print(f"   📄 {doc_info['original_name']}")
            print(f"      Type: {doc_info['document_type']}")
            print(f"      Size: {doc_info['file_size']} bytes")
            print(f"      Uploaded: {doc_info['upload_date']}")
            print()
    
    def delete_document(self, document_name: str) -> bool:
        """
        Delete a specific document.
        
        Args:
            document_name (str): Name of the document to delete
            
        Returns:
            bool: True if deletion successful, False otherwise
        """
        try:
            # Find the document by name
            doc_to_delete = None
            for doc_id, doc_info in self.documents.items():
                if doc_info['original_name'] == document_name:
                    doc_to_delete = doc_id
                    break
            
            if not doc_to_delete:
                print(f"❌ Document '{document_name}' not found.")
                return False
            
            # Delete the physical file
            file_path = self.documents[doc_to_delete]['stored_path']
            if os.path.exists(file_path):
                os.remove(file_path)
            
            # Remove from documents dict
            del self.documents[doc_to_delete]
            
            # Update profile picture if it was deleted
            if self.profile_picture and self.profile_picture == file_path:
                self.profile_picture = None
            
            print(f"✅ Successfully deleted '{document_name}'.")
            self.save_pet_data()
            return True
            
        except Exception as e:
            print(f"❌ Error deleting document: {str(e)}")
            return False
    
    def save_pet_data(self):
        """Save pet data to a JSON file."""
        try:
            pet_data = {
                "name": self.name,
                "health": self.health,
                "happiness": self.happiness,
                "energy": self.energy,
                "tricks": self.tricks,
                "documents": self.documents,
                "profile_picture": self.profile_picture,
                "creation_date": self.creation_date,
                "last_saved": datetime.now().isoformat()
            }
            
            with open(f"{self.pet_dir}/pet_data.json", 'w') as f:
                json.dump(pet_data, f, indent=2)
                
        except Exception as e:
            print(f"❌ Error saving pet data: {str(e)}")
    
    def load_pet_data(self):
        """Load pet data from a JSON file."""
        try:
            data_file = f"{self.pet_dir}/pet_data.json"
            if os.path.exists(data_file):
                with open(data_file, 'r') as f:
                    pet_data = json.load(f)
                
                self.health = pet_data.get('health', 100)
                self.happiness = pet_data.get('happiness', 100)
                self.energy = pet_data.get('energy', 100)
                self.tricks = pet_data.get('tricks', [])
                self.documents = pet_data.get('documents', {})
                self.profile_picture = pet_data.get('profile_picture')
                self.creation_date = pet_data.get('creation_date', datetime.now().isoformat())
                
                print(f"✅ Loaded saved data for {self.name}.")
                return True
        except Exception as e:
            print(f"❌ Error loading pet data: {str(e)}")
        
        return False

    @staticmethod
    def create_sample_document(filename: str, content: str):
        """Create a sample document for testing upload functionality."""
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"✅ Created sample document: {filename}")
            return True
        except Exception as e:
            print(f"❌ Error creating sample document: {str(e)}")
            return False