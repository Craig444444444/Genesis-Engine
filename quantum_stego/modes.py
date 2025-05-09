"""
Genesis Engine Quantum Steganography Modes

Created: 2025-05-09 06:12:04 UTC
Author: Craig444444444
"""

from enum import Enum
from PIL import Image
import numpy as np
from typing import Optional, List, Tuple

class SteganoMode(Enum):
    """
    Quantum-inspired steganographic modes.
    Each mode represents a different approach to data embedding.
    """
    PSI = "ψ"  # Quantum superposition mode
    PHI = "φ"  # Golden ratio mode
    TAU = "τ"  # Technical mode
    
    def encode(self, 
               img: Image.Image, 
               data_hash: str,
               positions: Optional[List[Tuple[int, int]]] = None) -> bool:
        """
        Encode data using the selected mode's algorithm.
        """
        if self == SteganoMode.PSI:
            return self._encode_psi(img, data_hash)
        elif self == SteganoMode.PHI:
            return self._encode_phi(img, data_hash, positions)
        else:
            return self._encode_tau(img, data_hash)
    
    def decode(self, img: Image.Image) -> str:
        """
        Decode data using the selected mode's algorithm.
        """
        if self == SteganoMode.PSI:
            return self._decode_psi(img)
        elif self == SteganoMode.PHI:
            return self._decode_phi(img)
        else:
            return self._decode_tau(img)
    
    def _encode_psi(self, img: Image.Image, data_hash: str) -> bool:
        """Quantum superposition mode encoding."""
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        
        pixels = img.load()
        width, height = img.size
        binary_data = ''.join(format(ord(c), '08b') for c in data_hash)
        
        try:
            for i, bit in enumerate(binary_data):
                if i >= width * height:
                    break
                x, y = i % width, i // width
                r, g, b, a = pixels[x, y]
                a = (a & ~1) | int(bit)
                pixels[x, y] = (r, g, b, a)
            return True
        except Exception:
            return False
    
    def _encode_phi(self, 
                   img: Image.Image, 
                   data_hash: str,
                   positions: Optional[List[Tuple[int, int]]] = None) -> bool:
        """Golden ratio mode encoding."""
        pixels = img.load()
        binary_data = ''.join(format(ord(c), '08b') for c in data_hash)
        
        try:
            if positions:
                for i, bit in enumerate(binary_data):
                    if i >= len(positions):
                        break
                    x, y = positions[i]
                    r, g, b = pixels[x, y]
                    r = (r & ~1) | int(bit)
                    pixels[x, y] = (r, g, b)
            else:
                # Default sequential embedding if no positions provided
                width, height = img.size
                for i, bit in enumerate(binary_data):
                    if i >= width * height:
                        break
                    x, y = i % width, i // width
                    r, g, b = pixels[x, y]
                    r = (r & ~1) | int(bit)
                    pixels[x, y] = (r, g, b)
            return True
        except Exception:
            return False
    
    def _encode_tau(self, img: Image.Image, data_hash: str) -> bool:
        """Technical mode encoding using multi-channel LSB."""
        pixels = img.load()
        width, height = img.size
        binary_data = ''.join(format(ord(c), '08b') for c in data_hash)
        
        try:
            for i, bit in enumerate(binary_data):
                if i >= width * height:
                    break
                x, y = i % width, i // width
                r, g, b = pixels[x, y]
                r = (r & ~0b11) | (int(bit) << 1)
                g = (g & ~0b1) | int(bit)
                pixels[x, y] = (r, g, b)
            return True
        except Exception:
            return False
    
    def _decode_psi(self, img: Image.Image) -> str:
        """Quantum superposition mode decoding."""
        if img.mode != "RGBA":
            return ""
            
        pixels = img.load()
        width, height = img.size
        binary_data = ""
        
        try:
            for y in range(height):
                for x in range(width):
                    if len(binary_data) >= 512:  # 64 bytes * 8 bits
                        break
                    _, _, _, a = pixels[x, y]
                    binary_data += str(a & 1)
                    
            # Convert binary to string
            chars = []
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                if len(byte) == 8:
                    chars.append(chr(int(byte, 2)))
            return ''.join(chars)
        except Exception:
            return ""
    
    def _decode_phi(self, img: Image.Image) -> str:
        """Golden ratio mode decoding."""
        pixels = img.load()
        width, height = img.size
        binary_data = ""
        
        try:
            for y in range(height):
                for x in range(width):
                    if len(binary_data) >= 512:
                        break
                    r, _, _ = pixels[x, y]
                    binary_data += str(r & 1)
                    
            chars = []
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                if len(byte) == 8:
                    chars.append(chr(int(byte, 2)))
            return ''.join(chars)
        except Exception:
            return ""
    
    def _decode_tau(self, img: Image.Image) -> str:
        """Technical mode decoding."""
        pixels = img.load()
        width, height = img.size
        binary_data = ""
        
        try:
            for y in range(height):
                for x in range(width):
                    if len(binary_data) >= 512:
                        break
                    r, _, _ = pixels[x, y]
                    binary_data += str((r >> 1) & 1)
                    
            chars = []
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                if len(byte) == 8:
                    chars.append(chr(int(byte, 2)))
            return ''.join(chars)
        except Exception:
            return ""
