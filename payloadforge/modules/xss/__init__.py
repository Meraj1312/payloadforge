"""
SQL Injection Module for PayloadForge
Educational purpose only - Payload templates for learning
"""

from .base_module import SQLiModule
from .sqli_payloads import PayloadTemplates
from .sqli_obfuscation import SQLObfuscator
from .sqli_signatures import DatabaseSignatures

__all__ = ['SQLiModule', 'PayloadTemplates', 'SQLObfuscator', 'DatabaseSignatures']
