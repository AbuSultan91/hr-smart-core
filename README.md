# 🏢 HR Smart Core - نظام إدارة الموارد البشرية المتطور

<div align="center">

![HR Smart Core Logo](https://via.placeholder.com/400x150/2E86AB/FFFFFF?text=HR+Smart+Core)

[![License](https://img.shields.io/badge/License-HSCCL-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2%2B-darkgreen.svg)](https://djangoproject.com)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/hrsmartcore/hr-smart-core)

**نظام إدارة موارد بشرية شامل مصمم خصيصاً للسوق السعودي ودول الخليج العربي**

[🌟 العرض التوضيحي](https://demo.hrsmartcore.com) | [📚 الوثائق](documentation/) | [💬 المجتمع](https://community.hrsmartcore.com) | [🤝 الشراكة](mailto:Hishamattas@gmail.com)

</div>

---

## 🎯 نظرة عامة على المشروع

**HR Smart Core** هو نظام إدارة موارد بشرية متطور مبني باستخدام Django، مصمم خصيصاً لتلبية احتياجات الشركات في المملكة العربية السعودية ودول الخليج العربي. يتميز النظام بالتوافق الكامل مع قانون العمل السعودي والحوسبة المالية الدقيقة للرواتب والمكافآت.

## 🎯 أهداف المشروع

- **المرونة**: نظام متعدد الشركات قابل للتخصيص
- **الامتثال**: توافق كامل مع نظام العمل السعودي
- **الأمان**: حماية متقدمة للبيانات والخصوصية
- **سهولة الاستخدام**: واجهة بديهية باللغة العربية
- **التوسع**: إمكانية البيع والتوزيع التجاري

## 🛠 التقنيات المستخدمة

### الخلفية (Backend)
- **Python 3.9+**: لغة البرمجة الأساسية
- **Django 4.2+**: إطار العمل الرئيسي
- **Django REST Framework**: لبناء APIs
- **SQLite/MySQL**: قواعد البيانات
- **Celery**: للمهام غير المتزامنة
- **Redis**: للتخزين المؤقت

### الواجهة الأمامية (Frontend)
- **HTML5**: هيكل الصفحات
- **CSS3**: التصميم والتنسيق
- **JavaScript (ES6+)**: التفاعل والديناميكية
- **Bootstrap 5**: إطار العمل للتصميم المتجاوب
- **jQuery**: للتفاعل مع DOM
- **Chart.js**: للرسوم البيانية والإحصائيات

### الأدوات المساعدة
- **Pillow**: لمعالجة الصور
- **ReportLab**: لإنشاء ملفات PDF
- **openpyxl**: لملفات Excel
- **django-cors-headers**: لإدارة CORS
- **django-crispy-forms**: لتحسين النماذج

## 📁 هيكل المشروع

```
hr_smart_core/
├── 📁 documentation/           # الوثائق الشاملة
├── 📁 project_setup/          # إعدادات وملفات الإعداد
├── 📁 hr_system/              # المشروع الرئيسي Django
├── 📁 apps/                   # تطبيقات النظام
├── 📁 static/                 # الملفات الثابتة
├── 📁 media/                  # ملفات الرفع
├── 📁 templates/              # قوالب HTML
├── 📁 tests/                  # ملفات الاختبار
├── 📁 utils/                  # أدوات مساعدة
├── 📁 scripts/                # سكريبتات التشغيل
└── 📁 deployment/             # ملفات النشر
```

## 🚀 البدء السريع

1. **تثبيت المتطلبات**:
   ```bash
   pip install -r requirements.txt
   ```

2. **إعداد قاعدة البيانات**:
   ```bash
   python manage.py migrate
   ```

3. **تشغيل السيرفر**:
   ```bash
   python manage.py runserver
   ```

4. **الوصول للنظام**:
   - الرابط: http://127.0.0.1:8000
   - المسؤول: admin/admin123

## 📖 الوثائق

راجع مجلد `documentation/` للحصول على:
- دليل التثبيت التفصيلي
- دليل المستخدم
- دليل المطور
- دليل API
- دليل الصيانة

## 📞 الدعم والمساعدة

للحصول على الدعم أو الإبلاغ عن مشاكل، يرجى مراجعة:
- دليل استكشاف الأخطاء
- الأسئلة الشائعة
- دليل المطور

## 📄 الترخيص

هذا المشروع مملوك بالكامل للمطور ويمكن استخدامه تجارياً.

---
**© 2025 HR Smart Core - جميع الحقوق محفوظة**
