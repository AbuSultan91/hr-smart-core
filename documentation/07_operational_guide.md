# 📂 دليل التشغيل الشامل للمشروع

**تاريخ الإنشاء**: 3 أغسطس 2025  
**آخر تحديث**: 3 أغسطس 2025  
**الإصدار**: 1.0.0

---

## 🎯 الغرض من هذا الدليل

هذا الدليل سيعلمك كيفية تشغيل وإدارة مشروع HR Smart Core في البيئات المختلفة (التطوير، الاختبار، الإنتاج) مع جميع السكريبتات والأوامر اللازمة.

---

## 🚀 السكريبتات والأوامر الأساسية

### سكريبتات إعداد المشروع

#### 1. سكريبت التثبيت الأولي
```bash
# scripts/setup.sh (Linux/macOS) أو setup.bat (Windows)

#!/bin/bash
echo "🚀 بدء إعداد مشروع HR Smart Core..."

# تحقق من وجود Python
python --version
if [ $? -ne 0 ]; then
    echo "❌ Python غير مثبت! يرجى تثبيت Python 3.9+"
    exit 1
fi

echo "✅ Python موجود"

# إنشاء البيئة الافتراضية
echo "📦 إنشاء البيئة الافتراضية..."
python -m venv venv

# تفعيل البيئة الافتراضية
echo "🔧 تفعيل البيئة الافتراضية..."
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# تحديث pip
echo "⬆️ تحديث pip..."
pip install --upgrade pip

# تثبيت المتطلبات
echo "📥 تثبيت المتطلبات..."
pip install -r requirements.txt

# إنشاء ملف .env إذا لم يكن موجود
if [ ! -f .env ]; then
    echo "⚙️ إنشاء ملف .env..."
    cp .env.example .env
    echo "⚠️ يرجى تحديث ملف .env بالإعدادات المناسبة"
fi

# إنشاء قاعدة البيانات
echo "🗃 إعداد قاعدة البيانات..."
python manage.py makemigrations
python manage.py migrate

# إنشاء مستخدم مدير
echo "👤 إنشاء حساب المدير..."
python manage.py createsuperuser

# جمع الملفات الثابتة
echo "📁 جمع الملفات الثابتة..."
python manage.py collectstatic --noinput

echo "🎉 تم إعداد المشروع بنجاح!"
echo "ℹ️ لتشغيل النظام: ./scripts/run.sh"
```

#### 2. سكريبت التشغيل
```bash
# scripts/run.sh
#!/bin/bash

echo "🚀 تشغيل HR Smart Core..."

# تفعيل البيئة الافتراضية
source venv/bin/activate

# تحقق من التحديثات
echo "🔄 تحقق من تحديثات قاعدة البيانات..."
python manage.py migrate

# تشغيل الخادم
echo "🌐 تشغيل خادم التطوير..."
python manage.py runserver 0.0.0.0:8000
```

#### 3. سكريبت النسخ الاحتياطي
```bash
# scripts/backup.sh
#!/bin/bash

BACKUP_DIR="backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/backup_${DATE}.json"

echo "💾 إنشاء نسخة احتياطية..."

# إنشاء مجلد النسخ الاحتياطي
mkdir -p $BACKUP_DIR

# تفعيل البيئة الافتراضية
source venv/bin/activate

# إنشاء النسخة الاحتياطية
python manage.py dumpdata --natural-foreign --natural-primary > $BACKUP_FILE

# ضغط النسخة الاحتياطية
gzip $BACKUP_FILE

echo "✅ تم إنشاء النسخة الاحتياطية: ${BACKUP_FILE}.gz"

# حذف النسخ القديمة (أكثر من 30 يوم)
find $BACKUP_DIR -name "backup_*.json.gz" -mtime +30 -delete
echo "🗑 تم حذف النسخ الاحتياطية القديمة"
```

#### 4. سكريبت الاستعادة
```bash
# scripts/restore.sh
#!/bin/bash

if [ $# -eq 0 ]; then
    echo "❌ يرجى تحديد ملف النسخة الاحتياطية"
    echo "الاستخدام: ./scripts/restore.sh backup_file.json.gz"
    exit 1
fi

BACKUP_FILE=$1

echo "📥 استعادة البيانات من: $BACKUP_FILE"

# تفعيل البيئة الافتراضية
source venv/bin/activate

# فك ضغط الملف إذا كان مضغوط
if [[ $BACKUP_FILE == *.gz ]]; then
    gunzip -c $BACKUP_FILE > temp_restore.json
    RESTORE_FILE="temp_restore.json"
else
    RESTORE_FILE=$BACKUP_FILE
fi

# تأكيد الاستعادة
read -p "⚠️ هذا سيمحو جميع البيانات الحالية. هل تريد المتابعة؟ (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # مسح قاعدة البيانات
    python manage.py flush --noinput
    
    # استعادة البيانات
    python manage.py loaddata $RESTORE_FILE
    
    echo "✅ تم استعادة البيانات بنجاح"
    
    # حذف الملف المؤقت
    if [ -f "temp_restore.json" ]; then
        rm temp_restore.json
    fi
else
    echo "❌ تم إلغاء العملية"
fi
```

---

## 🔧 أوامر إدارة النظام

### أوامر Django الأساسية

#### إدارة قاعدة البيانات:
```bash
# إنشاء هجرات جديدة
python manage.py makemigrations

# تطبيق الهجرات
python manage.py migrate

# إظهار حالة الهجرات
python manage.py showmigrations

# التراجع عن هجرة معينة
python manage.py migrate app_name migration_name

# مسح قاعدة البيانات (احذر!)
python manage.py flush

# إنشاء قاعدة بيانات جديدة
python manage.py migrate --run-syncdb
```

#### إدارة المستخدمين:
```bash
# إنشاء مستخدم مدير
python manage.py createsuperuser

# تغيير كلمة مرور مستخدم
python manage.py changepassword username

# إنشاء بيانات وهمية للاختبار
python manage.py create_sample_data
```

#### إدارة الملفات الثابتة:
```bash
# جمع الملفات الثابتة
python manage.py collectstatic

# جمع الملفات مع الاستبدال
python manage.py collectstatic --clear --noinput

# العثور على ملفات ثابتة
python manage.py findstatic css/main.css
```

### أوامر مخصصة للمشروع

#### 1. أمر إنشاء بيانات تجريبية
```python
# management/commands/create_sample_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.companies.models import Company
from apps.employees.models import Employee, Department
from faker import Faker
import random

class Command(BaseCommand):
    help = 'إنشاء بيانات تجريبية للاختبار'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--employees',
            type=int,
            default=50,
            help='عدد الموظفين المراد إنشاؤهم'
        )
        parser.add_argument(
            '--companies',
            type=int,
            default=1,
            help='عدد الشركات المراد إنشاؤها'
        )
    
    def handle(self, *args, **options):
        fake = Faker('ar_SA')
        employees_count = options['employees']
        companies_count = options['companies']
        
        self.stdout.write('🏢 إنشاء الشركات...')
        companies = []
        for i in range(companies_count):
            company = Company.objects.create(
                name=f'شركة {fake.company()}',
                commercial_registration=fake.numerify('##########'),
                tax_number=fake.numerify('###-###-###'),
                address=fake.address(),
                phone=fake.phone_number(),
                email=fake.company_email()
            )
            companies.append(company)
            self.stdout.write(f'  ✅ تم إنشاء: {company.name}')
        
        self.stdout.write('🏢 إنشاء الأقسام...')
        departments = []
        dept_names = ['الموارد البشرية', 'المالية', 'التقنية', 'المبيعات', 'التسويق']
        for company in companies:
            for dept_name in dept_names:
                dept = Department.objects.create(
                    company=company,
                    name=dept_name,
                    description=f'قسم {dept_name} في {company.name}'
                )
                departments.append(dept)
        
        self.stdout.write('👥 إنشاء الموظفين...')
        for i in range(employees_count):
            national_id = fake.numerify('##########')
            company = random.choice(companies)
            department = random.choice([d for d in departments if d.company == company])
            
            employee = Employee.objects.create(
                employee_id=f'EMP{i+1:04d}',
                national_id=national_id,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=22, maximum_age=60),
                gender=random.choice(['M', 'F']),
                phone=fake.phone_number(),
                email=fake.email(),
                address=fake.address(),
                company=company,
                department=department,
                hire_date=fake.date_between(start_date='-5y', end_date='today'),
                basic_salary=random.randint(3000, 15000)
            )
            
            # إنشاء حساب مستخدم
            User.objects.create_user(
                username=national_id[-4:],
                password=national_id[:4],
                email=employee.email,
                first_name=employee.first_name,
                last_name=employee.last_name
            )
            
            if (i + 1) % 10 == 0:
                self.stdout.write(f'  📊 تم إنشاء {i + 1} موظف...')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'🎉 تم إنشاء {employees_count} موظف في {companies_count} شركة بنجاح!'
            )
        )

# الاستخدام:
# python manage.py create_sample_data --employees 100 --companies 2
```

#### 2. أمر تنظيف النظام
```python
# management/commands/cleanup_system.py
from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta
import os

class Command(BaseCommand):
    help = 'تنظيف النظام من الملفات والبيانات غير المستخدمة'
    
    def handle(self, *args, **options):
        self.stdout.write('🧹 بدء تنظيف النظام...')
        
        # حذف الجلسات المنتهية
        expired_sessions = Session.objects.filter(
            expire_date__lt=timezone.now()
        )
        sessions_count = expired_sessions.count()
        expired_sessions.delete()
        self.stdout.write(f'  🗑 تم حذف {sessions_count} جلسة منتهية')
        
        # حذف ملفات السجل القديمة
        log_dir = 'logs'
        if os.path.exists(log_dir):
            cutoff_date = timezone.now() - timedelta(days=30)
            for filename in os.listdir(log_dir):
                file_path = os.path.join(log_dir, filename)
                if os.path.isfile(file_path):
                    file_time = timezone.datetime.fromtimestamp(
                        os.path.getmtime(file_path),
                        tz=timezone.get_current_timezone()
                    )
                    if file_time < cutoff_date:
                        os.remove(file_path)
                        self.stdout.write(f'  🗑 تم حذف ملف السجل: {filename}')
        
        # حذف النسخ الاحتياطية القديمة
        backup_dir = 'backups'
        if os.path.exists(backup_dir):
            cutoff_date = timezone.now() - timedelta(days=90)
            for filename in os.listdir(backup_dir):
                if filename.startswith('backup_'):
                    file_path = os.path.join(backup_dir, filename)
                    file_time = timezone.datetime.fromtimestamp(
                        os.path.getmtime(file_path),
                        tz=timezone.get_current_timezone()
                    )
                    if file_time < cutoff_date:
                        os.remove(file_path)
                        self.stdout.write(f'  🗑 تم حذف النسخة الاحتياطية: {filename}')
        
        self.stdout.write(self.style.SUCCESS('✅ تم تنظيف النظام بنجاح!'))

# الاستخدام:
# python manage.py cleanup_system
```

#### 3. أمر إنشاء تقرير النظام
```python
# management/commands/system_report.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.companies.models import Company
from apps.employees.models import Employee
from apps.attendance.models import AttendanceRecord
from django.utils import timezone
import psutil
import platform

class Command(BaseCommand):
    help = 'إنشاء تقرير حالة النظام'
    
    def handle(self, *args, **options):
        self.stdout.write('📊 إنشاء تقرير حالة النظام...')
        self.stdout.write('=' * 50)
        
        # معلومات النظام
        self.stdout.write('🖥 معلومات النظام:')
        self.stdout.write(f'  نظام التشغيل: {platform.system()} {platform.release()}')
        self.stdout.write(f'  البروسيسور: {platform.processor()}')
        self.stdout.write(f'  استخدام المعالج: {psutil.cpu_percent()}%')
        self.stdout.write(f'  استخدام الذاكرة: {psutil.virtual_memory().percent}%')
        self.stdout.write(f'  مساحة القرص المتاحة: {psutil.disk_usage("/").free // (1024**3)} GB')
        
        # إحصائيات قاعدة البيانات
        self.stdout.write('\n📊 إحصائيات البيانات:')
        companies_count = Company.objects.count()
        employees_count = Employee.objects.count()
        users_count = User.objects.count()
        attendance_count = AttendanceRecord.objects.count()
        
        self.stdout.write(f'  عدد الشركات: {companies_count}')
        self.stdout.write(f'  عدد الموظفين: {employees_count}')
        self.stdout.write(f'  عدد المستخدمين: {users_count}')
        self.stdout.write(f'  عدد سجلات الحضور: {attendance_count}')
        
        # الموظفين النشطين
        active_employees = Employee.objects.filter(status='active').count()
        inactive_employees = employees_count - active_employees
        
        self.stdout.write(f'  الموظفين النشطين: {active_employees}')
        self.stdout.write(f'  الموظفين غير النشطين: {inactive_employees}')
        
        # حضور اليوم
        today = timezone.now().date()
        today_attendance = AttendanceRecord.objects.filter(date=today).count()
        self.stdout.write(f'  حضور اليوم: {today_attendance}')
        
        # أحدث النشاطات
        self.stdout.write('\n📈 أحدث النشاطات:')
        recent_employees = Employee.objects.order_by('-created_at')[:5]
        for emp in recent_employees:
            self.stdout.write(f'  موظف جديد: {emp.full_name} ({emp.created_at.strftime("%Y-%m-%d")})')
        
        self.stdout.write('=' * 50)
        self.stdout.write(self.style.SUCCESS('✅ تم إنشاء التقرير بنجاح!'))

# الاستخدام:
# python manage.py system_report
```

---

## 📊 مراقبة النظام

### سكريبت مراقبة الأداء
```bash
# scripts/monitor.sh
#!/bin/bash

echo "📊 مراقبة أداء HR Smart Core"
echo "================================"

# تفعيل البيئة الافتراضية
source venv/bin/activate

# مراقبة استخدام الموارد
echo "🖥 استخدام الموارد:"
echo "  المعالج: $(python -c "import psutil; print(f'{psutil.cpu_percent()}%')")"
echo "  الذاكرة: $(python -c "import psutil; print(f'{psutil.virtual_memory().percent}%')")"
echo "  القرص: $(python -c "import psutil; print(f'{psutil.disk_usage(\"/\").percent}%')")"

# مراقبة قاعدة البيانات
echo -e "\n🗃 حالة قاعدة البيانات:"
python manage.py system_report

# مراقبة السجلات
echo -e "\n📝 آخر السجلات:"
if [ -f "logs/django.log" ]; then
    tail -n 10 logs/django.log
else
    echo "  لا توجد سجلات"
fi

# مراقبة العمليات
echo -e "\n🔄 العمليات النشطة:"
ps aux | grep python | grep manage.py
```

### سكريبت الفحص الصحي
```bash
# scripts/health_check.sh
#!/bin/bash

echo "🏥 فحص صحة النظام"
echo "==================="

# تفعيل البيئة الافتراضية
source venv/bin/activate

# فحص قاعدة البيانات
echo "🗃 فحص قاعدة البيانات..."
python manage.py check --database default
if [ $? -eq 0 ]; then
    echo "  ✅ قاعدة البيانات تعمل بشكل طبيعي"
else
    echo "  ❌ مشكلة في قاعدة البيانات"
fi

# فحص الهجرات
echo -e "\n📦 فحص الهجرات..."
python manage.py showmigrations --plan | grep '\[ \]'
if [ $? -ne 0 ]; then
    echo "  ✅ جميع الهجرات مطبقة"
else
    echo "  ⚠️ توجد هجرات غير مطبقة"
fi

# فحص الأمان
echo -e "\n🔒 فحص الأمان..."
python manage.py check --deploy
if [ $? -eq 0 ]; then
    echo "  ✅ فحص الأمان نجح"
else
    echo "  ⚠️ توجد مشاكل أمنية"
fi

# فحص الملفات الثابتة
echo -e "\n📁 فحص الملفات الثابتة..."
if [ -d "staticfiles" ]; then
    echo "  ✅ الملفات الثابتة موجودة"
else
    echo "  ⚠️ الملفات الثابتة غير موجودة - تشغيل collectstatic"
    python manage.py collectstatic --noinput
fi

# اختبار الاتصال
echo -e "\n🌐 اختبار الاتصال..."
timeout 5 python manage.py check --database default > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "  ✅ النظام يستجيب"
else
    echo "  ❌ النظام لا يستجيب"
fi

echo -e "\n🎉 انتهى فحص صحة النظام"
```

---

## 🔄 أتمتة المهام

### جدولة المهام باستخدام Cron (Linux/macOS)

#### 1. إعداد ملف crontab:
```bash
# تحرير جدولة المهام
crontab -e

# إضافة المهام التالية:

# نسخة احتياطية يومية في الساعة 2:00 صباحاً
0 2 * * * /path/to/hr_smart_core/scripts/backup.sh

# تنظيف النظام أسبوعياً (الأحد 3:00 صباحاً)
0 3 * * 0 /path/to/hr_smart_core/scripts/cleanup.sh

# مراقبة النظام كل 15 دقيقة
*/15 * * * * /path/to/hr_smart_core/scripts/health_check.sh >> /var/log/hr_monitor.log

# تحديث الإحصائيات كل ساعة
0 * * * * cd /path/to/hr_smart_core && python manage.py update_statistics
```

#### 2. سكريبت التحديث التلقائي:
```bash
# scripts/auto_update.sh
#!/bin/bash

echo "🔄 بدء التحديث التلقائي..."

cd /path/to/hr_smart_core

# تفعيل البيئة الافتراضية
source venv/bin/activate

# جلب التحديثات من Git
git fetch origin

# التحقق من وجود تحديثات
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse @{u})

if [ $LOCAL != $REMOTE ]; then
    echo "📥 توجد تحديثات جديدة، جاري التطبيق..."
    
    # إنشاء نسخة احتياطية قبل التحديث
    ./scripts/backup.sh
    
    # سحب التحديثات
    git pull origin main
    
    # تثبيت المتطلبات الجديدة
    pip install -r requirements.txt
    
    # تطبيق هجرات قاعدة البيانات
    python manage.py migrate
    
    # جمع الملفات الثابتة
    python manage.py collectstatic --noinput
    
    # إعادة تشغيل الخدمة (إذا كان يعمل في الإنتاج)
    # sudo systemctl restart hr_smart_core
    
    echo "✅ تم التحديث بنجاح!"
else
    echo "ℹ️ لا توجد تحديثات جديدة"
fi
```

---

## 🐳 التشغيل باستخدام Docker

### ملف Dockerfile:
```dockerfile
# Dockerfile
FROM python:3.9-slim

# إعداد متغيرات البيئة
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# إنشاء مجلد العمل
WORKDIR /app

# تثبيت متطلبات النظام
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gettext \
    && rm -rf /var/lib/apt/lists/*

# نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# نسخ المشروع
COPY . /app/

# إنشاء مستخدم غير مميز
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# تعريض المنفذ
EXPOSE 8000

# نقطة الدخول
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### ملف docker-compose.yml:
```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1
      - DATABASE_URL=postgresql://postgres:password@db:5432/hr_smart_core
    depends_on:
      - db
      - redis

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: hr_smart_core
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:6-alpine
    ports:
      - "6379:6379"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

### أوامر Docker:
```bash
# بناء وتشغيل الحاويات
docker-compose up --build

# تشغيل في الخلفية
docker-compose up -d

# عرض السجلات
docker-compose logs -f

# تشغيل أوامر Django
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic

# إيقاف الخدمات
docker-compose down

# إيقاف مع حذف البيانات
docker-compose down -v
```

---

## ⚠️ استكشاف الأخطاء الشائعة

### مشاكل قاعدة البيانات:
```bash
# خطأ: table doesn't exist
python manage.py migrate --fake-initial

# خطأ: migration conflicts
python manage.py migrate --merge

# إعادة تعيين الهجرات
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate
```

### مشاكل الملفات الثابتة:
```bash
# الملفات الثابتة لا تظهر
python manage.py collectstatic --clear
python manage.py collectstatic

# مشكلة الصلاحيات
sudo chown -R $USER:$USER staticfiles/
sudo chmod -R 755 staticfiles/
```

### مشاكل الأداء:
```bash
# مراقبة استخدام الذاكرة
python manage.py shell -c "import psutil; print(f'Memory: {psutil.virtual_memory().percent}%')"

# مراقبة الاستعلامات البطيئة
# في settings.py أضف:
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

---

## 📋 قائمة مرجعية للتشغيل اليومي

### بداية اليوم:
- [ ] تحقق من صحة النظام: `./scripts/health_check.sh`
- [ ] راجع السجلات: `tail -f logs/django.log`
- [ ] تحقق من النسخ الاحتياطية: `ls -la backups/`
- [ ] مراقبة الأداء: `./scripts/monitor.sh`

### أثناء العمل:
- [ ] اختبار التغييرات قبل التطبيق
- [ ] مراجعة الأخطاء الجديدة
- [ ] متابعة استخدام الموارد

### نهاية اليوم:
- [ ] إنشاء نسخة احتياطية: `./scripts/backup.sh`
- [ ] تنظيف النظام: `python manage.py cleanup_system`
- [ ] حفظ التغييرات في Git
- [ ] مراجعة تقرير اليوم: `python manage.py system_report`

---

**🎉 أهلاً وسهلاً بك في إدارة HR Smart Core!**

هذا الدليل سيساعدك في تشغيل وإدارة النظام بكفاءة عالية.
