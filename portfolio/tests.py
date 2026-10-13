import os
from io import BytesIO
from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import Resume, Project, ProjectOverview, ProjectFeature


class ResumeModelTest(TestCase):
    def setUp(self):
        self.pdf_content = b'%PDF-1.4\n%Test PDF content\n%%EOF'
        self.pdf_file = SimpleUploadedFile(
            "test_resume.pdf",
            self.pdf_content,
            content_type="application/pdf"
        )

    def test_resume_creation(self):
        resume = Resume.objects.create(
            title="Test Resume",
            file=self.pdf_file,
            is_active=True
        )
        self.assertEqual(resume.title, "Test Resume")
        self.assertTrue(resume.is_active)
        self.assertEqual(resume.file_extension, "pdf")

    def test_resume_str_representation(self):
        resume = Resume.objects.create(
            title="Test Resume",
            file=self.pdf_file,
            is_active=True
        )
        self.assertIn("Active", str(resume))

        resume.is_active = False
        resume.save()
        self.assertIn("Inactive", str(resume))

    def test_only_one_active_resume(self):
        resume1 = Resume.objects.create(
            title="Resume 1",
            file=self.pdf_file,
            is_active=True
        )
        resume2 = Resume.objects.create(
            title="Resume 2",
            file=self.pdf_file,
            is_active=True
        )
        resume1.refresh_from_db()
        resume2.refresh_from_db()
        self.assertFalse(resume1.is_active)
        self.assertTrue(resume2.is_active)

    def test_file_size_property(self):
        resume = Resume.objects.create(
            title="Test Resume",
            file=self.pdf_file,
            is_active=True
        )
        self.assertEqual(resume.file_size, len(self.pdf_content))

    def test_file_extension_property(self):
        resume = Resume.objects.create(
            title="Test Resume",
            file=self.pdf_file,
            is_active=True
        )
        self.assertEqual(resume.file_extension, "pdf")


class ResumeViewTest(TestCase):
    def setUp(self):
        self.pdf_content = b'%PDF-1.4\n%Test PDF content\n%%EOF'
        self.pdf_file = SimpleUploadedFile(
            "test_resume.pdf",
            self.pdf_content,
            content_type="application/pdf"
        )

    def test_index_view_with_active_resume(self):
        Resume.objects.create(
            title="Active Resume",
            file=self.pdf_file,
            is_active=True
        )
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "دانلود رزومه")
        self.assertContains(response, "resumes/test_resume")

    def test_index_view_without_active_resume(self):
        Resume.objects.create(
            title="Inactive Resume",
            file=self.pdf_file,
            is_active=False
        )
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "دانلود رزومه")
        self.assertContains(response, "my_resume_6")

    def test_index_view_no_resume(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "دانلود رزومه")
        self.assertContains(response, "my_resume_6")


class ResumeAdminTest(TestCase):
    def setUp(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='password'
        )
        self.client.login(username='admin', password='password')
        self.pdf_content = b'%PDF-1.4\n%Test PDF content\n%%EOF'
        self.pdf_file = SimpleUploadedFile(
            "test_resume.pdf",
            self.pdf_content,
            content_type="application/pdf"
        )

    def test_resume_admin_list_display(self):
        Resume.objects.create(
            title="Test Resume",
            file=self.pdf_file,
            is_active=True
        )
        response = self.client.get(reverse('admin:portfolio_resume_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Resume")
        self.assertContains(response, "Active")

    def test_resume_admin_add_valid_pdf(self):
        response = self.client.post(reverse('admin:portfolio_resume_add'), {
            'title': 'New Resume',
            'file': self.pdf_file,
            'is_active': True,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Resume.objects.filter(title="New Resume").exists())

    def test_resume_admin_rejects_non_pdf(self):
        txt_file = SimpleUploadedFile(
            "test.txt",
            b"not a pdf",
            content_type="text/plain"
        )
        response = self.client.post(reverse('admin:portfolio_resume_add'), {
            'title': 'Invalid Resume',
            'file': txt_file,
            'is_active': True,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Resume.objects.filter(title="Invalid Resume").exists())
        self.assertContains(response, "Only PDF files are allowed")

    def test_resume_admin_rejects_large_file(self):
        large_content = b'x' * (6 * 1024 * 1024)
        large_file = SimpleUploadedFile(
            "large.pdf",
            large_content,
            content_type="application/pdf"
        )
        response = self.client.post(reverse('admin:portfolio_resume_add'), {
            'title': 'Large Resume',
            'file': large_file,
            'is_active': True,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Resume.objects.filter(title="Large Resume").exists())
        self.assertContains(response, "File size must be less than 5MB")