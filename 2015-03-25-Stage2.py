
 
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

print generate_concept_HTML("Hello", "This is sweet")

# This is an example of what a concept would look like as a list.
EXAMPLE_CONCEPT = ["Python", "Python is a programming language"]

# This is the function you will complete
def make_HTML(title, description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + description
    html_text_3 = '''
    </div>
</div>'''
    
    generate_concept_HTML = html_text_1 + html_text_2 + html_text_3
    
    # your code should assign values to two variables 
    # (title and description) so that the call to 
    # generate_concept_HTML below works as expected.
    return generate_concept_HTML

print make_HTML("Python", "Python is a programming language")
# The previous line of code should print:
"""
<div class="concept">
    <div class="concept-title">
        Python
    </div>
    <div class="concept-description">
        Python is a programming language
    </div>
</div>
"""



# This is Andy's Solution. You should read through the code if 
# you're feeling stuck or if you're just interested in one way
# to solve the problem.
#
# You're page is probably using a different HTML structure.
# If that's the case, you may want to modify the 
# generate_concept_HTML function to better suit your HTML.
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
