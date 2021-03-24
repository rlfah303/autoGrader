import requests
import json

def validate_html():
    # get script from website
    print("\n","Which website you want to validate?")
    website_to_validate = input()
    response = requests.get("https://validator.w3.org/nu/?doc="+website_to_validate)
    script=response.text
    
    ## debuging website script
    #print(script)
    print("There are",script.count("Error</strong>"),"errors to fix!");
   
    
validate_html()

# def validate_css():
#     # get script from website
#     print("\n","Which website you want to validate?")
#     website_to_validate = input()
#     response = requests.get("https://jigsaw.w3.org/css-validator/validator?uri="+website_to_validate+"&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en")
#     script=response.text
  
#     #finding index for error
#     try:
#         index_number = script.index("Sorry")+38
#         print("Therea are",script[index_number:index_number+2],"errors to fix!")
#     except:
#         print("There are no errors")
    
# validate_css()

    

#------references
'''
https://www.youtube.com/watch?v=hpc5jyVpUpw
https://validator.w3.org
https://jigsaw.w3.org/css-validator
'''

#-----test websites---------
'''
https://www.simplesite.com
https://www.byuh.edu
https://manoa.hawaii.edu

https://jigsaw.w3.org/css-validator/
'''





