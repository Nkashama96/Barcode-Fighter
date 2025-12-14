import hashlib

class BarcodeNormalizer:
    """
    Universal normalizer:
    - Accepts any text input (barcode, string, whatever)
    - Converts into SHA3-512 hex digest (128 hex characters)
    """
    @staticmethod
    def normalize(raw_input: str) -> str:
        if raw_input is None:
            raw_input = ""

        raw_input = str(raw_input).strip()
        
        hash_hex = hashlib.sha3_512(raw_input.encode("utf-8")).hexdigest()
        # print(f"Frow raw:{raw_input.encode("utf-8")}")
        # print(f"Normalize:{hash_hex}")
        return hash_hex
