class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True

    for sub_group in group.get_groups():
        found_user = is_user_in_group(user, sub_group)
        if found_user:
            return True
    
    return False

def testcase1(id, expected):
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    print_testcase_state(id, parent, expected)

def testcase2(id, expected):
    parent = Group("parent")
    child = Group("child")
    child.add_user("child1")
    parent.add_group(child)
    print_testcase_state(id, parent, expected)

def testcase3(id, expected):
    home = Group("home")

    group_a = Group("group_a")
    group_a_user = Group("group_a_user")
    group_a.add_group(group_a_user)
    
    group_b = Group("group_b")
    group_b_user = Group("group_b_user")
    group_b.add_group(group_b_user)
    group_b.add_user("group_b_user")
    
    home.add_group(group_a)
    home.add_group(group_b)
    print_testcase_state(id, home, expected)


def testcase4(id, expected):
    home = Group("home")

    group_a = Group("group_a")
    group_a_user = Group("group_a_user")
    group_a.add_group(group_a_user)

    home.add_group(group_a)
    
    print_testcase_state(id, "None", expected)


def testcase5(id, expected):
    home = Group("home")

    group_a = Group("group_a")
    group_a_user = Group("group_a_user")
    group_a.add_group(group_a_user)

    home.add_group(group_a)
    
    print_testcase_state(id, None, expected)


def print_testcase_state(id, group, expected):
    if not isinstance(id, str):
        print(f"id needs to be str, it is {type(id)}")
        return

    if not isinstance(group, Group):
        print(f"group needs to be a class of {Group}, it is {type(group)}")
        return
        
    if is_user_in_group(id, group) == expected:
        print("Test passed")
    else:
        print("Test failed")


testcase1("sub_child_user", True)
testcase2("parent_user", False)
testcase3("group_b_user", True)
testcase4("group_a_user", False) # Exception error
testcase5("group_a_user", False) # Exception error
