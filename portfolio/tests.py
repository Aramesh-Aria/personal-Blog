import os
import tempfile
from io import BytesIO, StringIO
from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import Resume, Project, ProjectOverview, ProjectFeature, SiteProfile


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
        self.assertContains(response, "resumes/ahmad_aramesh_resume.pdf")

    def test_index_view_no_resume(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "دانلود رزومه")
        self.assertContains(response, "resumes/ahmad_aramesh_resume.pdf")


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

def make_webp(name="thumb.webp"):
    from PIL import Image
    buf = BytesIO()
    Image.new("RGB", (4, 4), "red").save(buf, format="WEBP")
    return SimpleUploadedFile(name, buf.getvalue(), content_type="image/webp")


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class ProjectMediaUploadTest(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        self.admin = User.objects.create_superuser('admin', 'admin@example.com', 'pass')
        self.client.force_login(self.admin)
        self.project = Project.objects.create(
            title="Demo",
            category="Web",
            filter_class="filter-web",
            image="portfolio/old.webp",
            media_type="video",
            media_src="portfolio/old.mp4",
            date="2026",
        )

    def admin_form_data(self, **overrides):
        data = {
            'title': 'Demo', 'category': 'Web', 'filter_class': 'filter-web',
            'date': '2026', 'url': '', 'media_type': 'video',
            'overview_points-TOTAL_FORMS': '0', 'overview_points-INITIAL_FORMS': '0',
            'features-TOTAL_FORMS': '0', 'features-INITIAL_FORMS': '0',
        }
        data.update(overrides)
        return data

    def test_existing_path_renders_media_url(self):
        response = self.client.get(reverse('project_detail', args=[self.project.pk]))
        self.assertContains(response, 'src="/public/media/portfolio/old.mp4"')

    def test_admin_replaces_thumbnail_and_video(self):
        video = SimpleUploadedFile("new-demo.mp4", b"\x00\x00\x00\x18ftypmp42", content_type="video/mp4")
        url = reverse('admin:portfolio_project_change', args=[self.project.pk])
        response = self.client.post(url, self.admin_form_data(image=make_webp("new.webp"), media_src=video))
        self.assertEqual(response.status_code, 302)

        self.project.refresh_from_db()
        self.assertTrue(self.project.image.name.startswith('portfolio/new'))
        self.assertTrue(self.project.media_src.name.startswith('portfolio/new-demo'))

        response = self.client.get(reverse('project_detail', args=[self.project.pk]))
        self.assertContains(response, self.project.media_src.url)

    def test_admin_rejects_unsupported_media_extension(self):
        bad = SimpleUploadedFile("script.exe", b"MZ", content_type="application/octet-stream")
        url = reverse('admin:portfolio_project_change', args=[self.project.pk])
        response = self.client.post(url, self.admin_form_data(media_src=bad))
        self.assertEqual(response.status_code, 200)
        self.project.refresh_from_db()
        self.assertEqual(self.project.media_src.name, 'portfolio/old.mp4')


class ResumeMissingFileTest(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        self.client.force_login(User.objects.create_superuser('admin', 'admin@example.com', 'pass'))
        self.resume = Resume.objects.create(title="Gone", file="resumes/missing.pdf", is_active=True)

    def test_admin_pages_load_when_file_missing(self):
        response = self.client.get(reverse('admin:portfolio_resume_changelist'))
        self.assertContains(response, "File missing")
        response = self.client.get(reverse('admin:portfolio_resume_change', args=[self.resume.pk]))
        self.assertEqual(response.status_code, 200)

    def test_index_falls_back_when_active_resume_file_missing(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['active_resume'])
        self.assertNotContains(response, 'resumes/missing.pdf')


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class SiteProfileTest(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        self.client.force_login(User.objects.create_superuser('admin', 'admin@example.com', 'pass'))

    def test_index_uses_default_profile_images_without_site_profile(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'src="/public/media/profile/profile_5.webp"')
        self.assertContains(response, 'src="/public/media/profile/profile-4.webp"')

    def test_admin_upload_replaces_profile_images(self):
        response = self.client.post(reverse('admin:portfolio_siteprofile_add'), {
            'hero_image': make_webp("new-hero.webp"),
            'about_image': make_webp("new-about.webp"),
        })
        self.assertEqual(response.status_code, 302)

        profile = SiteProfile.load()
        response = self.client.get(reverse('index'))
        self.assertContains(response, f'src="{profile.hero_image.url}"')
        self.assertContains(response, f'src="{profile.about_image.url}"')
        self.assertTrue(profile.hero_image.name.startswith('profile/new-hero'))

    def test_only_one_site_profile(self):
        SiteProfile().save()
        SiteProfile().save()
        self.assertEqual(SiteProfile.objects.count(), 1)
        response = self.client.get(reverse('admin:portfolio_siteprofile_add'))
        self.assertEqual(response.status_code, 403)


class SeedMediaCommandTest(TestCase):
    def test_copies_missing_files_and_skips_existing(self):
        from django.core.management import call_command
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            out = StringIO()
            call_command('seed_media', stdout=out)
            self.assertTrue(os.path.exists(os.path.join(media_root, 'profile', 'profile_5.webp')))
            self.assertTrue(os.path.exists(os.path.join(media_root, 'portfolio', 'project-1-demo.mp4')))

            out = StringIO()
            call_command('seed_media', stdout=out)
            self.assertIn('0 copied', out.getvalue())


class ErrorPageTest(TestCase):
    def test_missing_page_uses_custom_404(self):
        response = self.client.get('/this-page-does-not-exist/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, 'Page Not Found', status_code=404)
        self.assertContains(response, f'href="{reverse("index")}"', status_code=404)
        self.assertContains(response, 'name="robots" content="noindex"', status_code=404)

    def test_server_error_renders_custom_500(self):
        from django.test import RequestFactory
        from django.views.defaults import server_error
        response = server_error(RequestFactory().get('/'))
        self.assertEqual(response.status_code, 500)
        self.assertIn(b'Something went wrong', response.content)
