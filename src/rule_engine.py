"""
محرك القواعد - نظام الاستدلال المنطقي
Rule Engine - Logical Inference System for Tajweed Rules

يطبق قواعد التجويد الـ 6 الرئيسية:
1. الإظهار الحلقي
2. الإخفاء الحقيقي
3. الإدغام
4. الإقلاب
5. التفخيم
6. الترقيق
"""

from typing import List, Dict
from text_processor import TextProcessor


class RuleEngine:
    """
    محرك القواعد - نظام الاستدلال المنطقي
    Rule Engine - Logical Inference System
    """

    def __init__(self):
        """تهيئة محرك القواعد"""
        self.processor = TextProcessor()
        self.rules = self._initialize_rules()

    def _initialize_rules(self) -> Dict:
        """
        تهيئة قاعدة القواعد
        Initialize the rule base
        
        Returns:
            Dict: قاموس القواعد
        """
        rules = {
            'al_izhar': {
                'name': 'الإظهار الحلقي',
                'name_en': 'Throat Manifestation',
                'description': 'نطق النون والتنوين بوضوح عند الحروف الحلقية',
                'letters': ['ا', 'ه', 'ع', 'غ', 'ح', 'خ'],
                'confidence': 0.95
            },
            'al_ikhfa': {
                'name': 'الإخفاء الحقيقي',
                'name_en': 'True Concealment',
                'description': 'إخفاء النون والتنوين عند 15 حرفاً',
                'letters': ['ص', 'ذ', 'ت', 'ك', 'ط', 'ف', 'ق', 'ج', 'د', 'ش', 'ز', 'س', 'ب', 'ل', 'ن'],
                'confidence': 0.90
            },
            'al_idgham': {
                'name': 'الإدغام',
                'name_en': 'Assimilation',
                'description': 'دمج النون والتنوين مع الحروف (ي، ن، م، و)',
                'letters': ['ي', 'ن', 'م', 'و'],
                'confidence': 0.98
            },
            'al_iqlab': {
                'name': 'الإقلاب',
                'name_en': 'Conversion',
                'description': 'قلب النون الساكنة إلى باء عند الباء',
                'letters': ['ب'],
                'confidence': 0.97
            },
            'al_tafkhim': {
                'name': 'التفخيم',
                'name_en': 'Emphasis',
                'description': 'تفخيم حروف معينة: ص، ض، ط، ظ، ق، غ، ر، خ',
                'letters': ['ص', 'ض', 'ط', 'ظ', 'ق', 'غ', 'ر', 'خ'],
                'confidence': 0.92
            },
            'al_tarqiq': {
                'name': 'الترقيق',
                'name_en': 'Thinning',
                'description': 'ترقيق باقي الحروف',
                'confidence': 0.85
            }
        }
        
        return rules

    def apply_rules(self, text: str) -> List[Dict]:
        """
        تطبيق القواعد على النص
        Apply rules to text
        
        Args:
            text (str): النص المراد تطبيق القواعد عليه
            
        Returns:
            List[Dict]: قائمة الأحكام المكتشفة
        """
        detected_rules = []
        features = self.processor.extract_features(text)
        letters = features['letters']
        
        # تطبيق كل قاعدة
        for i, letter in enumerate(letters):
            # التحقق من ال��ظهار الحلقي
            if self._check_al_izhar(letter, letters, i):
                detected_rules.append(self._create_rule_result(
                    'al_izhar', letter, i, text
                ))
            
            # التحقق من الإخفاء الحقيقي
            elif self._check_al_ikhfa(letter, letters, i):
                detected_rules.append(self._create_rule_result(
                    'al_ikhfa', letter, i, text
                ))
            
            # التحقق من الإدغام
            elif self._check_al_idgham(letter, letters, i):
                detected_rules.append(self._create_rule_result(
                    'al_idgham', letter, i, text
                ))
            
            # التحقق من الإقلاب
            elif self._check_al_iqlab(letter, letters, i):
                detected_rules.append(self._create_rule_result(
                    'al_iqlab', letter, i, text
                ))
            
            # التحقق من التفخيم
            if self._check_al_tafkhim(letter):
                detected_rules.append(self._create_rule_result(
                    'al_tafkhim', letter, i, text
                ))
            
            # التحقق من الترقيق
            elif self._check_al_tarqiq(letter, letters, i):
                detected_rules.append(self._create_rule_result(
                    'al_tarqiq', letter, i, text
                ))
        
        return detected_rules

    def _check_al_izhar(self, letter: str, letters: List[str], position: int) -> bool:
        """
        التحقق من قاعدة الإظهار الحلقي
        Check Throat Manifestation rule
        
        Args:
            letter (str): الحرف الحالي
            letters (List[str]): قائمة الحروف
            position (int): موقع الحرف
            
        Returns:
            bool: صحيح إذا انطبقت القاعدة
        """
        # الإظهار يحدث عند النون الساكنة أو التنوين قبل حروف حلقية
        if letter in ['ن', 'ه']:  # النون أو هاء التأنيث
            if position + 1 < len(letters):
                next_letter = letters[position + 1]
                return self.processor.check_throat_letters(next_letter)
        
        return False

    def _check_al_ikhfa(self, letter: str, letters: List[str], position: int) -> bool:
        """
        التحقق من قاعدة الإخفاء الحقيقي
        Check True Concealment rule
        
        Args:
            letter (str): الحرف الحالي
            letters (List[str]): قائمة الحروف
            position (int): موقع الحرف
            
        Returns:
            bool: صحيح إذا انطبقت القاعدة
        """
        # الإخفاء يحدث عند النون الساكنة قبل 15 حرفاً
        if letter in ['ن', 'ه']:
            if position + 1 < len(letters):
                next_letter = letters[position + 1]
                return self.processor.check_hiding_letters(next_letter)
        
        return False

    def _check_al_idgham(self, letter: str, letters: List[str], position: int) -> bool:
        """
        التحقق من قاعدة الإدغام
        Check Assimilation rule
        
        Args:
            letter (str): الحرف الحالي
            letters (List[str]): قائمة الحروف
            position (int): موقع الحرف
            
        Returns:
            bool: صحيح إذا انطبقت القاعدة
        """
        # الإدغام يحدث عند النون الساكنة قبل (ي، ن، م، و)
        if letter == 'ن':
            if position + 1 < len(letters):
                next_letter = letters[position + 1]
                return self.processor.check_assimilation_letters(next_letter)
        
        return False

    def _check_al_iqlab(self, letter: str, letters: List[str], position: int) -> bool:
        """
        التحقق من قاعدة الإقلاب
        Check Conversion rule
        
        Args:
            letter (str): الحرف الحالي
            letters (List[str]): قائمة الحروف
            position (int): موقع الحرف
            
        Returns:
            bool: صحيح إذا انطبقت القاعدة
        """
        # الإقلاب يحدث عند النون الساكنة قبل الباء
        if letter == 'ن':
            if position + 1 < len(letters):
                next_letter = letters[position + 1]
                return next_letter == 'ب'
        
        return False

    def _check_al_tafkhim(self, letter: str) -> bool:
        """
        التحقق من قاعدة التفخيم
        Check Emphasis rule
        
        Args:
            letter (str): الحرف المراد التحقق منه
            
        Returns:
            bool: صحيح إذا كان الحرف مفخماً
        """
        return self.processor.check_heavy_letters(letter)

    def _check_al_tarqiq(self, letter: str, letters: List[str], position: int) -> bool:
        """
        التحقق من قاعدة الترقيق
        Check Thinning rule
        
        Args:
            letter (str): الحرف الحالي
            letters (List[str]): قائمة الحروف
            position (int): موقع الحرف
            
        Returns:
            bool: صحيح إذا كان الحرف مرققاً
        """
        # الترقيق يحدث لباقي الحروف التي ليست مفخمة
        return not self.processor.check_heavy_letters(letter)

    def _create_rule_result(self, rule_id: str, letter: str, position: int, text: str) -> Dict:
        """
        إنشاء نتيجة قاعدة
        Create a rule result
        
        Args:
            rule_id (str): معرّف القاعدة
            letter (str): الحرف
            position (int): موقع الحرف
            text (str): النص الكامل
            
        Returns:
            Dict: نتيجة القاعدة
        """
        rule = self.rules.get(rule_id, {})
        
        return {
            'rule_id': rule_id,
            'name': rule.get('name', 'Unknown Rule'),
            'name_en': rule.get('name_en', ''),
            'description': rule.get('description', ''),
            'letter': letter,
            'position': position,
            'confidence': rule.get('confidence', 0.0),
        }

    def get_rule_statistics(self, rules: List[Dict]) -> Dict:
        """
        الحصول على إحصائيات القواعس
        Get statistics about detected rules
        
        Args:
            rules (List[Dict]): قائمة القواعس المكتشفة
            
        Returns:
            Dict: إحصائيات القواعس
        """
        stats = {
            'total_rules': len(rules),
            'unique_rules': len(set(r['rule_id'] for r in rules)),
            'average_confidence': sum(r['confidence'] for r in rules) / len(rules) if rules else 0,
            'rules_by_type': {}
        }
        
        # عد القواعس حسب النوع
        for rule in rules:
            rule_id = rule['rule_id']
            if rule_id not in stats['rules_by_type']:
                stats['rules_by_type'][rule_id] = 0
            stats['rules_by_type'][rule_id] += 1
        
        return stats

    def explain_rule(self, rule_id: str) -> str:
        """
        شرح قاعدة معينة
        Explain a specific rule
        
        Args:
            rule_id (str): معرّف القاعدة
            
        Returns:
            str: شرح القاعدة
        """
        rule = self.rules.get(rule_id, {})
        
        explanation = f"""
        القاعدة: {rule.get('name', 'Unknown')}
        الاسم الإنجليزي: {rule.get('name_en', '')}
        
        الوصف:
        {rule.get('description', '')}
        
        الحروف: {', '.join(rule.get('letters', []))}
        درجة الثقة: {rule.get('confidence', 0.0) * 100}%
        """
        
        return explanation

    def __repr__(self) -> str:
        """تمثيل نصي لمحرك القواعد"""
        return f"<RuleEngine: {len(self.rules)} rules>"
