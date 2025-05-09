"""
Genesis Engine Quantum Steganography Integration Tests

Created: 2025-05-09 06:26:15 UTC
Author: Craig444444444
"""

import unittest
import numpy as np
from PIL import Image
import os
from pathlib import Path
from datetime import datetime

from quantum_stego.core import QuantumSteganography
from quantum_stego.modes import SteganoMode
from quantum_stego.quantum_features import QuantumFeatures, QuantumMetadata
from quantum_stego.security import QuantumSecurity
from quantum_stego.exceptions import *

class TestQuantumSteganographyIntegration(unittest.TestCase):
    """Integration test suite for Quantum Steganography module."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.test_dir = Path(__file__).parent / "test_data"
        cls.test_dir.mkdir(exist_ok=True)
        
        # Create test image
        cls.test_image = cls._create_test_image()
        cls.test_image_path = cls.test_dir / "test_image.png"
        cls.test_image.save(cls.test_image_path)
        
        # Initialize components
        cls.stego = QuantumSteganography()
        cls.quantum_features = QuantumFeatures()
        cls.security = QuantumSecurity()
    
    @staticmethod
    def _create_test_image(size=(100, 100)):
        """Create test image with φ-modulated patterns."""
        phi = (1 + 5 ** 0.5) / 2
        x = np.linspace(0, 1, size[0])
        y = np.linspace(0, 1, size[1])
        X, Y = np.meshgrid(x, y)
        Z = np.sin(2 * np.pi * phi * X) * np.cos(2 * np.pi * phi * Y)
        img_array = ((Z + 1) * 127.5).astype(np.uint8)
        return Image.fromarray(img_array)
    
    def test_full_encryption_workflow(self):
        """Test complete encryption workflow."""
        try:
            # Generate test data
            test_data = "test_content_type"
            output_path = self.test_dir / "encrypted_image.png"
            
            # Encode data
            result = self.stego.encode(
                str(self.test_image_path),
                str(output_path),
                test_data
            )
            self.assertTrue(result)
            
            # Verify file exists
            self.assertTrue(output_path.exists())
            
            # Decode and verify
            decoded = self.stego.decode(str(output_path))
            self.assertEqual(decoded, test_data)
            
        except Exception as e:
            self.fail(f"Encryption workflow failed: {e}")
    
    def test_quantum_features_integration(self):
        """Test quantum features integration."""
        try:
            # Test data
            test_array = np.random.random((10, 10))
            
            # Apply quantum transform
            transformed = self.quantum_features.apply_quantum_transform(test_array)
            self.assertEqual(transformed.shape, test_array.shape)
            
            # Generate superposition states
            states = self.quantum_features.get_superposition_state(test_array)
            self.assertEqual(len(states), 2)
            
        except Exception as e:
            self.fail(f"Quantum features integration failed: {e}")
    
    def test_security_features_integration(self):
        """Test security features integration."""
        try:
            # Test data
            test_array = np.random.random((10, 10))
            
            # Apply watermark
            watermarked = self.security.apply_quantum_watermark(test_array)
            self.assertTrue(
                self.security.verify_quantum_watermark(watermarked)
            )
            
            # Test encryption
            key = "test_key"
            encrypted, token = self.security.apply_quantum_encryption(
                test_array, key
            )
            self.assertTrue(
                self.security.verify_quantum_encryption(encrypted, token)
            )
            
        except Exception as e:
            self.fail(f"Security features integration failed: {e}")
    
    def test_error_handling(self):
        """Test error handling integration."""
        try:
            # Test invalid image path
            with self.assertRaises(QuantumStegoError):
                self.stego.encode(
                    "invalid_path.png",
                    "output.png",
                    "test_data"
                )
            
            # Test invalid quantum state
            with self.assertRaises(QuantumStateError):
                self.quantum_features.apply_quantum_transform(
                    np.array(['invalid'])
                )
                
            # Test invalid encryption
            with self.assertRaises(QuantumSecurityError):
                self.security.verify_quantum_encryption(
                    np.zeros((10, 10)),
                    "invalid_token"
                )
                
        except Exception as e:
            self.fail(f"Error handling integration failed: {e}")
    
    def test_mode_integration(self):
        """Test steganography modes integration."""
        try:
            for mode in SteganoMode:
                # Create test image for each mode
                test_image = self._create_test_image()
                
                # Test encoding
                result = mode.encode(
                    test_image,
                    "test_hash"
                )
                self.assertTrue(result)
                
                # Test decoding
                decoded = mode.decode(test_image)
                self.assertIsInstance(decoded, str)
                
        except Exception as e:
            self.fail(f"Mode integration failed: {e}")
    
    def test_metadata_integration(self):
        """Test metadata integration."""
        try:
            metadata = QuantumMetadata()
            
            # Record states
            test_array = np.random.random((10, 10))
            metadata.record_quantum_state(test_array)
            
            # Verify history
            state_history = metadata.get_state_history()
            self.assertGreater(len(state_history), 0)
            
            # Verify phi modulation stats
            stats = metadata.get_phi_modulation_stats()
            self.assertIn('mean', stats)
            self.assertIn('std', stats)
            
        except Exception as e:
            self.fail(f"Metadata integration failed: {e}")
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment."""
        try:
            import shutil
            shutil.rmtree(cls.test_dir)
        except Exception as e:
            print(f"Cleanup failed: {e}")

if __name__ == '__main__':
    unittest.main()
