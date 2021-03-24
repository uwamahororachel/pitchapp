import unittest
from app.models import Pitch, User, Comment
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'rachelnet',password = 'rachelnet', email = 'uwamahororachel@gmail.com')
        self.new_pitch = Pitch(id=1,title='Test',description='This is just a test pitch',comments="great",category="interview")

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.title,'Test')
        self.assertEquals(self.new_pitch.description,'This is just a test Pitch')
        self.assertEquals(self.new_pitch.category,"interview")
      

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)