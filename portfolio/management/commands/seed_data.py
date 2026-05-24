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
                    "آکاسمارت یک نرم‌افزار دسکتاپ برای مدیریت آموزشگاه موسیقی است که با پایتون پایساید۶ و اسکیو لایت توسعه داده شده است.",
                    "این پروژه مدیریت هنرجویان، کلاس‌ها، حضور و غیاب و گزارش‌های مالی را در یک محیط ساده و قابل استفاده متمرکز می‌کند.",
                    "منطق برنامه از رابط کاربری جدا شده و بخش‌های اصلی به‌صورت ماژولار پیاده‌سازی شده‌اند تا نگه‌داری و توسعه‌ی آینده ساده‌تر باشد.",
                ],
                "features": [
                    {
                        "icon": "bi bi-mortarboard",
                        "title": "Student Management",
                        "description": "ثبت هنرجو، اطلاعات تکمیلی، سوابق مالی و وضعیت ترم‌ها",
                    },
                    {
                        "icon": "bi bi-person-badge",
                        "title": "Teacher & Class Management",
                        "description": "تعریف اساتید، کلاس‌ها، زمان‌بندی و جلوگیری از تداخل جلسات",
                    },
                    {
                        "icon": "bi bi-calendar-check",
                        "title": "Attendance System",
                        "description": "ثبت حضور و غیاب به‌تفکیک جلسه و ترم",
                    },
                    {
                        "icon": "bi bi-cash-coin",
                        "title": "Financial Reports",
                        "description": "گزارش‌های لحظه‌ای از شهریه‌ها، پرداخت‌ها و بدهی‌ها",
                    },
                    {
                        "icon": "bi bi-chat-dots",
                        "title": "Automatic SMS Reminder",
                        "description": "ارسال پیامک هنگام نزدیک شدن به پایان ترم هنرجو",
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
                    "یک ربات تلگرام برای دریافت اخبار شخصی‌سازی‌شده است که با پایتون و نیوز ای پی آی توسعه داده شده است.",
                    "کاربر می‌تواند موضوعات، زبان محتوا و منابع خبری دلخواه خود را انتخاب کند تا اخبار مرتبط‌تری دریافت کند.",
                    "ترجیحات کاربران در پایگاه داده ذخیره می‌شود و ساختار پروژه برای تغییرات آینده آماده شده است.",
                ],
                "features": [
                    {
                        "icon": "bi bi-robot",
                        "title": "Smart Personalized News",
                        "description": "ربات تلگرام هوشمند برای دریافت اخبار شخصی‌سازی‌شده براساس علایق کاربر.",
                    },
                    {
                        "icon": "bi bi-list-check",
                        "title": "Topic & Source Control",
                        "description": "انتخاب و مدیریت موضوعات خبری و منابع معتبر توسط خود کاربر.",
                    },
                    {
                        "icon": "bi bi-ui-checks-grid",
                        "title": "Interactive Telegram UI",
                        "description": "رابط کاربری تعاملی با دکمه‌های دو مرحله‌ای (Inline Keyboard) برای تجربه بهتر کاربر.",
                    },
                    {
                        "icon": "bi bi-translate",
                        "title": "Multi-language Support",
                        "description": "پشتیبانی کامل از زبان فارسی و انگلیسی با ذخیره و حفظ ترجیحات زبانی کاربر.",
                    },
                    {
                        "icon": "bi bi-database-gear",
                        "title": "Robust Data Layer",
                        "description": "مدیریت داده‌ها با SQLAlchemy ORM و مهاجرت دیتابیس با Alembic برای توسعه‌پذیری و پایداری.",
                    },
                    {
                        "icon": "bi bi-person-gear",
                        "title": "User Preference Management",
                        "description": "سیستم ذخیره و به‌روزرسانی ترجیحات کاربران برای ارسال محتوای همیشه مرتبط.",
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
                    "سایت رسمی آکادمی موسیقی آرامش با هدف مدیریت هنرجویان، نمایش دوره‌های آموزشی و برگزاری کلاس‌ها طراحی شده است.",
                    "این پروژه از فریمورک جنگو و تقویم جلالی برای بومی‌سازی تاریخ‌ها استفاده می‌کند.",
                    "بخش تماس با ما برای ثبت‌نام و دریافت مشاوره‌های اولیه طراحی شده است.",
                ],
                "features": [
                    {
                        "icon": "bi bi-person-video3",
                        "title": "Teacher Directory",
                        "description": "پروفایل اختصاصی برای اساتید به همراه سوابق هنری و آموزشی.",
                    },
                    {
                        "icon": "bi bi-images",
                        "title": "Academy Gallery",
                        "description": "نمایش تصاویر و فعالیت‌های هنری آکادمی.",
                    },
                    {
                        "icon": "bi bi-calendar-event",
                        "title": "Class Schedules",
                        "description": "سیستم نمایش و مدیریت جلسات آموزشی با پشتیبانی از تقویم شمسی.",
                    },
                    {
                        "icon": "bi bi-envelope-check",
                        "title": "Inquiry Management",
                        "description": "فرم تماس یکپارچه برای دریافت درخواست‌های هنرجویان جدید.",
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
