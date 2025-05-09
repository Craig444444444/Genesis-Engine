"""
Genesis Engine Quantum Steganography Exceptions

Created: 2025-05-09 06:16:57 UTC
Author: Craig444444444
"""

class QuantumStegoError(Exception):
    """Base exception for quantum steganography operations."""
    def __init__(self, message: str = "Quantum steganography operation failed"):
        self.timestamp = "2025-05-09 06:16:57"
        self.message = f"[{self.timestamp}] {message}"
        super().__init__(self.message)

class QuantumStateError(QuantumStegoError):
    """
    Raised when quantum state becomes invalid.
    
    Common causes:
    - State decoherence
    - Invalid superposition
    - φ-modulation failure
    """
    def __init__(self, message: str = "Invalid quantum state"):
        super().__init__(f"Quantum State Error: {message}")

class PhiModulationError(QuantumStegoError):
    """
    Raised when φ-modulation fails.
    
    Common causes:
    - Invalid φ value
    - Modulation overflow
    - Pattern disruption
    """
    def __init__(self, message: str = "φ-modulation failed"):
        super().__init__(f"φ-Modulation Error: {message}")

class EntropyPoolError(QuantumStegoError):
    """
    Raised when entropy pool is depleted.
    
    Common causes:
    - Insufficient entropy
    - Pool exhaustion
    - Generation failure
    """
    def __init__(self, message: str = "Entropy pool depleted"):
        super().__init__(f"Entropy Pool Error: {message}")

class QuantumChecksumError(QuantumStegoError):
    """
    Raised when quantum checksum verification fails.
    
    Common causes:
    - Data corruption
    - Invalid checksum
    - Verification mismatch
    """
    def __init__(self, message: str = "Checksum verification failed"):
        super().__init__(f"Quantum Checksum Error: {message}")

class TemporalPatternError(QuantumStegoError):
    """
    Raised when temporal pattern analysis fails.
    
    Common causes:
    - Pattern disruption
    - Temporal inconsistency
    - Analysis failure
    """
    def __init__(self, message: str = "Temporal pattern analysis failed"):
        super().__init__(f"Temporal Pattern Error: {message}")

class EthicalValidationError(QuantumStegoError):
    """
    Raised when ethical validation fails.
    
    Common causes:
    - Content violation
    - Policy breach
    - Validation failure
    """
    def __init__(self, message: str = "Ethical validation failed"):
        super().__init__(f"Ethical Validation Error: {message}")

class QuantumSecurityError(QuantumStegoError):
    """
    Raised when security operations fail.
    
    Common causes:
    - Encryption failure
    - Watermark verification
    - Security breach
    """
    def __init__(self, message: str = "Security operation failed"):
        super().__init__(f"Quantum Security Error: {message}")

# Error code mapping for system integration
ERROR_CODES = {
    QuantumStateError: 1001,
    PhiModulationError: 1002,
    EntropyPoolError: 1003,
    QuantumChecksumError: 1004,
    TemporalPatternError: 1005,
    EthicalValidationError: 1006,
    QuantumSecurityError: 1007
}

def get_error_code(error: QuantumStegoError) -> int:
    """Get system error code for exception type."""
    return ERROR_CODES.get(type(error), 1000)
