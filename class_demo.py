import datetime

class Group:

    # Private variables:
    _number_of_groups = 0

    def __init__(self, name_of_the_group) -> None:
        self.members = []
        Group._number_of_groups += 1
        self.name_of_group = name_of_the_group
        self.date_of_creation = datetime.datetime.today().date()
    
    def __del__(self) -> None:
        Group._number_of_groups -= 1

    def __str__(self) -> str:
        separator_line = "\n______________________________________________"
        headline       = "\n----------------DETAILS ON {}-----------------".format(self.name_of_group)
        group_name_str = "\nName of Group: {}".format(self.name_of_group)
        created_on_str = "\nCreated On: {}".format(self.date_of_creation)
        members_heading = "\nMembers:\n"
        members_str = ""
        for i in self.members:
            members_str = members_str + "\t" + i + "\n"
        
        return (separator_line + headline + group_name_str + created_on_str + members_heading + members_str)


    def AddNewMember(self, name):
        self.members.append(name)
        print(name, " is added to ", self.name_of_group)
    
    def RemoveMember(self, name):
        self.members.remove(name)
        print(name, " is removed from ", self.name_of_group)
    
    def getnumberOfGroups(self) -> int:
        return self._number_of_groups


labours_group = Group("Labour's Group")
labours_group.AddNewMember("Rajiv")
labours_group.AddNewMember("AliBhai")
labours_group.AddNewMember("Shamir")
labours_group.AddNewMember("Surya")
labours_group.AddNewMember("Dilip")
labours_group.AddNewMember("MollaBhai")

friends_group = Group("College Friend's Group")
friends_group.AddNewMember("Subhojit")
friends_group.AddNewMember("Sourindra")
friends_group.AddNewMember("Debasish")
friends_group.AddNewMember("Suvam")
friends_group.AddNewMember("Sankar")
friends_group.AddNewMember("Payel")
friends_group.AddNewMember("Kartik")
friends_group.AddNewMember("OmPrakash")
friends_group.AddNewMember("Ankit")

family_group = Group("Sweet Cousins & Jijus Group")
family_group.AddNewMember("Borda")
family_group.AddNewMember("Bordee")
family_group.AddNewMember("MejDa")
family_group.AddNewMember("MejDee")
family_group.AddNewMember("SejDa")
family_group.AddNewMember("ChorDee")
family_group.AddNewMember("ChorDa")
family_group.AddNewMember("Disha")
family_group.AddNewMember("Putul")
family_group.AddNewMember("Sunny")


print(labours_group)
print(friends_group)
print(family_group)
