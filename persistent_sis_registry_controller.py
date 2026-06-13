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

    def _lookup_logic(self, ref: str):
        """Maps manifest reference strings to actual executable functions."""
        logic_map = {
            "FIN_001_LOGIC": lambda d: abs(d['v1'] - d['v2']) / ((d['v1'] + d['v2']) / 2) * 100
        }
        return logic_map.get(ref)
