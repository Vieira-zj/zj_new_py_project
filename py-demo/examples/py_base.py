# -- coding: utf-8 --
import dataclasses
import json
import os
import shutil
import tempfile
from contextlib import contextmanager
from typing import Final, List, Optional, TypedDict

# example: base


def test_const_var():
    main_mode: Final[str] = "main"
    print("mode:", main_mode)


def test_cal_division():
    float_res = 10 / 3
    print(f"result: {float_res:.2f}")

    int_res = 10 // 3  # 返回整数
    print("result:", int_res)


# example: typed dict


def test_class_with_typeddict():
    class Employee(TypedDict):
        name: str
        id: int
        department: str
        is_active: bool

    emp: Employee = {
        "name": "Bar",
        "id": 1024,
        "department": "Engineering",
        "is_active": True,
    }

    print(f"type: {type(emp)}")
    print(f"is dict: {isinstance(emp, dict)}")
    print()

    print(f"name: {emp['name']}")
    print(f"id: {emp['id']}")
    print(f"department: {emp['department']}")
    print(f"active: {'Yes' if emp.get('is_active') else 'No'}")


# example: dataclass
# parameters: slots=True, frozen=True, kw_only=True, order=True


@dataclasses.dataclass(slots=True, frozen=True, kw_only=True)
class Address:
    street: str
    city: str
    zip_code: str


@dataclasses.dataclass(slots=True, frozen=True, kw_only=True)
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


# example: context manager


@contextmanager
def temporary_workspace():
    ws_path = tempfile.mkdtemp()
    try:
        print(f"current workspace: {ws_path}")
        yield ws_path  # 将控制权交给 with block
    finally:
        shutil.rmtree(ws_path)
        print(f"clear workspace: {ws_path}")


def test_context_manager():
    with temporary_workspace() as ws:
        src = "/tmp/test/output.json"
        dst = os.path.join(ws, "output.bak")

        print(f"copy file: from {src} to {dst}")
        shutil.copy(src, dst)

        print("load json")
        with open(dst, mode="r", encoding="utf-8") as f:
            obj: dict = json.load(f)
            print(f"error code: {obj.get('error', 1)}")


if __name__ == "__main__":
    # test_const_var()
    # test_cal_division()

    # test_class_with_typeddict()
    # test_datacls_and_dict()

    test_context_manager()
