import os
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage

from flask import Flask, abort, flash, render_template, redirect, url_for
from dotenv import load_dotenv

from forms import ContactForm

load_dotenv()  # loads variables from .env into os.environ

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-change-me")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = int(os.environ.get("STATIC_CACHE_MAX_AGE", "31536000"))

try:
    from flask_compress import Compress
    Compress(app)
except Exception:
    # Keep app booting even if compression package is not installed yet.
    pass


@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}


def send_contact_email(*, sender_name: str, sender_email: str, subject: str, message: str) -> None:
    """
    Send contact form submission via Gmail SMTP to your chosen inbox.
    """
    
    gmail_address = os.environ.get("GMAIL_ADDRESS")
    gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")
    receiver = os.environ.get("CONTACT_RECEIVER_EMAIL")
    if not gmail_address or not gmail_app_password or not receiver:
        raise RuntimeError(
            "Missing email config. Set GMAIL_ADDRESS, GMAIL_APP_PASSWORD, CONTACT_RECEIVER_EMAIL."
        )

    smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))

    email_msg = EmailMessage()
    email_msg["From"] = gmail_address
    email_msg["To"] = receiver
    email_msg["Subject"] = f"[Portfolio Contact] {subject}"
    # Replying will go to the visitor, not your Gmail account.
    email_msg["Reply-To"] = sender_email
    email_msg.set_content(
        "\n".join(
            [
                "New message from portfolio contact form:",
                "",
                f"Name: {sender_name}",
                f"Email: {sender_email}",
                f"Subject: {subject}",
                "",
                "Message:",
                message,
            ]
        )
    )

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(gmail_address, gmail_app_password)
        server.send_message(email_msg)

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

]


@app.route("/")
def index():
    form = ContactForm()
    return render_template("index.html", projects=projects, form=form)


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
    form = ContactForm()
    if not form.validate_on_submit():
        # Show validation errors back on the home page
        return render_template("index.html", projects=projects, form=form), 400

    try:
        send_contact_email(
            sender_name=form.name.data,
            sender_email=form.email.data,
            subject=form.subject.data,
            message=form.message.data,
        )
    except Exception as e:
        # Keep details out of the UI, but log them for you.
        print("CONTACT_EMAIL_SEND_FAILED", repr(e))
        flash("Sorry—your message could not be sent right now. Please try again later.", "error")
        return redirect(url_for("index", _anchor="contact"))

    flash("Your message has been sent. Thank you!", "success")
    return redirect(url_for("index", _anchor="contact"))


if __name__ == "__main__":
    app.run(debug=True)
