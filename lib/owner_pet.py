class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate the pet_type
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner  # Set the owner

        # If the pet has an owner, automatically add the pet to the owner's list
        if owner:
            owner.add_pet(self)
        
        # Add this pet to the class-level list of all pets
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name}, pet_type={self.pet_type}, owner={self.owner.name if self.owner else None}>"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        # Ensure the pet being added is an instance of the Pet class
        if isinstance(pet, Pet):
            pet.owner = self  # Assign the owner to the pet
            self._pets.append(pet)
        else:
            raise ValueError("Can only add instances of Pet")

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        # Sort pets by their name
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"<Owner name={self.name}>"
