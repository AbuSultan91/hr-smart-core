# 🏗 هندسة النظام والتصميم المعماري

**تاريخ الإنشاء**: 3 أغسطس 2025  
**آخر تحديث**: 3 أغسطس 2025  
**الإصدار**: 1.0.0

---

## 🎯 فلسفة التصميم المعماري

### مبادئ التصميم الأساسية:

1. **فصل الاهتمامات (Separation of Concerns)**
   - فصل منطق العمل عن طبقة العرض
   - فصل النماذج عن العمليات
   - فصل التصميم عن البرمجة

2. **النظافة والبساطة (Clean & Simple)**
   - كود نظيف وقابل للقراءة
   - هيكل واضح ومنطقي
   - تجنب التعقيد غير الضروري

3. **القابلية للتوسع (Scalability)**
   - دعم الشركات المتعددة
   - إمكانية إضافة ميزات جديدة
   - تحمل زيادة عدد المستخدمين

4. **الأمان والموثوقية (Security & Reliability)**
   - حماية البيانات في جميع الطبقات
   - نظام احتياطي وشامل
   - تسجيل ومراقبة جميع العمليات

---

## 🏗 المعمارية العامة للنظام

### نموذج MVC المحسن (Enhanced MVC Pattern)

```
┌─────────────────────────────────────────────────────────┐
│                  طبقة العرض (Presentation Layer)        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   Templates │  │     CSS     │  │ JavaScript  │      │
│  │    (HTML)   │  │   Styling   │  │ Interaction │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────┐
│                 طبقة التحكم (Control Layer)              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │    Views    │  │     URLs    │  │    Forms    │      │
│  │ (Controllers)│  │  (Routing)  │  │ (Validation)│      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────┐
│                طبقة منطق العمل (Business Logic Layer)   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │  Services   │  │  Utilities  │  │ Validators  │      │
│  │ (Logic)     │  │  (Helpers)  │  │ (Rules)     │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────┐
│                  طبقة البيانات (Data Layer)              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   Models    │  │  Database   │  │   Migrations│      │
│  │  (ORM)      │  │  (SQLite)   │  │  (Schema)   │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 هيكل المشروع التفصيلي

### الهيكل الرئيسي:
```
hr_smart_core/
├── 📁 manage.py                    # نقطة دخول Django
├── 📁 requirements.txt             # متطلبات Python
├── 📁 .env                         # متغيرات البيئة
├── 📁 .gitignore                   # ملفات Git المستبعدة
│
├── 📁 hr_system/                   # إعدادات المشروع الرئيسي
│   ├── 📄 __init__.py
│   ├── 📄 settings.py              # إعدادات Django
│   ├── 📄 urls.py                  # URLs الرئيسية
│   ├── 📄 wsgi.py                  # WSGI للنشر
│   └── 📄 asgi.py                  # ASGI للتطبيقات غير المتزامنة
│
├── 📁 apps/                        # تطبيقات النظام
│   ├── 📁 authentication/          # المصادقة وإدارة المستخدمين
│   ├── 📁 companies/               # إدارة الشركات
│   ├── 📁 employees/               # إدارة الموظفين
│   ├── 📁 attendance/              # الحضور والانصراف
│   ├── 📁 leaves/                  # الإجازات
│   ├── 📁 payroll/                 # الرواتب
│   ├── 📁 reports/                 # التقارير
│   ├── 📁 training/                # التدريب والتطوير
│   ├── 📁 performance/             # تقييم الأداء
│   ├── 📁 complaints/              # الشكاوى والمقترحات
│   ├── 📁 meetings/                # الاجتماعات
│   ├── 📁 assets/                  # إدارة الأصول
│   └── 📁 notifications/           # الإشعارات
│
├── 📁 static/                      # الملفات الثابتة
│   ├── 📁 css/                     # ملفات CSS
│   ├── 📁 js/                      # ملفات JavaScript
│   ├── 📁 images/                  # الصور والأيقونات
│   ├── 📁 fonts/                   # الخطوط العربية
│   └── 📁 libs/                    # المكتبات الخارجية
│
├── 📁 media/                       # ملفات الرفع
│   ├── 📁 profile_pictures/        # صور الموظفين
│   ├── 📁 documents/               # الوثائق والملفات
│   ├── 📁 attachments/             # المرفقات
│   └── 📁 reports/                 # التقارير المحفوظة
│
├── 📁 templates/                   # قوالب HTML
│   ├── 📁 base/                    # القوالب الأساسية
│   ├── 📁 auth/                    # قوالب المصادقة
│   ├── 📁 dashboard/               # لوحة التحكم
│   ├── 📁 employees/               # قوالب الموظفين
│   ├── 📁 reports/                 # قوالب التقارير
│   └── 📁 components/              # مكونات قابلة للإعادة
│
├── 📁 utils/                       # أدوات مساعدة
│   ├── 📄 __init__.py
│   ├── 📄 helpers.py               # دوال مساعدة عامة
│   ├── 📄 validators.py            # مدققات مخصصة
│   ├── 📄 decorators.py            # ديكوريتورز مخصصة
│   ├── 📄 constants.py             # الثوابت والإعدادات
│   ├── 📄 saudi_labor_law.py       # قوانين العمل السعودية
│   └── 📄 calculations.py          # حسابات الرواتب والإجازات
│
├── 📁 tests/                       # اختبارات النظام
│   ├── 📁 unit/                    # اختبارات الوحدة
│   ├── 📁 integration/             # اختبارات التكامل
│   ├── 📁 functional/              # اختبارات وظيفية
│   └── 📁 fixtures/                # بيانات اختبار وهمية
│
├── 📁 scripts/                     # سكريبتات التشغيل
│   ├── 📄 setup_database.py        # إعداد قاعدة البيانات
│   ├── 📄 create_superuser.py      # إنشاء مستخدم مدير
│   ├── 📄 backup_database.py       # نسخ احتياطي
│   ├── 📄 restore_database.py      # استعادة البيانات
│   └── 📄 migrate_data.py          # نقل البيانات
│
├── 📁 documentation/               # الوثائق
│   ├── 📄 README.md
│   ├── 📄 installation_guide.md
│   ├── 📄 user_manual.md
│   ├── 📄 api_documentation.md
│   └── 📄 deployment_guide.md
│
└── 📁 deployment/                  # ملفات النشر
    ├── 📄 docker-compose.yml       # Docker للتطوير
    ├── 📄 Dockerfile               # بناء الصورة
    ├── 📄 nginx.conf               # إعدادات Nginx
    └── 📄 supervisor.conf          # إعدادات العمليات
```

---

## 🔧 التطبيقات والوحدات

### 1. 🔐 تطبيق المصادقة (Authentication)
```python
apps/authentication/
├── 📄 __init__.py
├── 📄 models.py                    # نماذج المستخدمين والجلسات
├── 📄 views.py                     # عمليات تسجيل الدخول والخروج
├── 📄 forms.py                     # نماذج تسجيل الدخول
├── 📄 urls.py                      # روابط المصادقة
├── 📄 decorators.py                # ديكوريتورز الصلاحيات
├── 📄 middleware.py                # وسطاء المصادقة
├── 📄 signals.py                   # إشارات تسجيل العمليات
└── 📁 migrations/                  # هجرات قاعدة البيانات
```

**الوظائف الرئيسية**:
- تسجيل الدخول والخروج
- إدارة الجلسات والتوكينز
- نظام الصلاحيات المتدرج
- تسجيل عمليات الدخول والأنشطة

### 2. 🏢 تطبيق الشركات (Companies)
```python
apps/companies/
├── 📄 __init__.py
├── 📄 models.py                    # نماذج الشركات والفروع
├── 📄 views.py                     # إدارة بيانات الشركات
├── 📄 forms.py                     # نماذج إدخال بيانات الشركة
├── 📄 urls.py                      # روابط إدارة الشركات
├── 📄 admin.py                     # واجهة الإدارة
├── 📄 serializers.py               # مسلسلات API
└── 📁 migrations/
```

**الوظائف الرئيسية**:
- إنشاء وإدارة بيانات الشركات
- تخصيص إعدادات كل شركة
- إدارة الفروع والمواقع
- نظام multi-tenant

### 3. 👥 تطبيق الموظفين (Employees)
```python
apps/employees/
├── 📄 __init__.py
├── 📄 models.py                    # نماذج الموظفين والأقسام
├── 📄 views.py                     # عمليات إدارة الموظفين
├── 📄 forms.py                     # نماذج إدخال بيانات الموظف
├── 📄 urls.py                      # روابط إدارة الموظفين
├── 📄 admin.py                     # واجهة الإدارة
├── 📄 signals.py                   # إشارات إنشاء حسابات المستخدمين
├── 📄 utils.py                     # دوال مساعدة لحساب الخدمة
└── 📁 migrations/
```

**الوظائف الرئيسية**:
- إضافة وتعديل بيانات الموظفين
- إدارة الأقسام والمناصب
- تحديد صلاحيات الموظفين
- حساب سنوات الخدمة تلقائياً

### 4. ⏰ تطبيق الحضور (Attendance)
```python
apps/attendance/
├── 📄 __init__.py
├── 📄 models.py                    # نماذج سجلات الحضور
├── 📄 views.py                     # عمليات تسجيل الحضور
├── 📄 forms.py                     # نماذج تسجيل الحضور اليدوي
├── 📄 urls.py                      # روابط الحضور
├── 📄 api_views.py                 # APIs للتطبيق المحمول
├── 📄 utils.py                     # حسابات ساعات العمل
├── 📄 location_utils.py            # التحقق من الموقع الجغرافي
└── 📁 migrations/
```

**الوظائف الرئيسية**:
- تسجيل الحضور والانصراف
- التحقق من الموقع الجغرافي
- حساب ساعات العمل والإضافي
- تقارير الحضور المفصلة

### 5. 🏖 تطبيق الإجازات (Leaves)
```python
apps/leaves/
├── 📄 __init__.py
├── 📄 models.py                    # نماذج أنواع وطلبات الإجازات
├── 📄 views.py                     # عمليات طلب والموافقة على الإجازات
├── 📄 forms.py                     # نماذج طلب الإجازة
├── 📄 urls.py                      # روابط الإجازات
├── 📄 calculations.py              # حسابات أرصدة الإجازات
├── 📄 workflows.py                 # سير عمل الموافقات
├── 📄 saudi_rules.py               # قوانين الإجازات السعودية
└── 📁 migrations/
```

**الوظائف الرئيسية**:
- إدارة أنواع الإجازات المختلفة
- حساب أرصدة الإجازات تلقائياً
- نظام طلب وموافقة الإجازات
- تطبيق قوانين العمل السعودية

### 6. 💰 تطبيق الرواتب (Payroll)
```python
apps/payroll/
├── 📄 __init__.py
├── 📄 models.py                    # نماذج الرواتب والبدلات
├── 📄 views.py                     # عمليات حساب وإدارة الرواتب
├── 📄 forms.py                     # نماذج إعداد الرواتب
├── 📄 urls.py                      # روابط الرواتب
├── 📄 calculations.py              # حسابات الرواتب المعقدة
├── 📄 saudi_calculations.py        # حسابات نهاية الخدمة السعودية
├── 📄 report_generator.py          # مولد كشوف الرواتب
└── 📁 migrations/
```

**الوظائف الرئيسية**:
- حساب الرواتب الشهرية تلقائياً
- إدارة البدلات والخصومات
- حساب مكافأة نهاية الخدمة
- إنشاء كشوف الرواتب

### 7. 📊 تطبيق التقارير (Reports)
```python
apps/reports/
├── 📄 __init__.py
├── 📄 models.py                    # نماذج التقارير المحفوظة
├── 📄 views.py                     # عمليات إنشاء وعرض التقارير
├── 📄 forms.py                     # نماذج فلترة التقارير
├── 📄 urls.py                      # روابط التقارير
├── 📄 generators.py                # مولدات التقارير المختلفة
├── 📄 exporters.py                 # تصدير للـ PDF وExcel
├── 📄 chart_utils.py               # إنشاء الرسوم البيانية
└── 📁 migrations/
```

**الوظائف الرئيسية**:
- إنشاء تقارير مفصلة ومخصصة
- تصدير التقارير بصيغ مختلفة
- رسوم بيانية وإحصائيات
- جدولة التقارير التلقائية

---

## 🗃 تصميم قاعدة البيانات

### نموذج البيانات الأساسي (ERD):

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Companies     │    │   Departments   │    │   Employees     │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ id (PK)         │◄──┐│ id (PK)         │◄──┐│ id (PK)         │
│ name            │   ││ company_id (FK) │   ││ employee_id     │
│ commercial_reg  │   ││ name            │   ││ company_id (FK) │
│ tax_number      │   ││ description     │   ││ department_id   │
│ logo            │   ││ manager_id      │   ││ national_id     │
│ settings        │   │└─────────────────┘   ││ name            │
│ is_active       │   │                      ││ email           │
│ created_at      │   │┌─────────────────┐   ││ phone           │
└─────────────────┘   ││   Positions     │   ││ hire_date       │
                      │├─────────────────┤   ││ position_id     │
                      ││ id (PK)         │◄──┤│ basic_salary    │
                      ││ department_id   │   ││ status          │
                      ││ title           │   ││ is_active       │
                      ││ level           │   │└─────────────────┘
                      ││ requirements    │   │
                      │└─────────────────┘   │
                      │                      │
┌─────────────────┐   │                      │   ┌─────────────────┐
│   Attendance    │   │                      │   │    Leaves       │
├─────────────────┤   │                      │   ├─────────────────┤
│ id (PK)         │   │                      │   │ id (PK)         │
│ employee_id (FK)│───┘                      └───│ employee_id (FK)│
│ date            │                              │ leave_type_id   │
│ check_in        │                              │ start_date      │
│ check_out       │                              │ end_date        │
│ location_lat    │                              │ days_count      │
│ location_lng    │                              │ status          │
│ work_hours      │                              │ applied_at      │
│ overtime_hours  │                              │ approved_at     │
│ status          │                              │ approved_by     │
└─────────────────┘                              └─────────────────┘

┌─────────────────┐                              ┌─────────────────┐
│    Payroll      │                              │  Leave_Types    │
├─────────────────┤                              ├─────────────────┤
│ id (PK)         │                              │ id (PK)         │
│ employee_id (FK)│──────────────────────────────│ company_id (FK) │
│ month           │                              │ name            │
│ year            │                              │ max_days        │
│ basic_salary    │                              │ is_paid         │
│ allowances      │                              │ rules           │
│ deductions      │                              │ is_active       │
│ overtime_pay    │                              └─────────────────┘
│ net_salary      │
│ generated_at    │
└─────────────────┘
```

### الجداول الأساسية:

#### 1. جدول الشركات (Companies)
```sql
CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200) NOT NULL,
    commercial_registration VARCHAR(50),
    tax_number VARCHAR(50),
    logo VARCHAR(200),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(200),
    settings JSON,  -- إعدادات مخصصة لكل شركة
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### 2. جدول الموظفين (Employees)
```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id VARCHAR(20) UNIQUE,  -- رقم الموظف
    company_id INTEGER REFERENCES companies(id),
    department_id INTEGER REFERENCES departments(id),
    position_id INTEGER REFERENCES positions(id),
    
    -- البيانات الشخصية
    national_id VARCHAR(10) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    birth_date DATE,
    gender VARCHAR(10),
    nationality VARCHAR(50),
    
    -- البيانات الوظيفية
    hire_date DATE NOT NULL,
    contract_type VARCHAR(20),
    basic_salary DECIMAL(10,2),
    work_hours_per_day INTEGER DEFAULT 8,
    work_days_per_week INTEGER DEFAULT 6,
    
    -- حالة الموظف
    status VARCHAR(20) DEFAULT 'active',  -- active, suspended, terminated
    termination_date DATE,
    termination_reason TEXT,
    
    -- بيانات النظام
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    last_login DATETIME,
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### 3. جدول الحضور (Attendance)
```sql
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER REFERENCES employees(id),
    date DATE NOT NULL,
    
    -- أوقات الحضور والانصراف
    check_in_time TIME,
    check_out_time TIME,
    break_start_time TIME,
    break_end_time TIME,
    
    -- الموقع الجغرافي
    check_in_location_lat DECIMAL(10,8),
    check_in_location_lng DECIMAL(11,8),
    check_out_location_lat DECIMAL(10,8),
    check_out_location_lng DECIMAL(11,8),
    
    -- الحسابات
    work_hours DECIMAL(4,2),
    overtime_hours DECIMAL(4,2),
    late_minutes INTEGER DEFAULT 0,
    early_leave_minutes INTEGER DEFAULT 0,
    
    -- الحالة
    status VARCHAR(20),  -- present, absent, late, early_leave
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔧 الأدوات والمكتبات المطلوبة

### متطلبات Python الأساسية:
```python
# requirements.txt
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
django-crispy-forms==2.1
crispy-bootstrap5==0.7

# قاعدة البيانات
mysqlclient==2.2.0  # إذا استخدمت MySQL

# معالجة الصور والملفات
Pillow==10.0.1
python-decouple==3.8

# التقارير والتصدير
reportlab==4.0.4
openpyxl==3.1.2
xlsxwriter==3.1.9

# المهام غير المتزامنة
celery==5.3.4
redis==5.0.1

# الأمان
cryptography==41.0.7
bcrypt==4.0.1

# التاريخ والوقت
python-dateutil==2.8.2
pytz==2023.3

# إدارة البيئة
python-dotenv==1.0.0

# اختبارات
pytest==7.4.3
pytest-django==4.6.0
factory-boy==3.3.0

# لتطوير
django-debug-toolbar==4.2.0
```

### مكتبات JavaScript:
```javascript
// package.json للواجهة الأمامية
{
  "dependencies": {
    "bootstrap": "^5.3.2",
    "jquery": "^3.7.1",
    "chart.js": "^4.4.0",
    "moment.js": "^2.29.4",
    "sweetalert2": "^11.7.32",
    "datatables.net": "^1.13.6",
    "select2": "^4.1.0-rc.0",
    "leaflet": "^1.9.4"  // للخرائط والموقع
  }
}
```

---

## 🔧 إعدادات Django المخصصة

### ملف settings.py الأساسي:
```python
# hr_system/settings.py
import os
from decouple import config

# إعدادات أساسية
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # تطبيقات خارجية
    'rest_framework',
    'corsheaders',
    'crispy_forms',
    'crispy_bootstrap5',
    
    # تطبيقات المشروع
    'apps.authentication',
    'apps.companies',
    'apps.employees',
    'apps.attendance',
    'apps.leaves',
    'apps.payroll',
    'apps.reports',
]

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# الأمان
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# الدولية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ملفات الرفع
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# إعدادات REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

---

## 🚀 خطة التطوير والتنفيذ

### المرحلة الأولى: الأساسيات (4-6 أسابيع)
1. **إعداد البيئة والهيكل الأساسي**
2. **تطبيق المصادقة ونظام الصلاحيات**
3. **تطبيق الشركات والموظفين**
4. **الواجهات الأساسية والتصميم**

### المرحلة الثانية: الوظائف الأساسية (6-8 أسابيع)
1. **تطبيق الحضور والانصراف**
2. **تطبيق الإجازات والموافقات**
3. **تطبيق الرواتب والحسابات**
4. **التقارير الأساسية**

### المرحلة الثالثة: الميزات المتقدمة (4-6 أسابيع)
1. **التدريب وتقييم الأداء**
2. **الشكاوى والمقترحات**
3. **إدارة الأصول والاجتماعات**
4. **تطبيق الجوال (API)**

### المرحلة الرابعة: التحسين والاختبار (2-4 أسابيع)
1. **اختبارات شاملة ونظام الأخطاء**
2. **تحسين الأداء والأمان**
3. **الوثائق الشاملة**
4. **التحضير للنشر التجاري**

---

**📝 ملاحظة**: هذا التصميم المعماري قابل للتطوير والتحديث حسب احتياجات المشروع ومتطلبات السوق.
