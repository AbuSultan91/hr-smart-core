# 🛠 دليل التثبيت والإعداد الشامل

**تاريخ الإنشاء**: 3 أغسطس 2025  
**آخر تحديث**: 3 أغسطس 2025  
**الإصدار**: 1.0.0

---

## 📋 متطلبات النظام

### المتطلبات الأساسية:
- **نظام التشغيل**: Windows 10/11, macOS 10.15+, Ubuntu 18.04+
- **Python**: الإصدار 3.9 أو أحدث
- **الذاكرة**: 4 جيجابايت RAM كحد أدنى (يُفضل 8 جيجابايت)
- **التخزين**: 10 جيجابايت مساحة فارغة
- **الاتصال**: إنترنت لتحميل المتطلبات

### البرامج المطلوبة:
- **Git**: لإدارة النسخ والتحديثات
- **محرر النصوص**: VS Code, PyCharm, أو أي محرر تفضله
- **متصفح حديث**: Chrome, Firefox, Safari, Edge

---

## 🚀 التثبيت خطوة بخطوة

### الخطوة 1: تحضير البيئة

#### أ) تثبيت Python:
```bash
# تحقق من وجود Python
python --version
# يجب أن تكون النتيجة Python 3.9.x أو أحدث

# إذا لم يكن مثبتاً، حمل من الموقع الرسمي:
# https://www.python.org/downloads/
```

#### ب) تثبيت Git:
```bash
# تحقق من وجود Git
git --version

# إذا لم يكن مثبتاً، حمل من:
# https://git-scm.com/downloads
```

#### ج) إنشاء مجلد المشروع:
```bash
# إنشاء مجلد المشروع
mkdir hr_smart_core
cd hr_smart_core

# تهيئة Git
git init
```

### الخطوة 2: إعداد البيئة الافتراضية

#### أ) إنشاء البيئة الافتراضية:
```bash
# إنشاء البيئة الافتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
# في Windows:
venv\Scripts\activate

# في macOS/Linux:
source venv/bin/activate
```

#### ب) التحقق من تفعيل البيئة:
```bash
# يجب أن ترى (venv) في بداية سطر الأوامر
(venv) C:\hr_smart_core>
```

### الخطوة 3: تثبيت المتطلبات

#### أ) إنشاء ملف المتطلبات:
```bash
# إنشاء ملف requirements.txt
touch requirements.txt
```

#### ب) محتوى ملف requirements.txt:
```python
# متطلبات Django الأساسية
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
django-crispy-forms==2.1
crispy-bootstrap5==0.7

# قاعدة البيانات
# اختر واحداً حسب احتياجاتك:
# mysqlclient==2.2.0      # للـ MySQL
# psycopg2-binary==2.9.7  # للـ PostgreSQL

# معالجة الصور والملفات
Pillow==10.0.1
python-decouple==3.8

# التقارير والتصدير
reportlab==4.0.4
openpyxl==3.1.2
xlsxwriter==3.1.9

# المهام غير المتزامنة (اختياري)
celery==5.3.4
redis==5.0.1

# الأمان
cryptography==41.0.7

# التاريخ والوقت
python-dateutil==2.8.2
pytz==2023.3

# إدارة البيئة
python-dotenv==1.0.0

# للتطوير والاختبار
django-debug-toolbar==4.2.0
pytest==7.4.3
pytest-django==4.6.0
```

#### ج) تثبيت المتطلبات:
```bash
# تحديث pip لأحدث إصدار
pip install --upgrade pip

# تثبيت جميع المتطلبات
pip install -r requirements.txt
```

### الخطوة 4: إنشاء هيكل المشروع

#### أ) إنشاء مشروع Django:
```bash
# إنشاء المشروع الأساسي
django-admin startproject hr_system .

# إنشاء مجلد التطبيقات
mkdir apps

# إنشاء ملف __init__.py في مجلد apps
touch apps/__init__.py
```

#### ب) إنشاء التطبيقات الأساسية:
```bash
# الانتقال لمجلد التطبيقات
cd apps

# إنشاء تطبيق المصادقة
python ../manage.py startapp authentication

# إنشاء تطبيق الشركات
python ../manage.py startapp companies

# إنشاء تطبيق الموظفين
python ../manage.py startapp employees

# إنشاء تطبيق الحضور
python ../manage.py startapp attendance

# إنشاء تطبيق الإجازات
python ../manage.py startapp leaves

# إنشاء تطبيق الرواتب
python ../manage.py startapp payroll

# إنشاء تطبيق التقارير
python ../manage.py startapp reports

# العودة للمجلد الرئيسي
cd ..
```

#### ج) إنشاء المجلدات الإضافية:
```bash
# إنشاء المجلدات المطلوبة
mkdir static
mkdir media
mkdir templates
mkdir utils
mkdir tests
mkdir scripts
mkdir documentation
mkdir deployment

# إنشاء المجلدات الفرعية للملفات الثابتة
mkdir static/css
mkdir static/js
mkdir static/images
mkdir static/fonts
mkdir static/libs

# إنشاء المجلدات الفرعية للملفات المرفوعة
mkdir media/profile_pictures
mkdir media/documents
mkdir media/attachments
mkdir media/reports

# إنشاء المجلدات الفرعية للقوالب
mkdir templates/base
mkdir templates/auth
mkdir templates/dashboard
mkdir templates/employees
mkdir templates/reports
mkdir templates/components
```

### الخطوة 5: إعداد الإعدادات الأساسية

#### أ) إنشاء ملف البيئة (.env):
```bash
# إنشاء ملف .env
touch .env
```

#### ب) محتوى ملف .env:
```python
# إعدادات التطوير
DEBUG=True
SECRET_KEY=your-very-secret-key-here-change-this-in-production

# قاعدة البيانات
DATABASE_URL=sqlite:///db.sqlite3

# إعدادات الأمان
ALLOWED_HOSTS=localhost,127.0.0.1

# إعدادات البريد الإلكتروني (اختياري)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# إعدادات الملفات
MEDIA_ROOT=media/
STATIC_ROOT=staticfiles/

# إعدادات Redis (للمهام غير المتزامنة)
REDIS_URL=redis://localhost:6379/0
```

#### ج) تعديل ملف settings.py:
```python
# hr_system/settings.py
import os
from pathlib import Path
from decouple import config

# بناء المسارات
BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات الأمان
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
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

# الوسطاء
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hr_system.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# الدولية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# ملفات الرفع
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# إعدادات REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# إعدادات Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# إعدادات CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# إعدادات الجلسات
SESSION_COOKIE_AGE = 86400  # 24 ساعة
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# إعدادات التطوير
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
```

### الخطوة 6: إعداد قاعدة البيانات

#### أ) إنشاء الهجرات الأولى:
```bash
# إنشاء هجرات قاعدة البيانات
python manage.py makemigrations

# تطبيق الهجرات
python manage.py migrate
```

#### ب) إنشاء مستخدم المدير:
```bash
# إنشاء حساب المدير
python manage.py createsuperuser

# أدخل البيانات التالية عند المطالبة:
# Username: admin
# Email: admin@example.com
# Password: admin123 (أو كلمة مرور قوية)
```

### الخطوة 7: إعداد الملفات الثابتة

#### أ) تحميل Bootstrap وjQuery:
```bash
# إنشاء مجلد المكتبات
mkdir static/libs/bootstrap
mkdir static/libs/jquery
mkdir static/libs/fontawesome

# يمكنك تحميل الملفات من:
# Bootstrap: https://getbootstrap.com/
# jQuery: https://jquery.com/
# Font Awesome: https://fontawesome.com/
```

#### ب) إنشاء ملفات CSS وJS مخصصة:
```bash
# إنشاء ملفات CSS مخصصة
touch static/css/main.css
touch static/css/rtl.css
touch static/css/dashboard.css

# إنشاء ملفات JavaScript مخصصة
touch static/js/main.js
touch static/js/dashboard.js
touch static/js/attendance.js
```

### الخطوة 8: إنشاء القوالب الأساسية

#### أ) إنشاء القالب الأساسي:
```bash
# إنشاء القالب الأساسي
touch templates/base/base.html
```

#### ب) محتوى القالب الأساسي (base.html):
```html
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}HR Smart Core{% endblock %}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    
    <!-- ملفات CSS مخصصة -->
    {% load static %}
    <link href="{% static 'css/main.css' %}" rel="stylesheet">
    <link href="{% static 'css/rtl.css' %}" rel="stylesheet">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- رأس الصفحة -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <i class="fas fa-users"></i> HR Smart Core
            </a>
            <div class="navbar-nav ms-auto">
                {% if user.is_authenticated %}
                    <span class="navbar-text me-3">
                        مرحباً، {{ user.get_full_name|default:user.username }}
                    </span>
                    <a class="nav-link" href="{% url 'logout' %}">
                        <i class="fas fa-sign-out-alt"></i> تسجيل الخروج
                    </a>
                {% endif %}
            </div>
        </div>
    </nav>

    <!-- المحتوى الرئيسي -->
    <main class="container-fluid mt-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </main>

    <!-- ذيل الصفحة -->
    <footer class="bg-light text-center py-3 mt-5">
        <div class="container">
            <p class="text-muted mb-0">
                © 2025 HR Smart Core - جميع الحقوق محفوظة
            </p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    
    <!-- ملفات JS مخصصة -->
    <script src="{% static 'js/main.js' %}"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### الخطوة 9: إنشاء صفحة الدخول

#### أ) إنشاء قالب تسجيل الدخول:
```bash
touch templates/auth/login.html
```

#### ب) محتوى صفحة الدخول:
```html
{% extends 'base/base.html' %}
{% load static %}

{% block title %}تسجيل الدخول - HR Smart Core{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-4">
        <div class="card">
            <div class="card-header text-center">
                <h4><i class="fas fa-sign-in-alt"></i> تسجيل الدخول</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="username" class="form-label">اسم المستخدم</label>
                        <input type="text" class="form-control" id="username" name="username" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">كلمة المرور</label>
                        <input type="password" class="form-control" id="password" name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">
                        <i class="fas fa-sign-in-alt"></i> دخول
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### الخطوة 10: إعداد URLs

#### أ) إعداد URLs الرئيسية:
```python
# hr_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('', include('apps.dashboard.urls')),  # سننشئه لاحقاً
]

# إضافة ملفات الوسائط في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

#### ب) إنشاء URLs للمصادقة:
```bash
touch apps/authentication/urls.py
```

```python
# apps/authentication/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'auth'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

### الخطوة 11: اختبار التثبيت

#### أ) تشغيل الخادم المحلي:
```bash
# تشغيل الخادم
python manage.py runserver

# ستظهر رسالة مشابهة لهذه:
# Starting development server at http://127.0.0.1:8000/
```

#### ب) اختبار الوصول:
1. افتح المتصفح واذهب إلى: `http://127.0.0.1:8000/admin/`
2. سجل الدخول بحساب المدير الذي أنشأته
3. تأكد من عمل لوحة الإدارة بشكل صحيح

---

## 🔧 إعدادات إضافية

### إعداد قاعدة بيانات MySQL (اختياري):

#### أ) تثبيت MySQL:
```bash
# في Ubuntu:
sudo apt-get install mysql-server

# في macOS:
brew install mysql

# في Windows: حمل من الموقع الرسمي
```

#### ب) إنشاء قاعدة بيانات:
```sql
-- اتصل بـ MySQL
mysql -u root -p

-- إنشاء قاعدة بيانات
CREATE DATABASE hr_smart_core CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- إنشاء مستخدم
CREATE USER 'hr_user'@'localhost' IDENTIFIED BY 'your_password';

-- منح الصلاحيات
GRANT ALL PRIVILEGES ON hr_smart_core.* TO 'hr_user'@'localhost';
FLUSH PRIVILEGES;
```

#### ج) تحديث إعدادات Django:
```python
# في ملف .env
DATABASE_URL=mysql://hr_user:your_password@localhost/hr_smart_core

# في settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hr_smart_core',
        'USER': 'hr_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
```

### إعداد Redis (للمهام غير المتزامنة):

#### أ) تثبيت Redis:
```bash
# في Ubuntu:
sudo apt-get install redis-server

# في macOS:
brew install redis

# في Windows: حمل من الموقع الرسمي
```

#### ب) تشغيل Redis:
```bash
# تشغيل خادم Redis
redis-server

# في نافذة طرفية أخرى، اختبر الاتصال
redis-cli ping
# يجب أن ترى: PONG
```

---

## 🐛 استكشاف الأخطاء الشائعة

### مشكلة: خطأ في تثبيت mysqlclient
```bash
# الحل في Windows:
pip install mysqlclient

# إذا فشل، استخدم:
pip install wheel
pip install --only-binary=all mysqlclient

# أو استخدم:
pip install PyMySQL
# ثم أضف في settings.py:
import pymysql
pymysql.install_as_MySQLdb()
```

### مشكلة: خطأ في تشغيل migrations
```bash
# احذف ملفات migrations القديمة
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# أنشئ migrations جديدة
python manage.py makemigrations
python manage.py migrate
```

### مشكلة: الملفات الثابتة لا تظهر
```bash
# جمع الملفات الثابتة
python manage.py collectstatic

# تأكد من إعدادات STATIC_URL و STATICFILES_DIRS
```

### مشكلة: خطأ في encoding للعربية
```python
# تأكد من إعدادات قاعدة البيانات في settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

# وأضف في أعلى ملف settings.py:
import locale
locale.setlocale(locale.LC_ALL, 'ar_SA.UTF-8')
```

---

## ✅ قائمة التحقق بعد التثبيت

- [ ] Python 3.9+ مثبت ويعمل
- [ ] البيئة الافتراضية مُنشأة ومُفعلة
- [ ] جميع المتطلبات مثبتة بنجاح
- [ ] هيكل المشروع مُنشأ بالكامل
- [ ] إعدادات Django مُحدثة ومُخصصة
- [ ] قاعدة البيانات مُنشأة والهجرات مُطبقة
- [ ] حساب المدير مُنشأ ويعمل
- [ ] الخادم المحلي يعمل بدون أخطاء
- [ ] لوحة الإدارة يمكن الوصول إليها
- [ ] الملفات الثابتة تُحمل بشكل صحيح
- [ ] ملف .env مُنشأ ومُحدث
- [ ] Git مُهيأ والملفات مُتتبعة

---

## 🔄 النسخ الاحتياطي الأولي

بعد اكتمال التثبيت، قم بإنشاء نسخة احتياطية:

```bash
# إنشاء نسخة احتياطية من قاعدة البيانات
python manage.py dumpdata > initial_backup.json

# إنشاء git repository
git add .
git commit -m "Initial project setup"

# (اختياري) رفع للـ repository
git remote add origin https://github.com/yourusername/hr_smart_core.git
git push -u origin main
```

---

**🎉 تهانينا! تم تثبيت وإعداد HR Smart Core بنجاح!**

**الخطوة التالية**: راجع `05_development_guide.md` لبدء تطوير الميزات الأساسية.
