import dataclasses
from typing import List, Optional

# demo: dataclass


@dataclasses.dataclass
class Address:
    street: str
    city: str
    zip_code: str


@dataclasses.dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None
    addresses: List[Address] = dataclasses.field(default_factory=list)
    is_active: bool = True


def test_datacls_and_dict():
    addr1 = Address(street="123 Main St", city="Anytown", zip_code="12345")
    addr2 = Address(street="456 Oak Ave", city="Otherville", zip_code="67890")

    person1 = Person(
        name="Foo",
        age=30,
        email="foo@example.com",
        addresses=[addr1, addr2],
    )
    person2 = Person(
        name="Bar",
        age=25,
        is_active=False,
    )

    # dataclass -> dict
    dict1 = dataclasses.asdict(person1)
    dict2 = dataclasses.asdict(person2)
    print("person1 dict:", dict1)
    print("person2 dict:", dict2)

    # dict to dataclass
    print()
    person3 = Person(**dict1)
    print("person3:", person3.name, person3.email, person3.addresses)
    person4 = Person(**dict2)
    print("person4:", person4.name, person4.age)


if __name__ == "__main__":
    test_datacls_and_dict()
