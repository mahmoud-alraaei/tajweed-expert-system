"""
نقطة الدخول الرئيسية للنظام الخبير
Main Entry Point for the Expert System
"""

import json
from pathlib import Path
from .text_processor import TextProcessor
from .rule_engine import RuleEngine
from .ml_model import MLModel


class TajweedExpertSystem:
    """
    نظام خبير التجويد - النسخة الرئيسية
    Main Tajweed Expert System Class
    """

    def __init__(self):
        """تهيئة النظام الخبير"""
        self.text_processor = TextProcessor()
        self.rule_engine = RuleEngine()
        self.ml_model = MLModel()
        print("✅ تم تهيئة نظام خبير التجويد بنجاح")
        print("✅ Tajweed Expert System initialized successfully")

    def analyze(self, quranic_text: str) -> dict:
        """
        تحليل نص قرآني واستخراج أحكام التجويد
        
        Args:
            quranic_text (str): النص القرآني المراد تحليله
            
        Returns:
            dict: قاموس يحتوي على:
                - text: النص الأصلي
                - processed_text: النص المعالج
                - tajweed_rules: قائمة أحكام التجويد المكتشفة
                - confidence: درجة الثقة الإجمالية
        """
        
        try:
            # 1. معالجة النص
            print("\n📝 معالجة النص...")
            processed_text = self.text_processor.process(quranic_text)
            
            # 2. تطبيق قواعد التجويد
            print("🔍 تطبيق قواعد التجويد...")
            tajweed_rules = self.rule_engine.apply_rules(processed_text)
            
            # 3. التنبؤ باستخدام نموذج ML
            print("🤖 تحليل نموذج التعلم الآلي...")
            ml_predictions = self.ml_model.predict(processed_text)
            
            # 4. دمج النتائج
            results = {
                'text': quranic_text,
                'processed_text': processed_text,
                'tajweed_rules': tajweed_rules,
                'ml_predictions': ml_predictions,
                'confidence': self._calculate_confidence(tajweed_rules, ml_predictions)
            }
            
            return results
            
        except Exception as e:
            print(f"❌ حدث خطأ: {str(e)}")
            return {'error': str(e)}

    @staticmethod
    def _calculate_confidence(rules: list, predictions: list) -> float:
        """حساب درجة الثقة الإجمالية"""
        if not rules and not predictions:
            return 0.0
        
        total_confidence = 0
        count = 0
        
        for rule in rules:
            total_confidence += rule.get('confidence', 0)
            count += 1
        
        for pred in predictions:
            total_confidence += pred.get('confidence', 0)
            count += 1
        
        return (total_confidence / count * 100) if count > 0 else 0.0

    def display_results(self, results: dict):
        """عرض النتائج بشكل منسق"""
        if 'error' in results:
            print(f"❌ خطأ: {results['error']}")
            return
        
        print("\n" + "=" * 60)
        print("📊 نتائج التحليل / Analysis Results")
        print("=" * 60)
        
        print(f"\n📖 النص الأصلي / Original Text:")
        print(f"   {results['text']}")
        
        print(f"\n⚙️ النص المعالج / Processed Text:")
        print(f"   {results['processed_text']}")
        
        print(f"\n🎯 أحكام التجويد / Tajweed Rules:")
        for i, rule in enumerate(results['tajweed_rules'], 1):
            print(f"   {i}. {rule['name']} ({rule['confidence']}% ثقة)")
            print(f"      الموقع: {rule['position']}")
            print(f"      الوصف: {rule['description']}")
        
        print(f"\n🤖 نتائج التعلم الآلي / ML Predictions:")
        for i, pred in enumerate(results['ml_predictions'], 1):
            print(f"   {i}. {pred['rule']} ({pred['confidence']}% ثقة)")
        
        print(f"\n📈 درجة الثقة الإجمالية / Overall Confidence:")
        print(f"   {results['confidence']:.2f}%")
        
        print("=" * 60 + "\n")


def main():
    """الدالة الرئيسية"""
    print("\n")
    print("🕌 نظام خبير استخراج أحكام التجويد 🕌")
    print("💻 Expert System for Tajweed Rules Extraction")
    print("=" * 60 + "\n")
    
    # إنشاء النظام
    system = TajweedExpertSystem()
    
    # نصوص تجريبية
    test_texts = [
        "قَالَ أَحَدُهُمَا",
        "مِن شَيْء",
        "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    ]
    
    print("\n🔄 بدء الاختبار...\n")
    
    for text in test_texts:
        results = system.analyze(text)
        system.display_results(results)


if __name__ == "__main__":
    main()
