# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:35:33 2017

@author: 赵晓胜
"""

from itertools import imap
global gdata_file
global label_vector
global group_map
path = "d:/data/graph.txt"
def getMaxId():

    return max(imap(lambda x:eval(x)[0],file(path,'r').xreadlines()))+1
def mapFunc(line):    ##voting

    node,edges = eval(line.strip())

##    edges = ((node,1),) + edges

    labels = label_vector[node]

    if labels:

        return [(edge+(labels,)) for edge in edges]

    else:

        return [(edge+({node:1},)) for edge in edges]

def mergeMap(a,b,weight):##merge b to a

    for k,v in b.iteritems():

        g = a.get(k)

        if g:

            a[k] = g + v * weight

        else:

            a[k] = v * weight

    return a



def reduceFunc(map_phrase): ##merge

    tmp = {}

    for map_results in map_phrase:

        for map_result in map_results:

            l = tmp.get(map_result[0])

            if l:

                mergeMap(l,map_result[2],map_result[1])

            else:

                tmp[map_result[0]] = mergeMap(dict(),map_result[2],map_result[1])



    return tmp



def select(m): ##select top k labels

    u = sorted(m.items(),key = lambda x:x[1],reverse=True)

    if len(u) >=3 and ((u[0][1] - u[1][1]) > (u[1][1] - u[2][1])):

        uu = u[:2]

    else:

        uu = u[:3]

    s = sum([x[1] for x in uu])

    return dict( [(x[0],(x[1]+0.0)/s) for x in uu])



def close():

    print (label_vector)



label_vector = [None] * getMaxId()

group_map = {}



if __name__ == '__main__':

    for loop in xrange(7):

        gdata_file = file(path,"r")

        map_phrase = map(mapFunc, gdata_file.xreadlines())

        group_map = reduceFunc(map_phrase)

        gdata_file.close()



        for k,v in group_map.iteritems():

            label_vector[k] = select(v)



    close()