class GymMembership:
    """
    Clase para representar una membresía de gimnasio.

    Atributos:
        membership_plans (dict): Un diccionario de planes de membresía y sus costos.
        additional_features (dict): Un diccionario de características adicionales y sus costos.
        premium_features (dict): Un diccionario de características premium y sus costos.
        selected_plan (str): El plan de membresía actualmente seleccionado.
        selected_features (list): La lista de características adicionales seleccionadas por usuario
        group_members (int): El número de miembros del grupo para el cálculo del descuento grupal.
    """

    def __init__(self):
        """
        Inicializa el objeto con valores predeterminados para los planes de membresía,
        características adicionales, características premium,
        plan seleccionado, características seleccionadas y miembros del grupo.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.membership_plans = {"Basic": 50, "Premium": 100, "Family": 150}
        self.additional_features = {"Personal Training": 30, "Group Classes": 20}
        self.premium_features = {"Exclusive Facilities": 50, "Specialized Programs": 50}
        self.selected_plan = None
        self.selected_features = []
        self.group_members = 1

    def display_membership_plans(self):
        """
        Muestra los planes de membresía disponibles y sus costos.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        print("Planes de Membresía:")
        for plan, cost in self.membership_plans.items():
            print(f"{plan}: ${cost}")

    def select_membership_plan(self):
        """
        Solicita al usuario seleccionar un plan de membresía. Si el plan es válido,
        se establece como el plan seleccionado; sino se solicita al usuario seleccionar nuevamente.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        plan = input("Seleccione un plan de membresía: ")
        if plan in self.membership_plans:
            self.selected_plan = plan
        else:
            print("Plan no disponible. Por favor, seleccione de nuevo.")
            self.select_membership_plan()

    def display_additional_features(self):
        """
        Muestra las caracts. adicionales disponibles y sus costos, incluyendo caracts. premium.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        print("Características Adicionales:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")
        for feature, cost in self.premium_features.items():
            print(f"{feature}: ${cost} (Premium)")

    def customize_membership(self):
        """
        Solicita al usuario seleccionar caracts. adicionales para su membresía. El usuario puede
        continuar agregando características hasta que indique que ha terminado.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.display_additional_features()
        while True:
            feature = input(
                "Seleccione una característica adicional o 'done' para finalizar: "
            )
            if feature == "done":
                break
            if feature in self.additional_features or feature in self.premium_features:
                self.selected_features.append(feature)
            else:
                print("Característica no disponible. Por favor, seleccione de nuevo.")

    def ask_group_membership(self):
        """
        Solicita al usuario ingresar el número de miembros del grupo. Muestra una notificación
        sobre el descuento grupal.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        print(
            "¡Se aplicará un descuento del 10% del costo la membresía para inscripciones grupales!"
        )
        self.group_members = int(
            input(
                "¿Cuántos miembros se inscribirán juntos? (Ingrese un número entero): "
            )
        )

    def apply_group_discount(self, total_cost):
        """
        Aplica un descuento del 10% al costo total si hay más de un miembro del grupo.

        Parámetros:
            total_cost (float): El costo total antes de aplicar el descuento grupal.

        Retorna:
            float: El costo total después de aplicar el descuento grupal.
        """
        if self.group_members > 1:
            print("Aplicando descuento del 10% para membresías grupales.")
            return total_cost * 0.9
        return total_cost

    def apply_special_offer_discount(self, total_cost):
        """
        Aplica descuentos por ofertas especiales basados en el costo total.

        Parámetros:
            total_cost (float): El costo total antes de aplicar descuentos por ofertas especiales.

        Retorna:
            float: El costo total después de aplicar descuentos por ofertas especiales.
        """
        if total_cost > 400:
            print("Aplicando descuento de $50.")
            return total_cost - 50
        elif total_cost > 200:
            print("Aplicando descuento de $20.")
            return total_cost - 20
        return total_cost

    def apply_premium_surcharge(self, total_cost):
        """
        Recargo del 15% si se incluyen características premium en un plan de membresía no premium.

        Parámetros:
            total_cost (float): El costo total.

        Retorna:
            float: El costo total después de aplicar el recargo por características premium.
        """
        if (
            any(feature in self.premium_features for feature in self.selected_features)
            and self.selected_plan != "Premium"
        ):
            print("Aplicando recargo del 15% para características premium.")
            total_cost = total_cost * 1.15
            return round(total_cost)
        return total_cost

    def calculate_cost(self):
        """
        Calcula el costo total, incluyendo el costo base, características adicionales,
        características premium y aplicando descuentos y recargos relevantes.

        Parámetros:
            Ninguno

        Retorna:
            int: El costo final de la membresía como un entero.
        """
        base_cost = self.membership_plans[self.selected_plan]
        features_cost = sum(
            self.additional_features[feature]
            for feature in self.selected_features
            if feature in self.additional_features
        )
        premium_features_cost = sum(
            self.premium_features[feature]
            for feature in self.selected_features
            if feature in self.premium_features
        )

        total_cost = base_cost + features_cost + premium_features_cost
        print(f"Costo total*: ${total_cost}")
        total_cost = self.apply_premium_surcharge(total_cost)
        print(f"Costo final**: ${total_cost}")
        total_cost = self.apply_group_discount(total_cost)
        print(f"Costo final***: ${total_cost}")
        total_cost = self.apply_special_offer_discount(total_cost)
        print(f"Costo final****: ${total_cost}")

        return int(total_cost)

    def confirm_membership(self):
        """
        Confirma la selección de la membresía mostrando el plan seleccionado,
        características adicionales,y el costo final. Solicita al usuario confirmar
        o cancelar la membresía.

        Parámetros:
            Ninguno

        Retorna:
            int: El costo total si se confirma, o -1 si se cancela.
        """
        total_cost = self.calculate_cost()
        print(f"Membresía seleccionada: {self.selected_plan}")
        print(f"Características adicionales: {', '.join(self.selected_features)}")
        print(f"Costo total: ${total_cost}")
        confirm = input("¿Desea confirmar esta membresía? (si/no): ")
        if confirm.lower() == "si":
            print("Membresía confirmada.")
            return total_cost
        else:
            print("Membresía cancelada.")
            return -1

    def run(self):
        """
        Ejecuta el proceso de selección y personalización de membresía.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.display_membership_plans()
        self.select_membership_plan()
        self.customize_membership()
        self.ask_group_membership()
        total_cost = self.confirm_membership()
        print(f"Costo final: ${total_cost}")


if __name__ == "__main__":
    gym_membership = GymMembership()
    gym_membership.run()
