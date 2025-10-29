favorite_cars = [
    {
        "make": "Telsa",
        "model": "Model S",
        "year": 2022,
        "price": 79999.99,
        "features": ["Autopilot", "Electric", "All-Wheel Drive"],
        "is_electric": True,
        "owner": None
    },
    {
        "make": "Porshe",
        "model": "911 Carrera",
        "year": 2023,
        "price": 104999.99,
        "features": ["Autopilot", "Electric", "All-Wheel Drive"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Audi",
        "model": "R8",
        "year": 2023,
        "price": 144195.00,
        "features": ["All-Wheel Drive", "v10 Engine", "Convertible"],
        "is_electric": False,
        "owner": None
    }
]
# favorite_cars[0] = None
for car in favorite_cars:
    try:   
        if car['make'] == 'Telsa':
            print(f"The first item is a {car['model']}")
            print(car['make']+ " " + car['model'])
            break
        else:
            continue
    except TypeError as e:
        print("Encountered a TypeError")
        print(f"Error: {e}")
    else:
        print("No Exceptions were encountered")
    finally:
        print("This code will always run")