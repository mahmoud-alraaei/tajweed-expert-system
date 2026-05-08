"""
معالج النصوص العربية
Arabic Text Processor for Tajweed Analysis

يقوم بـ:
- تنظيف وتشكيل النصوص القرآنية
- تحليل الحروف والكلمات
- استخراج الميزات اللغوية
"""

import re
import unicodedata
from typing import List, Dict, Tuple


class TextProcessor:
    """
    معالج النصوص العربية المتقدم
    Advanced Arabic Text Processor
    """

    # الحروف العربية الأساسية
    ARABIC_LETTERS = {
        'ا': 'alef', 'ب': 'ba', 'ت': 'ta', 'ث': 'tha', 'ج': 'jim',
        'ح': 'ha', 'خ': 'kha', 'د': 'dal', 'ذ': 'dhal', 'ر': 'ra',
        'ز': 'zay', 'س': 'seen', 'ش': 'sheen', 'ص': 'sad', 'ض': 'dad',
        'ط': 'ta', 'ظ': 'za', 'ع': 'ayn', 'غ': 'ghayn', 'ف': 'fa',
        'ق': 'qaf', 'ك': 'kaf', 'ل': 'lam', 'م': 'meem', 'ن': 'noon',
        'ه': 'ha', 'و': 'waw', 'ي': 'ya'
    }

    # الحروف الحلقية (الإظهار)
    THROAT_LETTERS = ['ا', 'ه', 'ع', 'غ', 'ح', 'خ']

    # حروف الإخفاء الحقيقي (15 حرف)
    HIDING_LETTERS = ['ص', 'ذ', 'ت', 'ك', 'ط', 'ف', 'ق', 'ج', 'د', 'ش', 'ز', 'س', 'ب', 'ل', 'ن']

    # حروف الإدغام بغنة (ي، ن، م، و)
    ASSIMILATION_LETTERS = ['ي', 'ن', 'م', 'و']

    # حروف التفخيم
    HEAVY_LETTERS = ['ص', 'ض', 'ط', 'ظ', 'ق', 'غ', 'ر', 'خ']

    def __init__(self):
        """تهيئة معالج النصوص"""
        self.diacritics = {
            'َ': 'fatha',      # الفتحة
            'ُ': 'damma',      # الضمة
            'ِ': 'kasra',      # الكسرة
            'ً': 'fathatan',   # فتحتان
            'ٌ': 'dammatan',   # ضمتان
            'ٍ': 'kasratan',   # كسرتان
            'ْ': 'sukun',      # السكون
            'ّ': 'shadda',     # الشدة
        }

    def process(self, text: str) -> str:
        """
        معالجة النص الأساسية
        
        Args:
            text (str): النص المراد معالجته
            
        Returns:
            str: النص المعالج
        """
        if not text:
            return ""

        # تنظيف النص
        cleaned = self._clean_text(text)
        
        return cleaned

    def _clean_text(self, text: str) -> str:
        """
        تنظيف النص من الأحرف غير المرغوبة
        Clean text from unwanted characters
        
        Args:
            text (str): النص الخام
            
        Returns:
            str: النص المنظف
        """
        # إزالة المسافات الزائدة
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        return text

    def extract_letters(self, text: str) -> List[str]:
        """
        استخراج الحروف من النص
        Extract letters from text
        
        Args:
            text (str): النص المراد تحليله
            
        Returns:
            List[str]: قائمة الحروف
        """
        letters = []
        for char in text:
            if char in self.ARABIC_LETTERS:
                letters.append(char)
        
        return letters

    def extract_words(self, text: str) -> List[str]:
        """
        استخراج الكلمات من النص
        Extract words from text
        
        Args:
            text (str): النص المراد تحليله
            
        Returns:
            List[str]: قائمة الكلمات
        """
        # فصل الكلمات بالمسافات
        words = text.split()
        
        return words

    def analyze_letter_position(self, text: str, letter_index: int) -> Dict:
        """
        تحليل مو��ع الحرف وسياقه
        Analyze letter position and context
        
        Args:
            text (str): النص
            letter_index (int): موقع الحرف
            
        Returns:
            Dict: معلومات الموقع والسياق
        """
        letters = self.extract_letters(text)
        
        if letter_index >= len(letters):
            return {}
        
        current_letter = letters[letter_index]
        previous_letter = letters[letter_index - 1] if letter_index > 0 else None
        next_letter = letters[letter_index + 1] if letter_index < len(letters) - 1 else None
        
        return {
            'current': current_letter,
            'previous': previous_letter,
            'next': next_letter,
            'position': letter_index,
            'is_beginning': letter_index == 0,
            'is_end': letter_index == len(letters) - 1,
        }

    def check_throat_letters(self, letter: str) -> bool:
        """
        التحقق من كون الحرف من الحروف الحلقية
        Check if letter is a throat letter
        
        Args:
            letter (str): الحرف المراد التحقق منه
            
        Returns:
            bool: صحيح إذا كان الحرف حلقياً
        """
        return letter in self.THROAT_LETTERS

    def check_hiding_letters(self, letter: str) -> bool:
        """
        التحقق من كون الحرف من حروف الإخفاء
        Check if letter is a hiding letter
        
        Args:
            letter (str): الحرف المراد التحقق منه
            
        Returns:
            bool: صحيح إذا كان من حروف الإخفاء
        """
        return letter in self.HIDING_LETTERS

    def check_assimilation_letters(self, letter: str) -> bool:
        """
        التحقق من كون الحرف من حروف الإدغام
        Check if letter is an assimilation letter
        
        Args:
            letter (str): الحرف المراد التحقق منه
            
        Returns:
            bool: صحيح إذا كان من حروف الإدغام
        """
        return letter in self.ASSIMILATION_LETTERS

    def check_heavy_letters(self, letter: str) -> bool:
        """
        التحقق من كون الحرف من الحروف المفخمة
        Check if letter is a heavy (emphasized) letter
        
        Args:
            letter (str): الحرف المراد التحقق منه
            
        Returns:
            bool: صحيح إذا كان من الحروف المفخمة
        """
        return letter in self.HEAVY_LETTERS

    def extract_features(self, text: str) -> Dict:
        """
        استخراج الميزات اللغوية من النص
        Extract linguistic features from text
        
        Args:
            text (str): النص المراد تحليله
            
        Returns:
            Dict: قاموس يحتوي على الميزات المختلفة
        """
        letters = self.extract_letters(text)
        words = self.extract_words(text)
        
        features = {
            'text': text,
            'letter_count': len(letters),
            'word_count': len(words),
            'letters': letters,
            'words': words,
            'throat_letters_count': sum(1 for l in letters if self.check_throat_letters(l)),
            'hiding_letters_count': sum(1 for l in letters if self.check_hiding_letters(l)),
            'heavy_letters_count': sum(1 for l in letters if self.check_heavy_letters(l)),
        }
        
        return features

    def get_letter_name(self, letter: str) -> str:
        """
        الحصول على اسم الحرف العربي
        Get the name of an Arabic letter
        
        Args:
            letter (str): الحرف
            
        Returns:
            str: اسم الحرف
        """
        return self.ARABIC_LETTERS.get(letter, 'unknown')

    def normalize_text(self, text: str) -> str:
        """
        توحيد النص (تطبيع)
        Normalize text to Unicode NFKD form
        
        Args:
            text (str): النص الخام
            
        Returns:
            str: النص الموحد
        """
        return unicodedata.normalize('NFKD', text)

    def find_letter_positions(self, text: str, letter: str) -> List[int]:
        """
        إيجاد جميع مواقع حرف معين في النص
        Find all positions of a specific letter in text
        
        Args:
            text (str): النص
            letter (str): الحرف المراد البحث عنه
            
        Returns:
            List[int]: قائمة بمواقع الحرف
        """
        letters = self.extract_letters(text)
        positions = [i for i, l in enumerate(letters) if l == letter]
        
        return positions

    def get_context_around_letter(self, text: str, position: int, context_size: int = 2) -> Tuple[List[str], str, List[str]]:
        """
        الحصول على السياق حول حرف معين
        Get context around a specific letter
        
        Args:
            text (str): النص
            position (int): موقع الحرف
            context_size (int): حجم السياق (عدد الحروف قبل وبعد)
            
        Returns:
            Tuple: (الحروف قبل، الحرف الحالي، الحروف بعد)
        """
        letters = self.extract_letters(text)
        
        if position >= len(letters):
            return [], '', []
        
        before = letters[max(0, position - context_size):position]
        current = letters[position]
        after = letters[position + 1:min(len(letters), position + 1 + context_size)]
        
        return before, current, after

    def __repr__(self) -> str:
        """تمثيل نصي لكائن المعالج"""
        return f"<TextProcessor: Arabic={len(self.ARABIC_LETTERS)} letters>"
