class ServiceQuote:

    def __init__(self,pcharge,lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge
 #       self.__tax_rate = tr
 #       self.__tax = tax

    def set_parts_charges(self,pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self,lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        tax = (int(self.__parts_charges) + int(self.__labor_charges))
        return tax

    def get_total_charges(self,tax):
        total_charges = int(self.__parts_charges) + int(self.__labor_charges) + int(tax)
        return total_charges