from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import About, SkillGroup, Skill, Project, Certification, Contact

class PortfolioTests(TestCase):
    def setUp(self):
        about = About.objects.create(content="Test About Me")
        contact = Contact.objects.create(
            phone="1234567890",
            email="test@example.com",
            linkedin="https://linkedin.com/test",
            github="https://github.com/test"
        )
        group = SkillGroup.objects.create(name="Frontend")
        Skill.objects.create(name="HTML", icon_url="https://example.com/html.png", group=group)
        Project.objects.create(title="Test Project", description="Test Description")
        Certification.objects.create(title="Test Certificate", provider="Test Provider")

    def test_home_view(self):
        response = self.client.get(reverse("home"))  # If your view is named `home`
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test About Me")
        self.assertContains(response, "Test Project")
        self.assertContains(response, "Test Certificate")
