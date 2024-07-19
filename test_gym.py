import unittest
from unittest.mock import patch

from gym import GymMembership


class TestGymMembership(unittest.TestCase):
    def setUp(self):
        self.gym_membership = GymMembership()

    def test_membership_plan_selection(self):
        # Simular la selección de un plan de membresía válido
        with patch('builtins.input', return_value='Basic'):
            self.gym_membership.select_membership_plan()
        self.assertEqual(self.gym_membership.selected_plan, 'Basic')

    def test_additional_features_selection(self):
        # Simular la selección de características adicionales
        with patch('builtins.input', side_effect=['Personal Training', 'Group Classes', 'done']):
            self.gym_membership.customize_membership()
        self.assertIn('Personal Training', self.gym_membership.selected_features)
        self.assertIn('Group Classes', self.gym_membership.selected_features)

    def test_invalid_additional_features_selection(self):
        # Simular la selección de características adicionales no válidas
        with patch('builtins.input', side_effect=['Invalid Feature', 'done']):
            with patch('builtins.print') as mocked_print:
                self.gym_membership.customize_membership()
        mocked_print.assert_called_with("Característica no disponible. Por favor, seleccione de nuevo.")

    def test_calculate_cost_basic(self):
        # Probar el cálculo del costo para el plan básico sin características adicionales
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = []
        self.assertEqual(self.gym_membership.calculate_cost(), 50)

    def test_calculate_cost_with_features(self):
        # Probar el cálculo del costo para el plan básico con características adicionales
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = ['Personal Training', 'Group Classes']
        self.assertEqual(self.gym_membership.calculate_cost(), 100)

    def test_group_discount(self):
        # Probar el descuento grupal
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.selected_features = []
        self.gym_membership.group_members = 2
        self.assertEqual(self.gym_membership.calculate_cost(), 135)  # 150 * 0.9

    def test_special_offer_discount(self):
        # Probar el descuento por ofertas especiales
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.selected_features = ['Personal Training', 'Group Classes']
        self.gym_membership.group_members = 2
        total_cost = self.gym_membership.calculate_cost()
        self.assertEqual(total_cost, 180)  # 150 + 30 + 20 - 20 (por superar los $200)

    def test_premium_surcharge(self):
        # Probar el recargo por características premium en un plan no premium
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = ['Exclusive Facilities']
        self.assertEqual(self.gym_membership.calculate_cost(), 115)  # 50 + 50 * 1.15

    def test_premium_surcharge_no_premium_features(self):
        # Verificar que no se aplique recargo si no hay características premium
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = ['Group Classes']
        self.assertEqual(self.gym_membership.calculate_cost(), 70)  # 50 + 20

    def test_user_confirmation(self):
        # Probar la confirmación de la membresía
        with patch('builtins.input', return_value='si'):
            self.gym_membership.selected_plan = 'Basic'
            self.gym_membership.selected_features = []
            self.assertEqual(self.gym_membership.confirm_membership(), 50)

    def test_user_cancellation(self):
        # Probar la cancelación de la membresía
        with patch('builtins.input', return_value='no'):
            self.gym_membership.selected_plan = 'Basic'
            self.gym_membership.selected_features = []
            self.assertEqual(self.gym_membership.confirm_membership(), -1)

if __name__ == "__main__":
    unittest.main()
