from bs4 import BeautifulSoup

with open('./Basic/home.html','r' ) as html_file:
    content= html_file.read()
    # print(content)
    
    soup= BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    
#for 1st tag item:   
    tags= soup.find('h3')
    
#for all tag items: 
    tags= soup.find_all('h5')
    print(tags)
 
#only course names   
    courses_html_tags= soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)
    
#for course cards
    course_card = soup.find_all('div', class_ = 'card')
    for course in course_card:
        course_name = course.h5.text
        course_price= course.a.text.split()[-1]
        print(course_name)
        print(course_price)
        
        print(f'{course_name} costs {course_price}')