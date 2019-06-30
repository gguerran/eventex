from django.test import TestCase

from eventex.core.models import Talk, CourseOld, Course

from eventex.core.manager import PeriodManager


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many Speakers and vice-versa"""
        self.talk.speakers.create(
            name='José Renato',
            slug='jose-renato',
            website='http://joserenato.net'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_speakers_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_description_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_start_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual("Título da Palestra", str(self.talk))


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='MorningTalk', start='11:59')
        Talk.objects.create(title='AfternoonTalk', start='12:00')

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['MorningTalk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        qs = Talk.objects.at_afternoon()
        expected = ['AfternoonTalk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)


class CourseOldModelTest(TestCase):
    def setUp(self):
        self.course = CourseOld.objects.create(
            title='Título do curso',
            start='09:00',
            description='Descrição do curso.',
            slots=20
        )

    def test_create(self):
        self.assertTrue(CourseOld.objects.exists())

    def test_speaker(self):
        """Course has many speakers and vice-versa"""
        self.course.speakers.create(
            name='José Renato',
            slug='jose-renato',
            website='http://joserenato.net'
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual(str(self.course), 'Título do curso')

    def test_manager(self):
        self.assertIsInstance(CourseOld.objects, PeriodManager)


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Título do curso',
            start='09:00',
            description='Descrição do curso.',
            slots=20
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_speaker(self):
        """Course has many speakers and vice-versa"""
        self.course.speakers.create(
            name='José Renato',
            slug='jose-renato',
            website='http://joserenato.net'
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual(str(self.course), 'Título do curso')

    def test_manager(self):
        self.assertIsInstance(CourseOld.objects, PeriodManager)