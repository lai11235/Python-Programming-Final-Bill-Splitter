#
# Pseudocode
#
# class BillManager:
#     function __init__():
#         bill_id_counter = 0
#         bill_names = []
#         accounts = []
#         is_bill_available = []
#         member = list()
#         name_mapping = {}
#         name_counter = 0

#     function add_new_member(name):
#         member.append(name)
#         name_mapping[name] = name_counter
#         name_counter += 1

#     function get_people_number() -> int:
#         return len(member)

#     function get_bill(bill_id: int) -> list:
#         return accounts[bill_id]

#     function add_bill(bill_name: str, cash_list: list) -> int:
#         bill_names.append(bill_name)
#         is_bill_available.append(True)
#         accounts.append(cash_list)
#         return len(accounts) - 1

#     function delete_bill(bill_id: int) -> bool:
#         if 0 <= bill_id < len(is_bill_available):
#             is_bill_available[bill_id] = False
#             return True
#         return False

#     function person_renew():
#         for account in accounts:
#             account.append(-1)

#     function bill_renew(bill_id: int, bill_new_name: str, cash_list: list) -> bool:
#         if 0 <= bill_id < len(accounts):
#             accounts[bill_id] = cash_list
#             bill_names[bill_id] = bill_new_name
#             return True
#         return False

#     function clear_calculations():
#         // Clear calculation-related data
#         // (Not detailed to keep it simple)

#     function bill_calc():
#         // Perform bill calculations
#         // (Not detailed to keep it simple)

class BillManager:
    def __init__(self):
        self.bill_id_counter = 0
        self.bill_names = []
        self.accounts = []
        self.is_bill_available = []
        self.paying_flow = []
        self.total_cost = []

        self.member = list()
        self.name_mapping = {}
        self.name_counter = 0

    def add_new_member(self, name):
        self.member.append(name)
        self.name_mapping[name] = self.name_counter
        self.name_counter += 1

    def get_people_number(self) -> int:
        return len(self.member)

    def get_bill(self, bill_id: int) -> list:
        return self.accounts[bill_id]

    def add_bill(self, bill_name: str, cash_list: list) -> int:
        self.bill_names.append(bill_name)
        self.is_bill_available.append(True)
        self.accounts.append(cash_list)
        self.bill_id_counter += 1

        return self.bill_id_counter - 1

    def delete_bill(self, bill_id: int) -> bool:
        if bill_id < 0 or bill_id >= self.bill_id_counter:
            return False

        self.is_bill_available[bill_id] = False
        return True

    def person_renew(self):
        for account in self.accounts:
            account.append(-1)

    def bill_renew(self, bill_id: int, bill_new_name: str, cash_list: list) -> bool:
        if bill_id < 0 or bill_id >= self.bill_id_counter:
            return False

        self.accounts[bill_id] = cash_list
        self.bill_names[bill_id] = bill_new_name
        return True

    def clear_clac(self):
        self.paying_flow = []
        self.total_cost = []

    def bill_calc(self):
        name_len = self.get_people_number()

        self.paying_flow = [[i, 0] for i in range(name_len)]
        self.total_cost = [[i, 0] for i in range(name_len)]

        for i, account in enumerate(self.accounts):
            if not self.is_bill_available[i]:
                continue
            tx_money = 0
            man_pay = []
            man_gain = []

            for j, rec in enumerate(account):
                if rec == 0:
                    man_pay.append(j)
                elif rec == -1:
                    continue
                else:
                    man_gain.append(j)
                    self.total_cost[j][1] += rec
                    tx_money += rec

            total_paying_main = len(man_pay) + len(man_gain)
            avg_payment = tx_money // total_paying_main

            for join in man_pay:
                self.paying_flow[join][1] += (account[join] - avg_payment)

            remain_payment = tx_money - (avg_payment * total_paying_main)

            if len(man_pay) != 0:
                avg_remain_payment = remain_payment // len(man_pay)
            else:
                avg_remain_payment = remain_payment // name_len

            for join in man_gain:
                self.paying_flow[join][1] += (account[join] -
                                              avg_payment - avg_remain_payment)
                remain_payment -= avg_remain_payment

            self.paying_flow[man_gain[0]][1] -= remain_payment

        for i in range(len(self.total_cost)):
            self.total_cost[i][1] -= self.paying_flow[i][1]

        self.paying_flow = sorted(
            self.paying_flow, key=lambda x: x[1], reverse=True)
