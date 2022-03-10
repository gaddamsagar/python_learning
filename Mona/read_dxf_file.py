import ezdxf

read_dxf=ezdxf.readfile('MSB_Sample_8.dxf')  #using ezdxf library for read dxf format file
msp=read_dxf.modelspace()          #this is used for showwing block of model space
for e in msp:
    print(e)
    if e.dxftype() == 'LINE':
        print(e)
# group=msp.groupby(dxfattrib='layer') #this is used for group of layers and entities are collecting
# dict1={}                              # create empty dict
# for layer,entities in group.items():  # taking layers and entities from using for loop
#     if('_ROOM' in layer): # this is showwing only Room layer
#         count=0           # i am using count for counting purpose
#         for entity in entities: # this for loop is used for only collecting entities
#             print(entity)
#             if entity.dxftype()=='POLYLINE': # this condition is used for only LWPOLYLINE entities taking
#                 lst=entity.get_points()

            # data = ezdxf.readfile('MSB_Sample_8.dxf')
# data1 = data.modelspace().groupby(dxfattrib='layer')
# for l,e in data1.items():
#     if '_ROOM' in l:
#         print(l,e)
#         for x in e:
#             if x.dxftype()=='POLYLINE':
#                 print(x.dxftype())
#                 dir(x)
#                 # print(x.get_points())

# for d in data.layers:
#     print(d.dxf.name)