"""
نظام خبير استخراج أحكام التجويد من النصوص القرآنية
Expert System for Extracting Tajweed Rules from Quranic Text

Version: 1.0
Author: Mahmoud-AlRaaei
"""

__version__ = "1.0"
__author__ = "Mahmoud-AlRaaei"
__description__ = "Expert System for Extracting Tajweed Rules from Quranic Text"

from .text_processor import TextProcessor
from .rule_engine import RuleEngine
from .ml_model import MLModel

__all__ = ['TextProcessor', 'RuleEngine', 'MLModel']
