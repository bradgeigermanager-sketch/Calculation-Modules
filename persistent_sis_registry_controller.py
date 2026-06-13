import json

class PersistentSISController(SISRegistryController):
    def load_manifest(self, filepath: str):
        """Loads and syncs the library from a persistent JSON file."""
        with open(filepath, 'r') as f:
            manifest = json.load(f)
            
        for uid, data in manifest.items():
            # In a production SIS, formula_ref would map to an importable library function
            # Here, we re-register using the dynamic definition
            self.register_module(
                uid=uid,
                metadata=data["metadata"],
                schema=data["schema"],
                formula=self._lookup_logic(data["formula_ref"])
            )
        print(f"[SIS] Manifest loaded from {filepath}.")

    from formula_library import FORMULA_REGISTRY

    def _lookup_logic(self, ref: str):
    """Maps manifest reference strings to actual executable functions."""
        return FORMULA_REGISTRY.get(ref)
