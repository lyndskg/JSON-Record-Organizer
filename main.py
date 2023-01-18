
import sys
import json
import heapq

def main():
    path = sys.argv[1] # path command line variable
    n = int(sys.argv[2]) # "n" command line variable

    try: # tries to open file at path 
        f = open(path, "r")
    except: # returns 1 if input file is not found 
        print("File not found")
        return 1

    line = f.readline() # reads first line

    h = [] # instantiates array used for priority queue

    stored = 0 # number of records kept 

    while line != "": # reads line until EOF 
        if len(line) == 1 and line[0] == "\n": # empty line case
            line = f.readline()
            continue

        for i in range(len(line)): # iterates until first colon to identify score
            if line[i] == ":":
                break
        
        score = int(line[:i])

        if "id" not in j: # if record contains no ID field, return 2
            print("ID not found")
            return 2
        
        id = j["id"] # grabs ID from JSON "j"

        if stored < n: # case where # of records kept is less than "n"
            try: # tries to load JSON into variable "j"
                j = json.loads(line[i + 1:])
            except: # returns 2 if record is not valid JSON
                print("JSON not valid")
                return 2

            heapq.heappush(h, (score, id)) # pushes score into priority queue
            stored += 1
        else: # case where # of records kept is equal to "n"
            try: # tries to load JSON into variable "j"
                j = json.loads(line[i + 1:])
            except: # returns 2 if record is not valid JSON
                print("JSON not valid")
                return 2
                
            if score > h[0][0]: # if score is within top "n" scores
                heapq.heappop(h) # pops smallest score from the priority queue
                heapq.heappush(h, (score, id)) # pushes new score and ID into priority queue
                stored += 1
        
        line = f.readline() # reads next line
    
    f.close()

    final = []

    while h: # loops through priority queue array 
        record = heapq.heappop(h) # stores record of and pops top of priority queue
        temp = {}
        temp["score"] = record[0] # retrieves score of record
        temp["id"] = record[1] # retrieves id of record
        final.append(temp) # appends record to final output 
    

    print(final[::-1]) # prints final output



main()