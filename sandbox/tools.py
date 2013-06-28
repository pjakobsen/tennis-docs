import json
from pprint import pprint

def dict_from_courses_md():
    # 
    '''
    id:1,
	month:1,
	stroke:"all",
	"title": "Month 1: Lecture-Introduction to the 45 degree angle"
	"url": "http://www.schooloftennis.net/start-here/instruction/quarter-1/month-1-introduction-to-the-45-angle/"
	"video": "MO1Begin_45Degree"
	"type": "lecture"
	"description": "
    '''
    file = open('sot.md')
    lessons=[]
    month = 1
    type = 'lesson'
    id = 1
    
    for line in file:
        stroke='all'
        if not line:continue
        if "CLASSES" in line:continue
        if "Month " in line: continue
        if "Month " in line: month = line.split("Month ")[1].split(":")[0]
        elif "Lecture" in line: type=="lecture"
        else:
            lecture_number = line.split(" ")[0]
            title = line[2:].strip()
        print line
        if "orehand" in title: stroke = "forehand"
        elif "ackhand" in title: stroke = "backhand"
        elif "olley" in title: stroke = "volley"
        elif "erve " in title: stroke = "serve"
        if "drill" in title: type="drills"
        if len(title)>5:
            lesson={'id':id, 'month':month, 'stroke':stroke,'name':title, 'type':type }
            #print lesson
            lessons.append(lesson)
            id+=1
        
    out = open("sot.json","w")   
    for l in lessons: 
        pprint(l)    
        out.write(json.dumps(l)+"\n")
    out.close()
        

if __name__ == "__main__":
    pass
    #dict_from_courses_md()
    