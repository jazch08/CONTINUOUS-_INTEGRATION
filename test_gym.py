"""
Módulo de pruebas para la clase `GymMembership`.

Este módulo contiene pruebas unitarias para la clase `GymMembership`,
que permite a los usuarios seleccionar
y personalizar una membresía de gimnasio.
Las pruebas cubren la selección de planes de membresía, características
adicionales, descuentos grupales y especiales, y el recargo por características premium.
También se verifica
la confirmación y cancelación de la membresía por parte del usuario.

El módulo utiliza `unittest` y `unittest.mock` para simular entradas del usuario
y verificar los resultados esperados.

Funciones:
    setUp:
        Inicializa una instancia de `GymMembership` antes de cada prueba.
    test_membership_plan_selection:
        Prueba la selección de un plan de membresía válido.
    test_additional_features_selection:
        Prueba la selección de características adicionales.
    test_invalid_additional_features_selection: 
        Prueba la selección de características adicionales no válidas.
    test_calculate_cost_basic:
        Prueba el cálculo del costo para el plan básico sin características adicionales.
    test_calculate_cost_with_features:
        Prueba el cálculo del costo para el plan básico con características adicionales.
    test_group_discount:
        Prueba el descuento grupal en el costo total.
    test_special_offer_discount:
        Prueba el descuento por ofertas especiales en el costo total.
    test_premium_surcharge:
        Prueba el recargo por características premium en un plan no premium.
    test_premium_surcharge_no_premium_features:
        Verifica que no se aplique recargo si no hay características premium.
    test_user_confirmation:
        Prueba la confirmación de la membresía por parte del usuario.
    test_user_cancellation:
        Prueba la cancelación de la membresía por parte del usuario.
"""

import unittest
from unittest.mock import patch

from gym import GymMembership


class TestGymMembership(unittest.TestCase):
    """
    Clase para probar la funcionalidad de la clase `GymMembership`.

    Métodos:
        setUp: Inicializa una instancia de `GymMembership` antes de cada prueba.
        test_membership_plan_selection: Prueba la selección de un plan de membresía válido.
        test_additional_features_selection: Prueba la selección de características adicionales.
        test_invalid_additional_features_selection:
            Prueba la selección de características adicionales no válidas.
        test_calculate_cost_basic:
            Prueba el cálculo del costo para el plan básico sin características adicionales.
        test_calculate_cost_with_features:
            Prueba el cálculo del costo para el plan básico con características adicionales.
        test_group_discount: Prueba el descuento grupal en el costo total.
        test_special_offer_discount: Prueba el descuento por ofertas especiales en el costo total.
        test_premium_surcharge: Prueba el recargo por características premium en un plan no premium.
        test_premium_surcharge_no_premium_features:
            Verifica que no se aplique recargo si no hay características premium.
        test_user_confirmation: Prueba la confirmación de la membresía por parte del usuario.
        test_user_cancellation: Prueba la cancelación de la membresía por parte del usuario.
    """

    def setUp(self):
        """
        Inicializa una instancia de `GymMembership` antes de cada prueba.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.gym_membership = GymMembership()

    def test_membership_plan_selection(self):
        """
        Prueba la selección de un plan de membresía válido.

        Simula la selección del plan 'Basic' y verifica que el plan seleccionado sea el correcto.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        with patch('builtins.input', return_value='Basic'):
            self.gym_membership.select_membership_plan()
        self.assertEqual(self.gym_membership.selected_plan, 'Basic')

    def test_additional_features_selection(self):
        """
        Prueba la selección de características adicionales.

        Simula la selección de 'Personal Training' y 'Group Classes',
        y verifica que las características
        seleccionadas se añadan correctamente.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        with patch('builtins.input', side_effect=['Personal Training', 'Group Classes', 'done']):
            self.gym_membership.customize_membership()
        self.assertIn('Personal Training', self.gym_membership.selected_features)
        self.assertIn('Group Classes', self.gym_membership.selected_features)

    def test_invalid_additional_features_selection(self):
        """
        Prueba la selección de características adicionales no válidas.

        Simula la selección de una característica no válida y
        verifica que se imprima el mensaje de error correcto.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        with patch('builtins.input', side_effect=['Invalid Feature', 'done']):
            with patch('builtins.print') as mocked_print:
                self.gym_membership.customize_membership()
        text = "Característica no disponible. Por favor, seleccione de nuevo."
        mocked_print.assert_called_with(text)

    def test_calculate_cost_basic(self):
        """
        Prueba el cálculo del costo para el plan básico sin características adicionales.

        Verifica que el costo total para el plan 'Basic'
        sin características adicionales sea el esperado.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = []
        self.assertEqual(self.gym_membership.calculate_cost(), 50)

    def test_calculate_cost_with_features(self):
        """
        Prueba el cálculo del costo para el plan básico con características adicionales.

        Verifica que el costo total para el plan 'Basic'
        con características adicionales sea el esperado.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = ['Personal Training', 'Group Classes']
        self.assertEqual(self.gym_membership.calculate_cost(), 100)

    def test_group_discount(self):
        """
        Prueba el descuento grupal en el costo total.

        Verifica que el descuento del 10% se aplique correctamente
        cuando hay más de un miembro del grupo.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.selected_features = []
        self.gym_membership.group_members = 2
        self.assertEqual(self.gym_membership.calculate_cost(), 135)  # 150 * 0.9

    def test_special_offer_discount(self):
        """
        Prueba el descuento por ofertas especiales en el costo total.

        Verifica que se aplique el descuento de $20 cuando el costo total
        supera los $200 y no supera los $400.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.gym_membership.selected_plan = 'Family'
        self.gym_membership.selected_features = ['Personal Training', 'Group Classes']
        self.gym_membership.group_members = 2
        total_cost = self.gym_membership.calculate_cost()
        self.assertEqual(total_cost, 180)  # 150 + 30 + 20 - 20 (por superar los $200)

    def test_premium_surcharge(self):
        """
        Prueba el recargo por características premium en un plan no premium.

        Verifica que se aplique el recargo del 15% cuando se seleccionan
        características premium en un plan no premium.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = ['Exclusive Facilities']
        self.assertEqual(self.gym_membership.calculate_cost(), 115)  # 50 + 50 * 1.15

    def test_premium_surcharge_no_premium_features(self):
        """
        Verifica que no se aplique recargo si no hay características premium.

        Verifica que el costo se calcule correctamente sin aplicar recargo
        si solo se seleccionan características no premium.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.gym_membership.selected_plan = 'Basic'
        self.gym_membership.selected_features = ['Group Classes']
        self.assertEqual(self.gym_membership.calculate_cost(), 70)  # 50 + 20

    def test_user_confirmation(self):
        """
        Prueba la confirmación de la membresía por parte del usuario.

        Simula la confirmación de la membresía y verifica que el costo final sea el correcto.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        with patch('builtins.input', return_value='si'):
            self.gym_membership.selected_plan = 'Basic'
            self.gym_membership.selected_features = []
            self.assertEqual(self.gym_membership.confirm_membership(), 50)

    def test_user_cancellation(self):
        """
        Prueba la cancelación de la membresía por parte del usuario.

        Simula la cancelación de la membresía y verifica que se retorne -1 como se espera.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        with patch('builtins.input', return_value='no'):
            self.gym_membership.selected_plan = 'Basic'
            self.gym_membership.selected_features = []
            self.assertEqual(self.gym_membership.confirm_membership(), -1)

if __name__ == "__main__":
    unittest.main()
