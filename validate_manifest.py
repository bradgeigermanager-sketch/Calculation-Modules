from pydantic import BaseModel, Field, validator
from typing import List, Dict

class ModuleMetadata(BaseModel):
    label: str
    category: str

class RegistryEntry(BaseModel):
    metadata: ModuleMetadata
    schema_fields: List[str] = Field(..., alias="schema")
    formula_ref: str

class SISManifest(BaseModel):
    __root__: Dict[str, RegistryEntry]

# --- VALIDATION USAGE ---
import json

def validate_manifest(filepath: str):
    with open(filepath, 'r') as f:
        data = json.load(f)
    # This will raise a ValidationError if the JSON doesn't match the schema
    manifest = SISManifest.parse_obj(data)
    print("[SIS] Manifest integrity verified.")
    return manifest
