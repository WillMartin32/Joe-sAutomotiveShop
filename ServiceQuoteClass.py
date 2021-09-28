class ServiceQuote:

    def __init__(self,pcharge,lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge

    def set_parts_charges(self,pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self,lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        tax = .20(self.__parts_charges + self.__labor_charges)
        return tax

    def get_total_charges(self):
        total_charges = self.__parts_charges + self.__labor_charges