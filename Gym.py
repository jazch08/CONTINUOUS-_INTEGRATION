class GymMembership:
    def __init__(self):
        self.membership_plans = {"Basic": 50, "Premium": 100, "Family": 150}
        self.additional_features = {"Personal Training": 30, "Group Classes": 20}
        self.premium_features = {"Exclusive Facilities": 50, "Specialized Programs": 50}
        self.selected_plan = None
        self.selected_features = []
        self.group_members = 1

    def display_membership_plans(self):
        print("Planes de Membresía:")
        for plan, cost in self.membership_plans.items():
            print(f"{plan}: ${cost}")

    def select_membership_plan(self):
        plan = input("Seleccione un plan de membresía: ")
        if plan in self.membership_plans:
            self.selected_plan = plan
        else:
            print("Plan no disponible. Por favor, seleccione de nuevo.")
            self.select_membership_plan()

    def display_additional_features(self):
        print("Características Adicionales:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")
        for feature, cost in self.premium_features.items():
            print(f"{feature}: ${cost} (Premium)")

    def customize_membership(self):
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
        print(
            "¡Notificación: Se aplicará un descuento del 10% en el costo total de la membresía para inscripciones grupales!"
        )
        self.group_members = int(
            input(
                "¿Cuántos miembros se inscribirán juntos? (Ingrese un número entero): "
            )
        )

    def apply_group_discount(self, total_cost):
        if self.group_members > 1:
            print("Aplicando descuento del 10% para membresías grupales.")
            return total_cost * 0.9
        return total_cost

    def apply_special_offer_discount(self, total_cost):
        if total_cost > 400:
            print("Aplicando descuento de $50.")
            return total_cost - 50
        elif total_cost > 200:
            print("Aplicando descuento de $20.")
            return total_cost - 20
        return total_cost

    def apply_premium_surcharge(self, total_cost):
        if (
            any(feature in self.premium_features for feature in self.selected_features)
            and self.selected_plan != "Premium"
        ):
            print("Aplicando recargo del 15% para características premium.")
            total_cost = total_cost * 1.15
            return round(total_cost)
        return total_cost

    def calculate_cost(self):
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
        self.display_membership_plans()
        self.select_membership_plan()
        self.customize_membership()
        self.ask_group_membership()
        total_cost = self.confirm_membership()
        print(f"Costo final: ${total_cost}")


if __name__ == "__main__":
    gym_membership = GymMembership()
    gym_membership.run()
