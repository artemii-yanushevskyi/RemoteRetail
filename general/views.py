from django.shortcuts import render

def cv_page(request):
    with open('/home/fabulous/cv.md', 'r', encoding='utf-8') as f:
        text = f.read()
    cv = text.replace("\n", "\\n")
    return render(request, 'general/cv.html', {'md': cv})
