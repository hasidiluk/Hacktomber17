import math
import sys


v = 0

eps = -1E-3
DEBUG = 0
debugMaxDist =0
bestData = ""
# all = raw_input()
numbers = map(int, raw_input().split())
n=numbers[0]
x0=[0]*n
y0=[0]*n
x1=[0]*n
y1=[0]*n
# print n,numbers
# for i in n:
#     print i
len = numbers[1:]
#print len
    # x0[i]=raw_input()
    # y0[i] = raw_input()
    # x1[i] = raw_input()
    # y1[i] = raw_input()
maxDist = 0
maxSides = n - (n+1)%2
# def swap(premium, i, j):
#     assert type(premium) == list
#     print premium,i,j
#     tmp = permium[i]
#     premium[i]=premium[j]
#     premium[j]=tmp

def segSeq(nVers):
    s = "" + len[0]
    for i in range(1,nVers,2):
        s += "\n     " + x0[i] + " " + y0[i] + " " + x1[i] + " " + y1[i] +" " + x1[i + 1] + " " + y1[i + 1]
        return s

def buggyData(nver):
    global debugMaxDist
    if (DEBUG == 0): return
    thisTop = 0
    thisMin = 200
    for i in range(1,nver,2):
        thisTop = max(thisTop,y1[i])

    if thisTop > debugMaxDist :
        debugMaxDist = thisTop
        bestData = "Max: " + thisTop + " " + segSeq(nver)


def mix(iPrem):
    global maxDist,maxSides
    if iPrem == maxSides:
        # print iPrem
        buggyData(iPrem)
        return maxDist
    # print 'it sucks here'
    for i in range(iPrem,n):
        #swap(len, iPrem, i)
        # print len[i],len[iPrem]
        len[i],len[iPrem]=len[iPrem],len[i]
        # print len[i], len[iPrem]
        # print len[0],len[iPrem]
        if (iPrem % 2 == 1):
            mix(iPrem + 1)
        elif iPrem == 0:
            x1[0] = len[0]
            mix(1)
        else:
            build(iPrem - 1, iPrem - 2)
            if (iPrem > 3):
                build(iPrem - 1, iPrem - 3)
        #swap(len, iPrem, i)
        len[i], len[iPrem] = len[iPrem], len[i]
    return maxDist


def build(i,e):
    D = len[e]
    r1 = len[i]
    r2 = len[i + 1]
    dx = x1[e] - x0[e]
    dy = y1[e] - y0[e]
    E = (r1 * r1 - r2 * r2 + D * D) / (2 * D)
    inRadical = r1 * r1 - E * E
    if inRadical <= 0:
        buggyData(i)
        return
    F = inRadical**(0.5)
    global maxDist
    for k in range(0,2,1):
        y1[i] = y0[i + 1] = y0[e] + (F * dx + E * dy) / D
        if y1[i]<=eps:
            buggyData(i)
        else:
            if y1[i] > maxDist:
                maxDist = y1[i]
            x1[i] = x0[i + 1] = x0[e] + (E * dx - F * dy) / D
            y0[i] = y0[e]
            x0[i] = x0[e]
            x1[i + 1] = x1[e]
            y1[i + 1] = y1[e]
            mix(i + 2)

        F = -F

n= mix(0)
print n







