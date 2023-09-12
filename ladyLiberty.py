#where is lady liberty?
"""
benScott

1. Time : 1st priority [i.e. all I have]
2. Energy :  [have descent energy]
3. Persistence
4. Discipline  [discipline not that interesting , for me ]
5. Consistency

-------
me(Discipline) = 1
inveret index:
formula: maxN +1 = 5+1 = 6
then:        ( maxN +1 ) - x[i]



# mylist: 

1. Discipline [ I must stay Discipline, at all times , fix the problem on hand]
2. Consistency [I have to stay consistent , till the end of this wave]

3. Persistence* 

4.Energy [almost exhausted most of my energy]
5.Time  [ no time to waste]


to know the differnce
1. map ( importance):

1.1 Ascending
1.2 Descending

key: element-wise index difference, to find


"""

"""
#TODO
1. add set 
Hi I'm looking for lady liberty
where can I find lady liberty?

A: it's in New York!
B: New Jersey
C: you kidding, correct , it's in Staten Island []



1.
ladyLiberty  in          Hidden variable

1. NY                       []
2. NJ                       []
3. StatenIsland             []

ladyLiberty in NY ?
ladyLiberty in NJ ?

ladyLiberty in StatenIsland  ?


===============

possible ladyLiberty locations

define  a set
ladyLiberty = { NY, NJ, StatenIsland }

different forms of learning
================
pre-processed thinking

Rotation 

1.clockwise 
2. counterclockeise

---------
post-processed thinking:

1.clockwise 
2. counterclockeise

rotation

====

Earth is a planet we are on

1. important
2. unimportant knowledge

Earth is a planet 

s  v  o
earth is planet True 

planet is earth True 

ok
True
If relationship




"""

class human:

    def __init__(self, colorCar, colorShirt):
        self.colorCar = colorCar
        self.colorShirt = colorShirt

# make a human: with biased interests 
h1 = human(colorCar="black", colorShirt = "white" )
print( h1.colorCar )
print( h1.colorShirt ) 

exceptionMsg = "Exception: please re-check input, tneen retry"

#heat up
def favecolor(context):
    
    #check criterion
    if context == "car":
        return h1.colorCar
    elif  context == "shirt":
        return h1.colorShirt
    else:
        raise(Exception(exceptionMsg))
#request info about:
#carColor

# Context-driven (for s human h1:
# carColor = h1. colorCar ==  black
print ( favecolor( "car") + " car" ) 
#shirtColor = h1. colorShirt ==  white
print( favecolor("shirt") + " shirt" ) 


# there is only, and there can only be a half-truth

class halfTruth:
    """ a class to explain the half-truth"""
    def __init__(self, obj):
        self.obj =  obj
        self.level = 0

    def __init__(self, obj, level ):
        self.obj =  obj
        self.level = level

    
#truth has levels
        
#lvl0 
us = "us"
usa = "USA"

#lvl1 
halfTruth(us)
halfTruth(usa)

nj = "NJ"
ny = "NY"

statenIsland = "StatenIsland"

#locations = ["NY","NJ", "StatenIsland"]

#1. make: an empty set
ladyLiberty = set( )

print( "ladyLiberty = ", ladyLiberty )

# ladyLiberty
# ladyL

ladyLiberty.append("NY" )
for i in range(len(ladyLiberty)):

    print(ladyLiberty[i])

