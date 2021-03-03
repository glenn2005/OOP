'''
################################################
#  Program: loops_with_oops                    #
#  Author: Glenn Ivory                         #
#  Date: 3/3/2021                              #
#  Description: Program to be used by the      #
#               POD Leaders in instructing     #
#               the POD members about Object   #
#               Oriented Programming concepts  #
#  The Hidden Genius Project                   #
#  OAK8 Cohort                                 #
################################################
'''

class Pod:
    # Class variable
    member = {}
    
    # Class Constructor method is called when an Object is instantiated
    def __init__(self, leader, cell):
        Pod.member[leader] = cell
        
    # Method to add member and number to member dictionary
    def add_member(self, name , cell):
        Pod.member[name] = cell
        
    # Class method to print the pod_leader and cell numbers
    def display_members(self):
        for Pod.member, number in Pod.member.items():
            print(Pod.member, number)
            
#  Prompt for the Pod Leader name and number
leader = input("Who is the leader? : ")
cell = input("What is the leaders cell number? : ")

# Initialize the Pod Dictionary with the leader’s name and number
pod = Pod(leader,cell)
pod.add_member(leader,cell)

amount = int(input("How many members would you like to add? : "))

for i in range(amount):
    members = input(" Who is the member? :")
    cell = int(input("What is their phone number?:"))
    pod.add_member(member, cell)
    
pod.display_members()













