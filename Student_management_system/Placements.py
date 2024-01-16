# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:06:08 2023

@author: students
"""
companies=['mi','csk','rcb','kxip','dc','gt','kkr']
def Display_companies():
    print(companies)
    return companies
domain_name=['east','west','north','south']
east=[]
west=[]
north=[]
south=[]
def companiesfromdomain(domain_name):
    for i in domain_name:
        if domain_name=='east':
            east.append(companies[6])
            print(f"companies from east are: {east}")
            return east
        elif domain_name=='west':
            west.append(companies[0])
            west.append(companies[5])
            print(f"companies from the west are: {west} ")
            return west
        elif domain_name=='north':
            north.append(companies[3])
            north.append(companies[4])
            print(f"companies from the north are: {north}")
            return north
        else:
            south.append(companies[1])
            south.append(companies[2])
            print(f"companies from the south are: {south}")
            return south
if __name__=='__main__':
    companiesfromdomain('east')
    companiesfromdomain('west')
    companiesfromdomain('north')
    companiesfromdomain('south')
        
    