from flask import Flask, abort, render_template, request, redirect, url_for

app = Flask(__name__)

# نمونه داده‌های اولیه برای پروژه‌ها
projects = [
    {
        "id": 1,
        "title": "AcaSmart – Desktop Music Academy Management Software",
        "category": "Desktop Application | Python | PySide6 | SQLite",
        "filter_class": "filter-python",
        "image": "img/portfolio/project-1.webp",  # thumbnail in projects grid
        "media": {
            "type": "video",
            "src": "img/portfolio/project-1-demo.mp4",
            "poster": "img/portfolio/project-1.webp",
        },
        "info": {
            "date": "28/1/2026",
            "url": "https://github.com/Aramesh-Aria/AcaSmart-repo",
        },
        "overview": [
            "آکاسمارت یک نرم‌افزار دسکتاپ برای مدیریت یکپارچه آموزشگاه‌های موسیقی است که با پایتون و پایساید۶ توسعه داده شده",
            "این نرم‌افزار مشکلات رایج آموزشگاه‌ها مثل مدیریت هنرجویان، برنامه‌ریزی کلاس‌ها، ثبت حضور و غیاب و گزارش‌های مالی را در یک محیط گرافیکی ساده و سریع حل می‌کند.",
            "این نرم‌افزار با معماری شی‌گرا توسعه داده شده و منطق برنامه به‌صورت کامل از رابط کاربری جدا شده است."
            "ساختار پروژه ماژولار بوده و هر بخش اصلی (مانند هنرجو، استاد، کلاس و امور مالی) در قالب کلاس‌های مستقل پیاده‌سازی شده است."
            "مدیریت ارتباط با پایگاه داده به‌صورت متمرکز انجام می‌شود تا پایداری، توسعه‌پذیری و نگه‌داری نرم‌افزار در آینده آسان‌تر باشد."
        ],
        "features": [
            {
                "icon": "bi bi-mortarboard",
                "title": "🎓 Student Management",
                "description": "ثبت هنرجو، اطلاعات تکمیلی، سوابق مالی و وضعیت ترم‌ها",
            },
            {
                "icon": "bi bi-person-badge",
                "title": "👨‍🏫 Teacher & Class Management",
                "description": "تعریف اساتید، کلاس‌ها، زمان‌بندی و جلوگیری از تداخل جلسات",
            },
            {
                "icon": "bi bi-calendar-check",
                "title": "📅 Attendance System",
                "description": "ثبت حضور و غیاب به‌تفکیک جلسه و ترم",
            },
            {
                "icon": "bi bi-cash-coin",
                "title": "💰 Financial Reports",
                "description": "گزارش‌های لحظه‌ای از شهریه‌ها، پرداخت‌ها و بدهی‌ها",
            },
            {
                "icon": "bi bi-chat-dots",
                "title": "📩 Automatic SMS Reminder",
                "description": "ارسال پیامک هنگام نزدیک شدن به پایان ترم هنرجو",
            },
        ],
    },
    {
        "id": 2,
        "title": "NewsReaderBot – Personalized News Telegram Bot",
        "category": "Telegram Bot | Python | SQLAlchemy | Alembic",
        "filter_class": "filter-design",
        "image": "img/portfolio/project-2.webp",  # thumbnail in projects grid
        "media": {
            "type": "video",
            "src": "img/portfolio/project-2-demo.mp4",
            "poster": "img/portfolio/project-2.webp",
        },
        "info": {
            "date": "28/1/2026",
            "url": "https://github.com/Aramesh-Aria/NewsReaderBot",
        },
        "overview": [
            "یک ربات تلگرام هوشمند برای دریافت اخبار شخصی‌سازی‌شده است که با استفاده از NewsAPI توسعه داده شده.",
            "این ربات به کاربران اجازه می‌دهد موضوعات، زبان محتوا و منابع خبری دلخواه خود را انتخاب کرده و اخبار مرتبط را به‌صورت هدفمند و منظم دریافت کنند.",
        ],
        "features": [
            {
                "icon": "bi bi-robot",
                "title": "🤖 Smart Personalized News",
                "description": "ربات تلگرام هوشمند برای دریافت اخبار شخصی‌سازی‌شده براساس علایق کاربر.",
            },
            {
                "icon": "bi bi-list-check",
                "title": "📰 Topic & Source Control",
                "description": "انتخاب و مدیریت موضوعات خبری و منابع معتبر توسط خود کاربر.",
            },
            {
                "icon": "bi bi-ui-checks-grid",
                "title": "📲 Interactive Telegram UI",
                "description": "رابط کاربری تعاملی با دکمه‌های دو مرحله‌ای (Inline Keyboard) برای تجربه بهتر کاربر.",
            },
            {
                "icon": "bi bi-translate",
                "title": "🌐 Multi-language Support",
                "description": "پشتیبانی کامل از زبان فارسی و انگلیسی با ذخیره و حفظ ترجیحات زبانی کاربر.",
            },
            {
                "icon": "bi bi-database-gear",
                "title": "🗄️ Robust Data Layer",
                "description": "مدیریت داده‌ها با SQLAlchemy ORM و مهاجرت دیتابیس با Alembic برای توسعه‌پذیری و پایداری.",
            },
            {
                "icon": "bi bi-person-gear",
                "title": "⚙️ User Preference Management",
                "description": "سیستم ذخیره و به‌روزرسانی ترجیحات کاربران برای ارسال محتوای همیشه مرتبط.",
            },
        ],
    },

]


@app.route("/")
def index():
    return render_template("index.html", projects=projects)


@app.route("/project/<int:id>")
def project_detail(id):
    # پیدا کردن پروژه بر اساس id
    project = next((p for p in projects if p["id"] == id), None)
    if project is None:
        abort(404)
    return render_template("project-details.html", project=project)

@app.route("/service")
def service_details():
    return render_template("service-details.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # فعلاً فقط تست
    print(name, email, subject, message)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
