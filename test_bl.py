import unittest
from unittest.mock import patch
from bl import BL
from user import User

class TestBL(unittest.TestCase):
    def setUp(self):
        """Set up the BL instance and initial data for testing."""
        self.bl = BL()
        self.user = User(67130500001, "Test User")
        self.bl.register_user(self.user)

    def test_register_user_success(self):
        """Test successful user registration."""
        user = User(67130500002, "New User")
        result = self.bl.register_user(user)
        self.assertTrue(result)
        self.assertIn(67130500002, self.bl.get_user_data())

    def test_register_user_duplicate(self):
        """Test duplicate user registration."""
        user = User(67130500001, "Duplicate User")
        result = self.bl.register_user(user)
        self.assertFalse(result)

    def test_current_user(self):
        """Test setting and getting the current user."""
        self.bl.current_user(67130500001)
        self.assertEqual(self.bl.get_currentid(), 67130500001)

    def test_logout(self):
        """Test logging out the current user."""
        self.bl.current_user(67130500001)
        self.bl.logout()
        self.assertEqual(self.bl.get_currentid(), '')

    def test_all_course(self):
        """Test fetching all courses."""
        courses = self.bl.all_course()
        self.assertIn("Discrete", courses)
        self.assertIn("Ux-Ui", courses)
        self.assertIn("DesignThinking", courses)

    def test_enroll_success(self):
        """Test successful course enrollment."""
        self.bl.enroll("Discrete", 67130500001)
        self.assertIn(67130500001, self.bl.get_course_data()["Discrete"])

    def test_enroll_duplicate(self):
        """Test duplicate course enrollment."""
        self.bl.enroll("Discrete", 67130500001)
        with self.assertRaises(TypeError):
            self.bl.enroll("Discrete", 67130500001)

    def test_filter_mycourse(self):
        """Test filtering courses for a specific user."""
        self.bl.enroll("Discrete", 67130500001)
        self.bl.enroll("Ux-Ui", 67130500001)
        my_courses = self.bl.filter_mycourse(67130500001)
        self.assertListEqual(my_courses, ["Discrete", "Ux-Ui"])

    def test_checkid_valid(self):
        """Test validation of user ID."""
        self.bl.checkid(67130500001)  # ไม่ควรraiseนะ

    def test_checkid_invalid(self):
        """Test invalid user ID."""
        with self.assertRaises(ValueError):
            self.bl.checkid(67130599999)

    def test_checkname_valid(self):
        """Test valid username."""
        self.bl.checkname("ValidName")  # ไม่ควรraiseนะ

    def test_checkname_invalid(self):
        """Test invalid username."""
        with self.assertRaises(ValueError):
            self.bl.checkname("12345")

    def test_duplicate_enroll_course(self):
        """Test checking for duplicate enrollment."""
        self.bl.enroll("Discrete", 67130500001)
        result = self.bl.duplicate_enroll_corse("Discrete", 67130500001)
        self.assertTrue(result)

class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        """Test User class initialization."""
        user = User(67130500001, "Test User")
        self.assertEqual(user.get_user_id(), 67130500001)
        self.assertEqual(user.get_user_name(), "Test User")

    def test_user_repr(self):
        """Test User class string representation."""
        user = User(67130500001, "Test User")
        self.assertEqual(repr(user), "User(67130500001, Test User)")

if __name__ == "__main__":
    unittest.main()
