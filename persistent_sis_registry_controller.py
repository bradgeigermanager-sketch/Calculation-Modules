import os
import json

class DistributedSISController(SISRegistryController):
    def load_registry_directory(self, directory_path: str):
        """Crawls a directory, loads all JSON modules, and registers them."""
        for filename in os.listdir(directory_path):
            if filename.endswith(".json"):
                with open(os.path.join(directory_path, filename), 'r') as f:
                    module_data = json.load(f)
                    
                    # Registering the module dynamically
                    self.register_module(
                        uid=module_data["uid"],
                        metadata=module_data["metadata"],
                        schema=module_data["schema"],
                        formula=self._lookup_logic(module_data["formula_ref"])
                    )
        print(f"[SIS] Distributed registry loaded from {directory_path}.")
        
