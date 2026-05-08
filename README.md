# نظام خبير استخراج أحكام التجويد 🕌

## 📖 وصف المشروع

نظام خبير هجين يجمع بين **محرك الاستدلال المنطقي** و**التعلم الآلي** لاستخراج أحكام التجويد من النصوص القرآنية تلقائياً.

### الهدف:
تحليل نص قرآني وتحديد:
- ✅ نوع الحكم التجويدي
- ✅ موقع الحكم في النص
- ✅ درجة الثقة في التشخيص

---

## 🏗️ معمارية النظام

```
النص القرآني المدخل
        ↓
معالج النصوص (Text Processing)
        ↓
    ╔═══════════════════════════════════╗
    ║  محرك الاستدلال  ↔  نموذج ML      ║
    ║  (Rule Engine)     (Decision Tree) ║
    ╚═══════════════════════════════════╝
        ↓
قائمة أحكام التجويد + درجة الثقة
```

---

## 🎯 أحكام التجويد المستهدفة

| الحكم | الوصف | مثال |
|-------|-------|------|
| الإظهار الحلقي | نطق النون والتنوين بوضوح | قَالَ أَحَدُهُمَا |
| الإخفاء الحقيقي | إخفاء النون والتنوين | مِن شَيْء |
| الإدغام | دمج الحروف | مَن نَّارٍ |
| الإقلاب | قلب النون الساكنة باء | أَن بَلَىٰ |
| التفخيم | تفخيم حروف معينة | قَالَ، ضَالُّون |
| الترقيق | ترقيق باقي الحروف | كِتَاب، مَدِيد |

---

## 🛠️ التقنيات المستخدمة

```
Backend:
  ✓ Python 3.9+
  ✓ Scikit-learn (Decision Trees)
  ✓ NLTK (معالجة النصوص العربية)
  ✓ Flask/FastAPI (API)

Data:
  ✓ JSON (قاعدة القواعد)
  ✓ SQLite (قاعدة البيانات)

Testing:
  ✓ Pytest (اختبارات الوحدة)
```

---

## 📁 هيكل المشروع

```
tajweed-expert-system/
├── src/
│   ├── main.py                 # نقطة الدخول
│   ├── text_processor.py       # معالج النصوص
│   ├── rule_engine.py          # محرك القواعد
│   ├── ml_model.py             # نموذج التعلم الآلي
│   └── utils.py                # دوال مساعدة
├── data/
│   ├── tajweed_rules.json      # قاعدة القواعد
│   └── test_cases.json         # حالات الاختبار
├── tests/
│   ├── test_processor.py       # اختبارات معالج النصوص
│   └── test_rules.py           # اختبارات محرك القواعد
├── docs/
│   └── knowledge_engineering.md # مخطط هندسة المعرفة
├── reports/
│   └── technical_report.md     # التقرير التقني
├── requirements.txt            # المتطلبات
└── README.md                   # هذا الملف
```

---

## 🚀 البدء السريع

### 1. الاستنساخ والتثبيت:
```bash
git clone https://github.com/Mahmoud-AlRaaei/tajweed-expert-system.git
cd tajweed-expert-system
pip install -r requirements.txt
```

### 2. تشغيل النظام:
```bash
python src/main.py
```

### 3. تشغيل الاختبارات:
```bash
python tests/test_processor.py
python tests/test_rules.py
```

---

## 📊 مثال على الاستخدام

```python
from src.text_processor import TextProcessor
from src.rule_engine import RuleEngine

# إنشاء معالج النصوص
processor = TextProcessor()

# إدخال نص قرآني
text = "قَالَ أَحَدُهُمَا"

# معالجة النص
processed = processor.process(text)

# تطبيق قواعد التجويد
engine = RuleEngine()
rules = engine.apply_rules(processed)

# عرض النتائج
for rule in rules:
    print(f"الحكم: {rule['name']}")
    print(f"الموقع: {rule['position']}")
    print(f"الثقة: {rule['confidence']}%")
```

---

## 📚 التوثيق

- 📄 [مخطط هندسة المعرفة](docs/knowledge_engineering.md)
- 📄 [التقرير التقني الكامل](reports/technical_report.md)
- 📄 [حالات الاختبار](data/test_cases.json)

---

## ✅ المتطلبات الأساسية

- ✓ Python 3.9 أو أحدث
- ✓ pip (مدير الحزم)
- ✓ Git

---

## 📝 الحالة الحالية للمشروع

- [x] إعداد هيكل المشروع
- [ ] كتابة معالج النصوص
- [ ] بناء محرك القواعد
- [ ] تطوير نموذج ML
- [ ] كتابة الاختبارات
- [ ] إعداد التقرير التقني
- [ ] إنشاء فيديو توضيحي (اختياري)

---

## 👨‍💻 المطور

**Mahmoud-AlRaaei**

---

## 📄 الترخيص

MIT License

---

## 📞 التواصل

للأسئلة والاقتراحات: [فتح Issue](https://github.com/Mahmoud-AlRaaei/tajweed-expert-system/issues)
