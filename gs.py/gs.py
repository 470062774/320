import json
import time

def write_json(obj, filename):
    with open(filename, mode='w') as f:
        json.dump(obj, f)


def read_json(filename):
    with open(filename) as f:
        return json.load(f)

if __name__ == '__main__':
    start_time = time.process_time()

    finallis=[]
    data = read_json('big_prob_input.json')
    '''
    manlist:  {'j0': ['k2', 'k1', 'k0'], 'j1': ['k2', 'k1', 'k0'], 'j2': ['k0', 'k2', 'k1']}
    man;  ['j0', 'j1', 'j2']
    manpreferlist:  ['k2', 'k1', 'k0']
    womanlist:  {'j0': ['k2', 'k1', 'k0'], 'j1': ['k2', 'k1', 'k0'], 'j2': ['k0', 'k2', 'k1']}
    womanpreferlist:  ['k2', 'k1', 'k0']
    {'j0': 'k2', 'j1': 'k1', 'j2': 'k0'}
    '''
    num=0
    while(num < len(data)):


        li=data[num]
    #print('dict is:',li)
        manlist = li[0]
    #print('manlist is:', manlist)
        man=list(manlist.keys())
    #print('man is:',man)
        manpreferlist=manlist[man[0]]
    #print('manpreferlist is:',manpreferlist)


        womanlist=li[1]
    #print('womanlist is:', womanlist)
        woman=list(womanlist.keys())
    #print('woman is:', woman)




        matchdict = {}

    #while(len(manlist) != 0):

    #return matchdict


        while(len(man) != 0):
            manpick=man[0]
            womanpick=manlist[man[0]][0]
            manlist[man[0]].remove(womanpick)
            man.remove(manpick)
            if(womanpick in matchdict.values()):
                womancurrent=list(matchdict.keys())[list(matchdict.values()).index(womanpick)]
                womanpreferlist = womanlist[womanpick]
                if(womanpreferlist.index(manpick) < womanpreferlist.index(womancurrent)):
                    matchdict.pop(womancurrent)
                    matchdict[manpick]=womanpick
                    man.append(womancurrent)
                else:
                    man.append(manpick)
            else:
                matchdict[manpick]=womanpick

        num = num + 1
        finallis.append(matchdict)

    print(finallis)

    write_json(finallis,'output.txt')

    end_time = time.process_time()
    # write output file
    print("Ran in: {:.5f} secs".format(end_time - start_time))