class Flight:
    def __init__(self, flight_id: str, fromm : str, to : str, price : int):
        self.flight_id = flight_id
        self.fromm = fromm
        self.to = to
        self.price = price
    def search_by_from(self):
        pass
    def search_by_to(self):
        pass
    def search_by_from_to(self):
        pass
    def display(self):
        print("Flight ID: ", self.flight_id, "from: ", self.fromm, "to: ",self.to, "price: ", self.price)
def main():
    obj1 = Flight('AI61E90', 'BLR', 'BOM', 5600)
    obj2 = Flight('BR161F91', 'BOM', 'BBI', 6750)
    obj3 = Flight('AI161F99', 'BBI', 'BLR', 8210)
    obj4 = Flight('VS171E20', 'JLR', 'BBI', 5500)
    obj5 = Flight('AS171G30', 'HYD','JLR', 4400)
    obj6 = Flight('AI131F49 ', 'HYD ', 'BOM', 3499)
    print("Welcome to Air India Airlines!")
    print("What do you want to search for?")
    print("1) Flights for a particular city\n2) Flights from a particular city\n3)Flights between cities \n4)Exit")
    while True:
        choice = int(input())
        if choice == 1:
            print("[BLR: Bengaluru, BOM: Mumbai, BBI: Bhubaneswar, HYD: Hyderabad, JLR: Jabalpur]")
            to_city = input().upper()
            for obj in [obj1, obj2, obj3, obj4, obj5, obj6]:
                if obj.to == to_city:
                    obj.display()
            print("\n\n\n\n")
            
            
        elif choice == 2:
                print("[BLR: Bengaluru, BOM: Mumbai, BBI: Bhubaneswar, HYD: Hyderabad, JLR: Jabalpur]")
                from_city = input().upper()
                for obj in [obj1, obj2, obj3, obj4, obj5, obj6]:
                    if obj.fromm == from_city:
                        obj.display()
                    # else:
                    #     print("Flight not available")
                print("\n\n\n\n")
        elif choice == 3:
                print("[BLR: Bengaluru, BOM: Mumbai, BBI: Bhubaneswar, HYD: Hyderabad, JLR: Jabalpur]")
                
                from_city = input().upper()
                to_city = input().upper()
                
                for obj in [obj1, obj2, obj3, obj4, obj5, obj6]:
                    if obj.fromm == from_city and obj.to == to_city:
                        obj.display()
                    # else:
                    #     print("Flight not available")
                print("\n\n\n\n")
                
        elif choice == 4:
                break
        else:
            print("Enter the correct number.")

if __name__ == "__main__":
    main()
        