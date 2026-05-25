from django.core.management.base import BaseCommand
from portfolio.models import Project, ProjectOverview, ProjectFeature

class Command(BaseCommand):
    help = 'Seeds the database with initial projects'

    def handle(self, *args, **kwargs):
        projects_data = [
            {
                "id": 1,
                "title": "AcaSmart – Desktop Music Academy Management Software",
                "category": "Desktop Application | Python | PySide6 | SQLite",
                "filter_class": "filter-python",
                "image": "portfolio/project-1.webp",
                "media": {
                    "type": "video",
                    "src": "portfolio/project-1-demo.mp4",
                    "poster": "portfolio/project-1.webp",
                },
                "info": {
                    "date": "28/1/2026",
                    "url": "https://github.com/Aramesh-Aria/AcaSmart-repo",
                },
                "overview": [
                    " آموزشگاه پیش از این برای پرداخت‌ها، حضور و غیاب و گزارش‌ها به ثبت دستی و دفتری وابسته بود.",
                    " AcaSmart را به عنوان یک اپ دسکتاپ با Python، PySide6 و SQLite پیاده‌سازی کردم تا مدیریت هنرجو، استاد، کلاس، جلسه و پیامک یادآوری در یک سیستم یکپارچه انجام شود.",
                    " منطق برنامه از رابط کاربری جدا شد و ماژول‌های اصلی مستقل طراحی شدند تا نگه‌داری آسان‌تر و خطاهای عملیاتی کمتر شود.",
                    " فرایندهای ثبت جلسات، پیگیری پرداختی‌ها و آماده‌سازی گزارش برای مدیریت سریع‌تر و قابل اتکاتر شد.",
                ],
                "features": [
                    {
                        "icon": "bi bi-mortarboard",
                        "title": "Student Management",
                        "description": "ثبت و نگه‌داری اطلاعات هنرجو، وضعیت ترم و سوابق پرداخت با ساختار داده‌ای قابل پیگیری.",
                    },
                    {
                        "icon": "bi bi-person-badge",
                        "title": "Teacher & Class Management",
                        "description": "تعریف اساتید، کلاس‌ها و زمان‌بندی جلسات با تمرکز بر جلوگیری از تداخل برنامه.",
                    },
                    {
                        "icon": "bi bi-calendar-check",
                        "title": "Attendance System",
                        "description": "ثبت حضور و غیاب به‌تفکیک جلسه برای بهبود دقت گزارش‌های آموزشی و مالی.",
                    },
                    {
                        "icon": "bi bi-cash-coin",
                        "title": "Financial Reports",
                        "description": "نمایش شهریه، پرداخت و بدهی هنرجویان برای تصمیم‌گیری مدیریتی روزمره.",
                    },
                    {
                        "icon": "bi bi-chat-dots",
                        "title": "Automatic SMS Reminder",
                        "description": "ارسال پیامک یادآور برای کاهش پیگیری‌های دستی و حفظ نظم اجرایی.",
                    },
                ],
            },
            {
                "id": 2,
                "title": "NewsReaderBot – Personalized News Telegram Bot",
                "category": "Telegram Bot | Python | SQLAlchemy | Alembic",
                "filter_class": "filter-python",
                "image": "portfolio/project-2.webp",
                "media": {
                    "type": "video",
                    "src": "portfolio/project-2-demo.mp4",
                    "poster": "portfolio/project-2.webp",
                },
                "info": {
                    "date": "28/1/2026",
                    "url": "https://github.com/Aramesh-Aria/NewsReaderBot",
                },
                "overview": [
                    " به یک ابزار شخصی نیاز داشتم که خبرها را از منابع انتخابی جمع‌آوری و دوره‌ای ارسال کند.",
                    " یک ربات تلگرام با Python ساختم که با تنظیمات کاربر، اخبار را از منابع منتخب دریافت و به‌صورت زمان‌بندی‌شده (هر ۸ ساعت) ارسال می‌کند.",
                    " ذخیره ترجیحات کاربر و لایه داده با SQLAlchemy مدیریت می‌شود و Alembic برای مهاجرت دیتابیس استفاده شده است.",
                    " فرآیند دریافت خبر به جای دریافت از سایت ها به یک ربات تلگرامی قابل تنظیم تبدیل شد.",
                ],
                "features": [
                    {
                        "icon": "bi bi-robot",
                        "title": "Smart Personalized News",
                        "description": "ارسال اخبار شخصی‌سازی‌شده با تمرکز روی تنظیم‌پذیری و پایداری ارسال.",
                    },
                    {
                        "icon": "bi bi-list-check",
                        "title": "Topic & Source Control",
                        "description": "مدیریت موضوعات و منابع خبری توسط کاربر برای حفظ ارتباط محتوایی.",
                    },
                    {
                        "icon": "bi bi-ui-checks-grid",
                        "title": "Interactive Telegram UI",
                        "description": "رابط تعاملی تلگرام با Inline Keyboard برای کاهش خطای ورودی کاربر.",
                    },
                    {
                        "icon": "bi bi-translate",
                        "title": "Multi-language Support",
                        "description": "پشتیبانی فارسی و انگلیسی همراه با ذخیره ترجیحات زبان در دیتابیس.",
                    },
                    {
                        "icon": "bi bi-database-gear",
                        "title": "Robust Data Layer",
                        "description": "لایه داده قابل نگه‌داری با SQLAlchemy و مهاجرت کنترل‌شده با Alembic.",
                    },
                    {
                        "icon": "bi bi-person-gear",
                        "title": "User Preference Management",
                        "description": "ذخیره و به‌روزرسانی ترجیحات برای ارسال مستمر محتوای مرتبط.",
                    },
                ],
            },
            {
                "id": 3,
                "title": "Aramesh Music Academy Website",
                "category": "Web Development | Django | Persian Localization",
                "filter_class": "filter-design",
                "image": "portfolio/project-3.webp",
                "media": {
                    "type": "image",
                    "src": "portfolio/project-3.webp",
                },
                "info": {
                    "date": "2026",
                    "url": "https://aramesh-academy.ir",
                },
                "overview": [
                    " مجموعه برای معرفی خدمات، مدیریت محتوای آموزشی و دریافت درخواست هنرجویان به یک وب‌سایت عملیاتی نیاز داشت.",
                    " وب‌سایت آکادمی آرامش را با Django پیاده‌سازی کردم تا صفحات، گالری، اساتید و برنامه کلاس‌ها از پنل مدیریت قابل به‌روزرسانی باشد.",
                    " مدل‌ها به‌صورت ساختاریافته تعریف شدند، Viewها با الگوی class-based پیاده‌سازی شد و فرم تماس به ثبت پیام در دیتابیس متصل است.",
                    " تیم آموزشگاه بدون وابستگی به تغییر کد، محتوای سایت را مدیریت می‌کند و مسیر ارتباطی هنرجوها رسمی‌تر شده است.",
                ],
                "features": [
                    {
                        "icon": "bi bi-person-video3",
                        "title": "Teacher Directory",
                        "description": "مدیریت پروفایل اساتید برای نمایش سوابق و نقش آموزشی به‌صورت ساختاریافته.",
                    },
                    {
                        "icon": "bi bi-images",
                        "title": "Academy Gallery",
                        "description": "افزودن و ویرایش گالری از پنل مدیریت بدون نیاز به تغییر مستقیم کد.",
                    },
                    {
                        "icon": "bi bi-calendar-event",
                        "title": "Class Schedules",
                        "description": "نمایش و مدیریت برنامه کلاس‌ها با تمرکز بر نظم اطلاعات و به‌روزرسانی سریع.",
                    },
                    {
                        "icon": "bi bi-envelope-check",
                        "title": "Inquiry Management",
                        "description": "فرم تماس متصل به دیتابیس برای ثبت قابل پیگیری پیام‌های ورودی.",
                    },
                ],
            },
        ]

        for p_data in projects_data:
            project, created = Project.objects.update_or_create(
                id=p_data['id'],
                defaults={
                    'title': p_data['title'],
                    'category': p_data['category'],
                    'filter_class': p_data['filter_class'],
                    'image': p_data['image'],
                    'media_type': p_data['media']['type'],
                    'media_src': p_data['media']['src'],
                    'media_poster': p_data['media'].get('poster'),
                    'date': p_data['info']['date'],
                    'url': p_data['info']['url'],
                }
            )
            
            # Clear existing related data to avoid duplicates if re-run
            project.overview_points.all().delete()
            project.features.all().delete()

            for text in p_data['overview']:
                ProjectOverview.objects.create(project=project, text=text)

            for f_data in p_data['features']:
                ProjectFeature.objects.create(
                    project=project,
                    icon=f_data['icon'],
                    title=f_data['title'],
                    description=f_data['description']
                )
            
            self.stdout.write(self.style.SUCCESS(f'Successfully seeded project "{project.title}"'))
