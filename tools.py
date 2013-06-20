def dict_from_courses():
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
    for line in file:
        month = 1
        print line
        if "Month " in title: month = line.split("Month ")[1]
        
        
        
        

if __name__ == "__main__":
    dict_from_courses()
    