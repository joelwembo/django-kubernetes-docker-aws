from enum import Enum, auto

class OrganizationRole(Enum):
    CEO = auto()
    PRESIDENT = auto()
    MANAGER = auto()
    STAFF = auto()

class OrgRoleRange(Enum):
    CEO, PRESIDENT, MANAGER, STAFF = range(4)

def main():
    my_role = OrganizationRole.MANAGER
    print(my_role)

if __name__ == "__main__":
    main()