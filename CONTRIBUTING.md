# 🤝 دليل المساهمة في HR Smart Core

مرحباً بك في مجتمع **HR Smart Core**! نحن نرحب بمساهمات المطورين من جميع أنحاء العالم العربي والعالم.

## 🎯 كيفية المساهمة

### 🚀 للمبتدئين

إذا كانت هذه مساهمتك الأولى في مشروع مفتوح المصدر، فأنت في المكان المناسب!

1. **اقرأ الوثائق**: ابدأ بقراءة [دليل فهم المشروع](documentation/06_project_understanding_guide.md)
2. **جهز بيئة التطوير**: اتبع [دليل التثبيت](documentation/04_installation_guide.md)
3. **ابحث عن مهمة مناسبة**: ابحث عن Issues مُعلَّمة بـ `good first issue`

### 📋 خطوات المساهمة

#### 1. Fork المشروع
```bash
# انقر على زر Fork في GitHub
# ثم استنسخ نسختك الشخصية
git clone https://github.com/your-username/hr-smart-core.git
cd hr-smart-core
```

#### 2. إعداد البيئة المحلية
```bash
# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate     # Windows

# تثبيت المتطلبات
pip install -r requirements/development.txt

# إعداد قاعدة البيانات
python manage.py migrate
python manage.py loaddata sample_data.json
```

#### 3. إنشاء فرع جديد
```bash
# إنشاء فرع للميزة الجديدة
git checkout -b feature/your-feature-name

# أو لإصلاح خطأ
git checkout -b fix/bug-description
```

#### 4. كتابة الكود
- اتبع معايير [PEP 8](https://pep8.org/) لـ Python
- اكتب تعليقات واضحة باللغة العربية أو الإنجليزية
- أضف اختبارات للميزات الجديدة

#### 5. تشغيل الاختبارات
```bash
# تشغيل جميع الاختبارات
python manage.py test

# تشغيل اختبارات محددة
python manage.py test apps.employees.tests

# فحص جودة الكود
flake8 .
black . --check
```

#### 6. Commit التغييرات
```bash
# إضافة الملفات المعدلة
git add .

# كتابة رسالة commit واضحة
git commit -m "Add: إضافة ميزة حساب الإجازات التلقائي"

# أو للإصلاحات
git commit -m "Fix: إصلاح خطأ في حساب الراتب الأساسي"
```

#### 7. Push ونشر Pull Request
```bash
# رفع التغييرات لحسابك
git push origin feature/your-feature-name

# ثم اذهب لـ GitHub وأنشئ Pull Request
```

## 📐 معايير الكود

### 🐍 Python Code Style
```python
# ✅ جيد
def calculate_salary(employee_id: int, month: int) -> Decimal:
    """
    حساب راتب الموظف لشهر معين
    
    Args:
        employee_id: معرف الموظف
        month: رقم الشهر (1-12)
        
    Returns:
        Decimal: إجمالي الراتب
    """
    employee = Employee.objects.get(id=employee_id)
    return employee.basic_salary + employee.allowances

# ❌ سيء
def calc(emp, m):
    return emp.salary + emp.allow
```

### 🎨 HTML/CSS Guidelines
```html
<!-- ✅ جيد - دعم RTL للعربية -->
<div class="employee-card" dir="rtl">
    <h3 class="employee-name">{{ employee.full_name }}</h3>
    <p class="employee-department">{{ employee.department.name }}</p>
</div>

<!-- ❌ سيء - بدون دعم RTL -->
<div class="card">
    <h3>{{ employee.full_name }}</h3>
</div>
```

### 📱 JavaScript Best Practices
```javascript
// ✅ جيد
const employeeService = {
    async getEmployeeData(employeeId) {
        try {
            const response = await fetch(`/api/employees/${employeeId}/`);
            return await response.json();
        } catch (error) {
            console.error('خطأ في جلب بيانات الموظف:', error);
            throw error;
        }
    }
};

// ❌ سيء
function getData(id) {
    return fetch('/api/employees/' + id + '/').then(r => r.json());
}
```

## 🧪 كتابة الاختبارات

### اختبارات الوحدة (Unit Tests)
```python
# tests/test_payroll.py
from django.test import TestCase
from decimal import Decimal
from apps.employees.models import Employee
from apps.payroll.services import PayrollService

class PayrollServiceTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            first_name="أحمد",
            last_name="محمد",
            basic_salary=Decimal('5000.00')
        )
    
    def test_calculate_basic_salary(self):
        """اختبار حساب الراتب الأساسي"""
        service = PayrollService()
        salary = service.calculate_basic_salary(self.employee)
        self.assertEqual(salary, Decimal('5000.00'))
```

### اختبارات التكامل (Integration Tests)
```python
# tests/test_api.py
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class EmployeeAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.client.force_authenticate(user=self.user)
    
    def test_create_employee(self):
        """اختبار إنشاء موظف جديد عبر API"""
        data = {
            'first_name': 'سعد',
            'last_name': 'العتيبي',
            'email': 'saad@company.com'
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, 201)
```

## 📝 كتابة الوثائق

### Docstrings للدوال
```python
def calculate_end_of_service_benefit(employee: Employee, end_date: date) -> Decimal:
    """
    حساب مكافأة نهاية الخدمة حسب نظام العمل السعودي
    
    المكافأة تحسب كالتالي:
    - نصف راتب شهر لكل سنة من أول 5 سنوات
    - راتب شهر كامل لكل سنة بعد ذلك
    
    Args:
        employee (Employee): بيانات الموظف
        end_date (date): تاريخ انتهاء الخدمة
        
    Returns:
        Decimal: قيمة مكافأة نهاية الخدمة
        
    Example:
        >>> employee = Employee.objects.get(id=1)
        >>> benefit = calculate_end_of_service_benefit(employee, date(2025, 12, 31))
        >>> print(f"المكافأة: {benefit} ريال")
    """
    # منطق الحساب هنا
    pass
```

## 🏷️ أنواع المساهمات

### 🆕 ميزات جديدة (Features)
- إضافة وحدات جديدة للنظام
- تحسين الواجهات الموجودة
- إضافة تكاملات مع أنظمة خارجية

### 🐛 إصلاح الأخطاء (Bug Fixes)
- إصلاح مشاكل في المنطق
- تحسين الأداء
- إصلاح مشاكل الأمان

### 📚 تحسين الوثائق
- إضافة أمثلة عملية
- ترجمة المحتوى
- إضافة شروحات للمطورين الجدد

### 🎨 تحسين التصميم
- تحسين تجربة المستخدم
- إضافة دعم أفضل للغة العربية
- تحسين الاستجابة للأجهزة المختلفة

## 🎯 أولويات المشروع الحالية

### 🔥 عالية الأولوية
- [ ] تطوير نظام الحضور والانصراف المتقدم
- [ ] إضافة حسابات الرواتب المعقدة
- [ ] تطوير تطبيق الجوال للموظفين
- [ ] تحسين أمان النظام

### 📈 متوسطة الأولوية
- [ ] إضافة التقارير التفاعلية
- [ ] تطوير نظام الإشعارات
- [ ] تحسين واجهة المدير
- [ ] إضافة دعم لعدة لغات

### 💡 اختيارية
- [ ] تكامل مع منصات التواصل الاجتماعي
- [ ] إضافة نظام التدريب الإلكتروني
- [ ] تطوير chatbot للدعم الفني

## 📞 التواصل والمساعدة

### 💬 قنوات التواصل
- **GitHub Issues**: [للأسئلة التقنية والأخطاء](https://github.com/hrsmartcore/hr-smart-core/issues)
- **GitHub Discussions**: [للنقاشات العامة](https://github.com/hrsmartcore/hr-smart-core/discussions)
- **Email**: dev@hrsmartcore.com
- **Telegram**: @HRSmartCore_Developers

### 🤝 مجتمع المطورين
- **Discord Server**: [انضم لخادم Discord](https://discord.gg/hrsmartcore)
- **Weekly Meetings**: كل ثلاثاء 8 مساءً (التوقيت السعودي)
- **Monthly Hackathon**: آخر جمعة من كل شهر

## 🏆 تقدير المساهمين

### 🌟 شهادات التقدير
- **Contributor Badge**: لأول مساهمة مقبولة
- **Core Contributor**: للمساهمات المنتظمة (5+ PRs)
- **Expert Contributor**: للمساهمات الجوهرية (20+ PRs)

### 🎁 مكافآت خاصة
- **اسمك في قائمة الشكر**: في README الرئيسي
- **وصول مبكر**: للميزات الجديدة قبل الإطلاق
- **خصومات خاصة**: على النسخة التجارية
- **شهادة مطور معتمد**: من HR Smart Core

### 💰 فرص العمل والشراكة
المساهمون المتميزون لديهم أولوية في:
- **الانضمام للفريق الأساسي** براتب ثابت
- **الشراكة التقنية** مع نسبة من الأرباح (5-35%)
- **فرص العمل الحر** في مشاريع العملاء
- **التدريب المجاني** على تقنيات متقدمة

## 📋 Code Review Guidelines

### ✅ ما نبحث عنه
- **الوضوح**: كود واضح وسهل الفهم
- **الكفاءة**: خوارزميات محسنة وأداء جيد
- **الأمان**: لا توجد ثغرات أمنية
- **الاختبارات**: تغطية جيدة بالاختبارات
- **التوثيق**: شرح واضح للتغييرات

### ❌ ما نتجنبه
- **كود معقد** بدون مبرر
- **تكرار غير ضروري** للكود
- **تجاهل معايير التنسيق**
- **عدم وجود اختبارات** للميزات الجديدة
- **تعليقات غير واضحة** أو مفقودة

## 🚀 بدء المساهمة اليوم!

هل أنت مستعد للمساهمة؟ إليك الخطوات السريعة:

1. **Fork المشروع** من GitHub
2. **اختر Issue** مناسب لمستواك  
3. **اكتب الكود** واتبع المعايير
4. **أرسل Pull Request** مع وصف واضح
5. **شارك في Code Review** واستقبل التعليقات

**مرحباً بك في رحلة بناء أفضل نظام HR في العالم العربي! 🎉**

---

## 📄 اتفاقية المساهم (CLA)

بتقديم مساهمة لهذا المشروع، أنت توافق على:

- مساهمتك أصلية ولا تنتهك حقوق الآخرين
- منح صاحب المشروع حقوق استخدام مساهمتك
- الالتزام بقيم المجتمع والسلوك المهني
- احترام رخصة المشروع وشروطه

---

**شكراً لك على اهتمامك بـ HR Smart Core! 🙏**
